# -*- coding: utf-8 -*-
from ..builder import Builder

class PNGBuilder(Builder):
    """
    PNG syntax diagrams generator.
    """
    def generate(self, *args, **kwargs):
        """
        Generate png image with given data and configuration.

        Args:
            data:

        Kwargs:
            font_type (str): Name of font type, ex. 'arial'.
            size (int): Font size in points.
            typeface (str): Font typeface, ex. 'bold italic'.

        Returns:
            Image. Rendered image.
        """
        super(PNGBuilder, self).generate(*args, **kwargs)
