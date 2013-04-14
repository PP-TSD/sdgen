# -*- coding: utf-8 -*-
from sdgen.fields import DetourArrow
from connections._loop import LoopConnection


class DetourConnection(LoopConnection):
    def get_loop_arrow_class(self):
        return DetourArrow
