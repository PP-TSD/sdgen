# -*- coding: utf-8 -*-
from sdgen.fields import Character
from terminal import Terminal


class InvTerminalChild(Terminal):
    _render_config_key = "invterminal"
    font_color = "white"
    background = "transparent"
    marked_font_color = "yellow"
    marked_background = "transparent"

    def render(self):
        text = self.get_field(Character,
                              self.value,
                              font_color=self.font_color,
                              background=self.background,
                              marked_font_color=self.marked_font_color,
                              marked_background=self.marked_background)
        return self.render_view(text)
