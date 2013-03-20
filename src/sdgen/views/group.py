# -*- coding: utf-8 -*-
from itertools import tee, izip

from ._view import View
from .connection import Connection
from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.fields.character import Character
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.simple_arrow import SimpleArrow
from sdgen.fields.flattener import Flattener


class Group(View):
    arrow_height = 1
    arrow_width = 10
    border_size = 1

    def get_arrow(self, x_offset, y_offset):
        arrow = SimpleArrow((self.arrow_width, self.arrow_height)).to_png()
        arrow.set_position(x_offset, y_offset)
        return arrow

    def render(self):
#        fields = []
#        max_y = 0
#
#        for subfield in self.subfields:
#            # image
#            field = subfield.render()
#            group_max_y = 0
#
#            # calculate max y
#            for f in field:
#                group_max_y = max(group_max_y, f.y + f.height)
#
#            # add field group to set
#            fields.append((field, group_max_y))
#            max_y = max(max_y, group_max_y)
#
#        layer = []
#        x_offset = self.border_size
#
#        header = Character(self.name).to_png()
#        header.set_position(self.border_size, self.border_size)
#        header_height = header.height + self.border_size
#
#        for (field_group, group_max_y) in fields:
#            layer.append(self.get_arrow(x_offset, max_y/2))
#            x_offset += self.arrow_width
#            group_max_x = 0
#
#            for field in field_group:
#                group_max_x = max(field.x, group_max_x)
#                field.apply_offset(x_offset, (max_y - group_max_y)/2 + header_height)
#                layer.append(field)
#
#            x_offset += group_max_x
#
#        # end arrow
#        layer.append(self.get_arrow(x_offset, max_y/2))
#        x_offset += self.arrow_width
#
#        # border
#        border = Rectangle((x_offset, max_y+header_height)).to_png()
#        border.set_position(0, 0)
#        layer.append(border)

        # render ImageWrappers of fields
        fields = [subfield.render() for subfield in self.subfields]

        connections = []
        # add connections
        for i in range(len(fields) - 1):
            if not isinstance(self.subfields[i], Connection) and not isinstance(self.subfields[i+1], Connection):
                connection = Connection(fields[i], fields[i+1])
                connections.append((connection, i+1))

        for connection, position in reversed(connections):
            fields.insert(position, connection.render())
        
        def next_field():
            x = 10
            for field in fields:
                yield field, (x, 10)
                x += field.get_size()[0]

        header = self.render_image(Character(self.name))
        header_height = header.height + self.border_size
        
        width = sum(map(lambda f: f.get_size()[0], fields)) + 10
        height = max(map(lambda f: f.get_size()[1], fields)) + header_height

        background = self.render_image(Rectangle((width, height)))
        field = Flattener(background, list(next_field()))

        return self.render_image(field)
