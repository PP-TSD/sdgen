# -*- coding: utf-8 -*-
from sdgen.fields.character import Character
from sdgen.fields.rounded_rectangle import RoundedRectangle
from sdgen.fields.flattener import Flattener
from _view import View


class Terminal(View):
    padding = 0

    def __init__(self, *args, **kwargs):
        super(Terminal, self).__init__(*args, **kwargs)
        if self.value == ' ':
            self.value = "Space"

    def render(self):
        text = self.render_image(self.get_field(Character, self.value, marked=self.marked))
        border = self.render_image(self.get_field(RoundedRectangle, tuple(p + self.padding * 2.0 for p in text.get_size())))

        terminal = Flattener(border, [(text, ((border.get_width() - text.get_width()) / 2,
                                              (border.get_height() - text.get_height()) / 2))])
        return self.render_view(terminal)
