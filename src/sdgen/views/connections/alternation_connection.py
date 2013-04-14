# -*- coding: utf-8 -*-
from sdgen.fields import AlternationArrow
from connection import Connection


class AlternationConnection(Connection):
    def set_arrow_handlers(self, size, handlers, left_length=0, right_length=0):
        self.size = size
        self.handlers = handlers
        self.left_length = left_length
        self.right_length = right_length

    def render(self):
        assert getattr(self, 'size', False), "Arrow size undefined"
        arrow = self.get_field(AlternationArrow, self.size, self.handlers, left_length=self.left_length, right_length=self.right_length)
        return self.render_view(arrow)
