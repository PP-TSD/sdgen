# -*- coding: utf-8 -*-
from sdgen._configurable_mixin import ConfigurableMixin


class Field(ConfigurableMixin):
    """ Base field class. """

    def to_png(self):
        raise NotImplementedError()

    def to_svg(self):
        raise NotImplementedError()
