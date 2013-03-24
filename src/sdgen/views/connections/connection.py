# -*- coding: utf-8 -*-

from .._view import View
from sdgen.fields.simple_arrow import SimpleArrow


class Connection(View):
    def render(self):
        return self.render_image(SimpleArrow((20, 0)))
