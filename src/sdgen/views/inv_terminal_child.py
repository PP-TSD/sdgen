from .terminal import Terminal
from ..fields.character import Character


class InvTerminalChild(Terminal):
    last = False
    delimiter_width = 3
    font_color = "white"
    background = "black"

    def render(self):
        text = Character(self.value, font_color=self.font_color, background=self.background)
        return self.render_view(text)
