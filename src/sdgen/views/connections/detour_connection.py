# -*- coding: utf-8 -*-
from sdgen.fields import DetourArrow
from _loop import LoopConnection


class DetourConnection(LoopConnection):
    """Detour connection.
    
    Should be used only for mark connection.
    
    .. seealso:: :class:`sdgen.views.connections._loop.LoopConnection`
    """
    def get_loop_arrow_class(self):
        return DetourArrow
