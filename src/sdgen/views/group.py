# -*- coding: utf-8 -*-
from ._view import View
from ..fields.character import Character
from ..fields.rectangle import Rectangle


class Group(View):
    arrow_length = 10
    border_size = 1

    def get_arrow(self, x_offset, y_offset):
        pass

    def get_fields_representation(self):
        fields = []
        max_y = 0

        for subfield in self.subfields:
            # list of fields
            field = subfield.get_fields_representation()
            group_max_y = 0

            # calculate max y
            for f in field:
                group_max_y = max(group_max_y, f[1][1]+f[0].get_size()[1])

            # add field group to set
            fields.append((field, group_max_y))
            max_y = max(max_y, group_max_y)

        layer = set()
        x_offset = self.border_size

        header = (Character(self.name).to_png(), [self.border_size, self.border_size])
        header_height = header[0].get_size()[1] + self.border_size

        for (field_group, group_max_y) in fields:
            layer.add(self.get_arrow(x_offset, max_y/2))
            x_offset += self.arrow_length
            group_max_x = 0

            for field in field_group:
                group_max_x = max(field[1][0], group_max_x)
                # x offset
                field[1][0] += x_offset
                # y offset
                field[1][1] += (max_y - group_max_y)/2 + header_height
                layer.add(field)

            x_offset += group_max_x

        # end arrow
        layer.add(self.get_arrow(x_offset, max_y/2))
        x_offset += self.arrow_length

        # border
        layer.add((Rectangle((x_offset, max_y+header_height)), (0, 0)))

        return layer
