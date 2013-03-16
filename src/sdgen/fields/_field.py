# -*- coding: utf-8 -*-


class Field(object):
    """ Base field class. """    
    def to_png(self):
        raise NotImplementedError()
    
    def to_svg(self):
        raise NotImplementedError()
