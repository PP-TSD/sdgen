# -*- coding: utf-8 -*-
from ._view import View
from ..fields.character import Character
from ..fields.rounded_rectangle import RoundedRectangle
from ..fields.flattener import Flattener


class Terminal(View):
    padding = 3

    def render(self):
        if self.value == ' ':
            self.value = "Space"
        text = self.render_image(Character(self.value))
        border = self.render_image(RoundedRectangle(tuple(self.px_to_pt(p) + self.padding * 2 for p in text.get_size())))

        terminal = Flattener(border, [(text, (self.pt_to_px(self.padding),) * 2)])
        return self.render_view(terminal)
