# -*- coding: utf-8 -*-
from ._view import View
from ..fields.character import Character
from ..fields.rounded_rectangle import RoundedRectangle


class Terminal(View):
    text_x_offset = 3
    text_y_offset = 2

    def render(self):
        text = self.render_image(Character(self.value))
        border = RoundedRectangle((text.get_size()[0] + self.text_x_offset * 2, text.get_size()[1] + self.text_y_offset * 2)).to_png()

        text.set_position(self.text_x_offset, self.text_y_offset)
        border.set_position(0, 0)

        terminal = self.paste(border, text, (0, 0))
        return terminal
