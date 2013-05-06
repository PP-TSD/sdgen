# -*- coding: utf-8 -*-
from connections.return_connection import ReturnConnection
from _loop import Loop


class Return(Loop):
    """
    Return view shows that it's child occurs many times.
    
    To specify number of occurrences use
    :class:`sdgen.views.quantity_above.QuantityAbove`.
    
    .. seealso:: :class:`sdgen.views._loop.Loop`
    """
    def get_connection_class(self):
        return ReturnConnection

    def get_absolute_subfield_handlers(self, subfield):
        return {
            "left": subfield.get_handler('left') + 2 * self.padding,
            "right": subfield.get_handler('right') + 2 * self.padding
        }

    def get_arrow_position(self, handlers):
        return (0, 0)

    def get_subfield_position(self, left_arrow_width):
        return (left_arrow_width, self.padding * 2)
