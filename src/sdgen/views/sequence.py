# -*- coding: utf-8 -*-
from sdgen.fields import Flattener
from _view import View
from connections.connection import Connection


class Sequence(View):
    """
    Sequence of views, separated by arrow.

    Arrows can be specified by putting
    :class:`sdgen.views.connections.connection.Connection` in children.
    If connection is not specified, default is used.
    """

    def add_children(self, children):
        extended_children = []
        for el1, el2 in self._pairs(children):
            el1_conn = isinstance(el1, Connection)
            el2_conn = isinstance(el2, Connection)
            # if one of siblings is connection or this is the last element
            if el1_conn != el2_conn or el2 is None:
                if el1_conn and el2 and el2.arrowhead:
                    el1.sharp = False
                extended_children.append(el1)
            # if siblings are not separated by connection, create connection
            elif not (el1_conn or el2_conn):
                extended_children.append(el1)
                extended_children.append(Connection(mark=self.marked, sharp=not el2.arrowhead))
            # in both cases only e1 is added to list, e2 will be added in next
            # loop iteration
        self.arrowhead = extended_children[0].arrowhead

        super(Sequence, self).add_children(extended_children)

    def render(self):
        # render ImageWrappers of fields
        fields = map(self.render_subview, self.subfields)

        top_max_height = max([max(x.get_handlers().values()) for x in fields])

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
        field = Flattener(list(next_field()))

        handlers = {
                    "left": top_max_height,
                    "right": right_handler
                    }
        rendered_fields = self.render_view(field)
        rendered_fields[0].update_handlers(handlers)
        return rendered_fields
