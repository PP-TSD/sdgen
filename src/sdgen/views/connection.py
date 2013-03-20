# -*- coding: utf-8 -*-

from ._view import View
from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.fields.simple_arrow import SimpleArrow

class Connection(View):
    def __init__(self, first, second, *args, **kwargs):
        """ First and second are ImageWrappers. """
        self.first = first
        self.second = second

    def render(self):
        return self.render_image(SimpleArrow((20, 0)))
