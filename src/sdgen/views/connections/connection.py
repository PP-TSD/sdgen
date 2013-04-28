# -*- coding: utf-8 -*-
from sdgen.fields import SimpleArrow
from sdgen.views._view import View


class Connection(View):
    render_config_key = "connection"
    render_config = {}
    sharp = True

    def render(self):
        return self.render_view(self.get_field(SimpleArrow, marked=self.marked, sharp=self.sharp, **self.render_config))
