# -*- coding: utf-8 -*-
from sdgen.fields import ReturnArrow
from _loop import LoopConnection


class ReturnConnection(LoopConnection):
    """Return connection.
    
    Should be used only for mark connection.
    
    .. seealso:: :class:`sdgen.views.connections._loop.LoopConnection`
    """
    def get_loop_arrow_class(self):
        return ReturnArrow
