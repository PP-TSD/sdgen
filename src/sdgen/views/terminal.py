# -*- coding: utf-8 -*-
from ._view import View
from ..fields.character import Character
from ..fields.rounded_rectangle import RoundedRectangle
from ..fields.flattener import Flattener


class Terminal(View):
    text_x_offset = 3
    text_y_offset = 2

    def render(self):
        if self.value == ' ':
            self.value = "Space"
        text = self.render_image(Character(self.value))
        border = self.render_image(RoundedRectangle((text.get_size()[0] + self.text_x_offset * 2, text.get_size()[1] + self.text_y_offset * 2)))

        terminal = Flattener(border, [(text, (self.text_x_offset, self.text_y_offset))])
        return self.render_image(terminal)
