# -*- coding: utf-8 -*-
from _loop import Loop
from connections.connection import Connection
from sdgen.views.connections.return_connection import ReturnConnection
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.flattener import Flattener
from sdgen.utils.antialiasing import antialiasing


class Return(Loop):
    padding = 8
    thickness = 2

    def get_connection_class(self):
        return ReturnConnection

    def get_handlers_relative_to_subfield(self, subfield, padding):
        return {
                # in pixels
                "left": subfield.get_handler('left') + 2 * padding,
                "right": subfield.get_handler('right') + 2 * padding
            }

    def get_arrow_position(self, handlers):
        return (0, 0)

    def get_subfield_position(self, left_arrow_width, padding):
        return (left_arrow_width, padding * 2)