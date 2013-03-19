# -*- coding: utf-8 -*-
from ._view import View
from sdgen.fields.character import Character
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.simple_arrow import SimpleArrow


class Group(View):
    arrow_height = 1
    arrow_width = 10
    border_size = 1

    def get_arrow(self, x_offset, y_offset):
        arrow = SimpleArrow((self.arrow_width, self.arrow_height)).to_png()
        arrow.set_position(x_offset, y_offset)
        return arrow

    def get_fields_representation(self):
        fields = []
        max_y = 0

        for subfield in self.subfields:
            # list of fields
            field = subfield.get_fields_representation()
            group_max_y = 0

            # calculate max y
            for f in field:
                group_max_y = max(group_max_y, f.y + f.height)

            # add field group to set
            fields.append((field, group_max_y))
            max_y = max(max_y, group_max_y)

        layer = set()
        x_offset = self.border_size

        header = Character(self.name).to_png()
        header.set_position(self.border_size, self.border_size)
        header_height = header.height + self.border_size

        for (field_group, group_max_y) in fields:
            layer.add(self.get_arrow(x_offset, max_y/2))
            x_offset += self.arrow_width
            group_max_x = 0

            for field in field_group:
                group_max_x = max(field.x, group_max_x)
                field.apply_offset(x_offset, (max_y - group_max_y)/2 + header_height)
                layer.add(field)

            x_offset += group_max_x

        # end arrow
        layer.add(self.get_arrow(x_offset, max_y/2))
        x_offset += self.arrow_width

        # border
        border = Rectangle((x_offset, max_y+header_height)).to_png()
        border.set_position(0, 0)
        layer.add(border)

        return layer
