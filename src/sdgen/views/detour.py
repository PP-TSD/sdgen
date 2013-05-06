# -*- coding: utf-8 -*-
from connections import DetourConnection
from _loop import Loop


class Detour(Loop):
    """
    Detour view shows that it's child is optional in described expression.
    
    In regular expression detour is written by '?', it means preceding
    group is not required.
    
    .. seealso:: :class:`sdgen.views._loop.Loop`
    """
    def get_absolute_subfield_handlers(self, subfield):
        return {
            # in points
            "left": subfield.get_height() - subfield.get_handler('left'),
            "right": subfield.get_height() - subfield.get_handler('right')
        }

    def get_arrow_position(self, subfield):
        return (0, subfield.get_handlers()['left'])
    
    def get_connection_class(self):
        return DetourConnection

    def get_subfield_position(self, left_arrow_width):
        return left_arrow_width, 0
