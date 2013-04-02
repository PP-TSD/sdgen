from ._view import View
from ..fields.rectangle import Rectangle


class InvTerminalDelimiter(View):
    width = 1
    height = 10
    fill = "white"
    outline = "white"

    def render(self):
        delimiter = Rectangle((self.width, self.height), fill=self.fill, outline=self.outline)
        return self.render_view(delimiter)
