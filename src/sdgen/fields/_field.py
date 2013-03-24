# -*- coding: utf-8 -*-
import Image

from sdgen.config import render_config, safeget
from sdgen.utils.image_wrapper import ImageWrapper


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


class Field(object):
    """ Base field class. """
    render_config_key = "default"
    _render_config_default_key = "default"

    def __init__(self, render_config_key=None, *args, **kwargs):
        # overwrite default class value for this instance
        if render_config_key:
            self.render_config_key = render_config_key

    def from_render_config(self, key):
        return (safeget(render_config, ".".join((self.render_config_key, key))) or
                safeget(render_config, ".".join((self._render_config_default_key, key))))

    def to_png(self):
        raise NotImplementedError()

    def to_svg(self):
        raise NotImplementedError()

    def pt_to_px(self, points):
        return points
