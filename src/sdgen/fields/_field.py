# -*- coding: utf-8 -*-
import Image

from sdgen._configurable_mixin import ConfigurableMixin


class Field(ConfigurableMixin):
    """ Base field class. """

    def to_png(self):
        raise NotImplementedError()

    def to_svg(self):
        raise NotImplementedError()

    def pt_to_px(self, points):
        return int(points)
    
    def px_to_pt(self, points):
        return float(points)
