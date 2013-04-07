# -*- coding: utf-8 -*-
from sdgen.views.connections._loop import LoopConnection
from sdgen.fields.detour_arrow import DetourArrow


class DetourConnection(LoopConnection):
    def get_loop_arrow_class(self):
        return DetourArrow