# -*- coding: utf-8 -*-
from ._view import View
from .connections.connection import Connection
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.flattener import Flattener


class Sequence(View):
    padding = 10
    arrow_height = 1
    arrow_width = 10

    def add_children(self, children):
        extended_children = []
        for el1, el2 in self._pairs(children):
            el1_conn = isinstance(el1, Connection)
            el2_conn = isinstance(el2, Connection)
            if el1_conn != el2_conn or el2 is None:
                extended_children.append(el1)
            elif not (el1_conn or el2_conn):
                extended_children.append(el1)
                extended_children.append(Connection())
        super(Sequence, self).add_children(extended_children)

    def render(self):
        # render ImageWrappers of fields
        fields = map(self.render_subview, self.subfields)

        top_max_height = max([max(x.get_handlers().values()) for x in fields])
        bottom_max_height = max([x.get_height() - min(x.get_handlers().values()) for x in fields])

        width = sum(map(lambda f: f.get_width(), fields))
        height = top_max_height + bottom_max_height

        def next_field():
            x = 0
            assert fields, "Empty group"
            # previous field can have not inline handlers (eg. _[]- )
            # it must be corrected in this field
            diff = fields[0].get_handler('right') - fields[0].get_handler('left')
            for field in fields:
                yield field, (x, diff + top_max_height - field.get_handler('left'))
                diff += field.get_handler('right') - field.get_handler('left')
                x += field.get_width()
        positioned_fields = list(next_field())

        # get y coordinate of last fields and add it's right handler
        right_handler = positioned_fields[-1][1][1] + positioned_fields[-1][0].get_handler('right')
        background = self.render_image(Rectangle((width, height), thickness=0))
        field = Flattener(background, list(next_field()))

        handlers = {
                    "left": top_max_height,
                    "right": right_handler
                    }
        rendered_fields = self.render_view(field)
        rendered_fields[0].update_handlers(handlers)
        return rendered_fields
