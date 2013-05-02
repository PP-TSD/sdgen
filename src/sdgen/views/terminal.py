# -*- coding: utf-8 -*-
from sdgen.fields.character import Character
from sdgen.fields.rounded_rectangle import RoundedRectangle
from sdgen.fields.flattener import Flattener
from _view import View


class Terminal(View):
    """
    Rounded rectangle with text inside.
    If value of Terminal is ' ', it's converted to 'Space'.

    .. attribute:: font_size : int

        Size of font used to generate inside text.
        Default: 15

    .. attribute:: font_typeface : int

        Font style.
        Default: regular
    """

    padding = 5
    font_size = 15
    font_typeface = "regular"

    def __init__(self, *args, **kwargs):
        super(Terminal, self).__init__(*args, **kwargs)
        if self.value == ' ':
            self.value = "Space"

    def render(self):
        kwargs = {
            "marked": self.marked
        }
        if self.value == "Space":
            kwargs["font_typeface"] = "italic"
        text = self.render_image(self.get_field(Character, self.value, **kwargs))
        border = self.render_image(self.get_field(RoundedRectangle, tuple(p + self.padding * 2.0 for p in text.get_size())))

        terminal = Flattener([
            (border, (0,0)),
            (text, ((border.get_width() - text.get_width()) / 2,
                        (border.get_height() - text.get_height()) / 2))
        ])
        return self.render_view(terminal)
