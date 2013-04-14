# -*- coding: utf-8 -*-
from sdgen.fields import DetourArrow
from _loop import LoopConnection


class DetourConnection(LoopConnection):
    def get_loop_arrow_class(self):
        return DetourArrow
