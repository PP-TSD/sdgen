# -*- coding: utf-8 -*-

class Builder(object):
    """
    Abstract builder for syntax diagrams.
    """

    def generate(self, *args, **kwargs):
        raise NotImplementedError()
