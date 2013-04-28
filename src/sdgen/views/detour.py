# -*- coding: utf-8 -*-
from connections import DetourConnection
from _loop import Loop


class Detour(Loop):
    padding = 10
    thickness = 2

    def get_connection_class(self):
        return DetourConnection

    def get_handlers_relative_to_subfield(self, subfield):
        return {
            # in points
            "left": subfield.get_height() - subfield.get_handler('left'),
            "right": subfield.get_height() - subfield.get_handler('right')
        }

    def get_arrow_position(self, subfield):
        return (0, subfield.get_handlers()['left'])

    def get_subfield_position(self, left_arrow_width):
        return left_arrow_width, 0
