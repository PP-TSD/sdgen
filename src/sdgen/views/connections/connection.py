# -*- coding: utf-8 -*-

from .._view import View
from sdgen.fields.simple_arrow import SimpleArrow


class Connection(View):
    render_config_key = "connection"

    def render(self):
        return self.render_view(SimpleArrow())
