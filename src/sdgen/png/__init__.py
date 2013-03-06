# -*- coding: utf-8 -*-
from .png_builder import PNGBuilder


def to_png(*args, **kwargs):
    """
    Backward compatibility
    """
    return PNGBuilder().generate(*args, **kwargs)
