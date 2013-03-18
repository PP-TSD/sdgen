# -*- coding: utf-8 -*-
from ._view import View
from ..fields.character import Character
from ..fields.rounded_rectangle import RoundedRectangle


class Terminal(View):
    text_x_offset = 3
    text_y_offset = 2

    def get_fields_representation(self):
        text = Character(self.value).to_png()
        border = RoundedRectangle((text.get_size()[0] + self.text_x_offset * 2, text.get_size()[1] + self.text_y_offset * 2)).to_png()

        terminal = set([(text, (self.text_x_offset, self.text_y_offset)),
                        (border, (0, 0))
                        ])

        return terminal
