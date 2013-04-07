# -*- coding: utf-8 -*-
from _loop import Loop
from connections.connection import Connection
from sdgen.views.connections.detour_connection import DetourConnection
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.flattener import Flattener
from sdgen.utils.antialiasing import antialiasing


class Detour(Loop):
    padding = 8
    thickness = 2

    def get_connection_class(self):
        return DetourConnection

    def get_handlers_relative_to_subfield(self, subfield, padding):
        return {
                # in pixels
                "left": subfield.get_height() - subfield.get_handler('left'),
                "right": subfield.get_height() - subfield.get_handler('right')
            }
    
    def get_arrow_position(self, subfield):
        return (0, subfield.get_handlers()['left'])

    def get_subfield_position(self, left_arrow_width, padding):
        return left_arrow_width, 0
