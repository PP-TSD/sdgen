# -*- coding: utf-8 -*-
from sdgen.views.connections.connection import Connection


class LoopConnection(Connection):

    def get_loop_arrow_class(self):
        raise NotImplementedError

    def set_subfield_params(self, size, handlers):
        self.subfield_width, self.subfield_height = size  # in px
        self.left_height, self.right_height = handlers['left'], handlers['right']
        self.subfield_size = True

    def render(self):
        assert getattr(self, 'subfield_size', False), "Subfield size undefined"
        arrow_class = self.get_loop_arrow_class()
        loop = arrow_class(self.subfield_width,
                           self.left_height,
                           self.right_height,
                           left_length=self.left_length,
                           right_length=self.right_length,
                           marked=self.marked)
        return self.render_view(loop)
