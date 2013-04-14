# -*- coding: utf-8 -*-
from sdgen.fields import ReturnArrow
from _loop import LoopConnection


class ReturnConnection(LoopConnection):
    def get_loop_arrow_class(self):
        return ReturnArrow
