# -*- coding: utf-8 -*-
from sdgen.config import render_config, safeget


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
