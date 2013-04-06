# -*- coding: utf-8 -*-
from sdgen.views.connections.connection import Connection
from sdgen.fields.detour_arrow import DetourArrow


class DetourConnection(Connection):
    def set_subfield_params(self, size, handlers):
        self.subfield_width, self.subfield_height = size  # in px
        self.left_height, self.right_height = handlers['left'], handlers['right']
        self.subfield_size = True
    
    def render(self):
        assert getattr(self, 'subfield_size', False), "Subfield size undefined"
        detour = DetourArrow(self.subfield_width, self.left_height,
                             self.right_height, left_length=self.left_length,
                             right_length=self.right_length)
        return self.render_view(detour)
