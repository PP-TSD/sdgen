from .terminal import Terminal
from ..fields.character import Character
from ..fields.rectangle import Rectangle
from ..fields.flattener import Flattener


class InvTerminalChild(Terminal):
    last = False
    delimiter_width = 3

    def render(self):
            if self.value == ' ':
                self.value = "Space"
            text = Character(self.value, font_color="white", background="black")
            if self.last:
                return self.render_view(text)
            else:
                text = self.render_image(text)
                delimiter = self.render_image(Rectangle((self.delimiter_width, self.px_to_pt(text.get_size()[1]))))
                background = self.render_image(Rectangle((10, 10)))
                field = Flattener(background, [(text, (0, 0)), (delimiter, (text.get_size()[0], 0))])
                return self.render_view(field)
