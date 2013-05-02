# -*- coding: utf-8 -*-
from sdgen.fields import Rectangle
from _view import View


class InvTerminalDelimiter(View):
    """
    Separator in Inverted Terminal.
    """
    _render_config_key = "invterminal"
    width = 1
    height = 10
    fill = "white"
    outline = "white"
    marked_fill = "yellow"
    marked_outline = "yellow"

    def render(self):
        delimiter = self.get_field(Rectangle,
                                   (self.width, self.height),
                                   fill=self.fill,
                                   outline=self.outline,
                                   marked_fill=self.marked_fill,
                                   marked_outline=self.marked_outline)
        return self.render_view(delimiter)
