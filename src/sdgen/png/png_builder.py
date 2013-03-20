# -*- coding: utf-8 -*-
import Image
import ImageDraw

from ..builder import Builder
from ..views._view import View


class PNGBuilder(Builder):
    """
    PNG syntax diagrams generator.
    """
    def generate(self, data, path, config):
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
        View._fn = "to_png"
        View.paste = lambda self, background, field, position: background.get_image().paste(field, position, field)

        field = super(PNGBuilder, self).generate(data, path, config)
        return field.get_image()
