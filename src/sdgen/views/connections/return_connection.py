# -*- coding: utf-8 -*-
from sdgen.views.connections._loop import LoopConnection
from sdgen.fields.return_arrow import ReturnArrow


class ReturnConnection(LoopConnection):
    def get_loop_arrow_class(self):
        return ReturnArrow