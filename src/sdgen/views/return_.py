# -*- coding: utf-8 -*-
from connections.return_connection import ReturnConnection
from _loop import Loop


class Return(Loop):
    padding = 10
    thickness = 2

    def get_connection_class(self):
        return ReturnConnection

    def get_handlers_relative_to_subfield(self, subfield):
        return {
            "left": subfield.get_handler('left') + 2 * self.padding,
            "right": subfield.get_handler('right') + 2 * self.padding
        }

    def get_arrow_position(self, handlers):
        return (0, 0)

    def get_subfield_position(self, left_arrow_width):
        return (left_arrow_width, self.padding * 2)
