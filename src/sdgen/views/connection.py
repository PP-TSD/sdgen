# -*- coding: utf-8 -*-

from ._view import View
from sdgen.utils.image_wrapper import ImageWrapper


class Connection(View):
    def __init__(self, first, second, *args, **kwargs):
        self.first = first
        self.second = second
