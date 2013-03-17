# -*- coding: utf-8 -*-


class View(object):
    """
    Base class for all fields in sdgen.
    """

    def __init__(self, name=None, type=None, value=None, marked=False, *args, **kwargs):
        self.subfields = []
        self.name = name
        self.value = value
        self.marked = marked

    def add_child(self, child):
        self.subfields.append(child)

    def get_png(self):
        """
        Implements png generation with all subfields of this field.
        """
        raise NotImplementedError()

    def get_svg(self):
        raise NotImplementedError()
