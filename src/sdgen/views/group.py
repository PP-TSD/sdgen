# -*- coding: utf-8 -*-
from ._view import View
from sequence import Sequence
from .connections.connection import Connection
from sdgen.fields.character import Character
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.flattener import Flattener


class Group(View):
    render_config_key = "group"
    padding = 10
    header_padding = 5
    arrow_height = 1
    arrow_width = 10
    border_size = 1

    def add_children(self, children):
        extended_children = []
        if children:
            #first connection
            if isinstance(children[0], Connection):
                extended_children.append(children[0])
                children = children[1:]
            else:
                extended_children.append(Connection())
            #last connection
            if children:
                if isinstance(children[-1], Connection):
                    extended_children.append(children[-1])
                    children = children[:-1]
                else:
                    extended_children.append(Connection())
            sequence = Sequence()
            sequence.add_children(children)
            extended_children.insert(1, sequence)
        super(Group, self).add_children(extended_children)

    def render(self):
        # render ImageWrappers of fields
        padding = self.pt_to_px(self.padding)
        fields = [subfield.render() for subfield in self.subfields]
        border_size = self.pt_to_px(self.border_size)

        header = self.render_image(Character(self.name, font_color="white", background="black", padding=self.header_padding))

        top_max_height = max([max(x.get_handlers().values()) for x in fields])
        bottom_max_height = max([x.get_height() - min(x.get_handlers().values()) for x in fields])

        width = sum(map(lambda f: f.get_width(), fields)) + 2 * (padding + border_size)
        height = header.height + top_max_height + bottom_max_height + 2 * (padding + border_size)

        def next_field():
            x = padding + border_size
            assert fields, "Empty group"
            # previous field can have not inline handlers (eg. _[]- )
            # it must be corrected in this field
            diff = fields[0].get_handler('right') - fields[0].get_handler('left')
            for field in fields:
                yield field, (x, border_size + header.height + padding + diff + top_max_height - field.get_handler('left'))
                diff = field.get_handler('right') - field.get_handler('left')
                x += field.get_width()

        background = self.render_image(Rectangle((width, height), thickness=self.border_size))
        field = Flattener(background, [(header, (border_size, ) * 2)] + list(next_field()))

        return self.render_image(field)
