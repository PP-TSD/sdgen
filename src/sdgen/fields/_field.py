# -*- coding: utf-8 -*-
import Image

from sdgen.config import render_config, safeget
from sdgen.utils.image_wrapper import ImageWrapper
from sdgen._configurable_mixin import ConfigurableMixin


ANTIALIASING = 4


def antialiasing(klass):
    klass.pt_to_px = lambda *args, **kwargs: ANTIALIASING * klass.pt_to_px(*args, **kwargs) 
    
    def to_png(*args, **kwargs):
        image_wrapper = klass.to_png(*args, **kwargs)
        image = image_wrapper.get_image()
        new_width = image_wrapper.get_width() / ANTIALIASING
        new_height = image_wrapper.get_height() / ANTIALIASING
        image.resize(new_width, new_height, Image.ANTIALIAS)
        image_wrapper.scale_parameters(1.0/ANTIALIASING)
        return image_wrapper
    
    klass.to_png = to_png


class Field(ConfigurableMixin):
    """ Base field class. """

    def to_png(self):
        raise NotImplementedError()

    def to_svg(self):
        raise NotImplementedError()

    def pt_to_px(self, points):
        return points

