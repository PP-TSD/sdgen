# -*- coding: utf-8 -*-
from connections.return_connection import ReturnConnection
from _loop import Loop


class Return(Loop):
    padding = 3
    thickness = 2

    def get_connection_class(self):
        return ReturnConnection

    def get_handlers_relative_to_subfield(self, subfield, padding):
        return {
            "left": subfield.get_handler('left') + 2 * padding,
            "right": subfield.get_handler('right') + 2 * padding
        }

    def get_arrow_position(self, handlers):
        return (0, 0)

    def get_subfield_position(self, left_arrow_width, padding):
        return (left_arrow_width, padding * 2)
