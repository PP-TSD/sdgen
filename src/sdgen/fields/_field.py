# -*- coding: utf-8 -*-

class Field(object):
    """
    Base class for all fields in sdgen.
    """


    def __init__(self):
        self.subfields = []

    def get_png(self):
        """
        Implements png generation with all subfields of this field.
        """
        raise NotImplementedError()

    def get_svg(self):
        raise NotImplementedError()
