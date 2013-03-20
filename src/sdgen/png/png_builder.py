# -*- coding: utf-8 -*-
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
        View.renderer = "to_png"

        image = super(PNGBuilder, self).generate(data, path, config)
        raw_image = image.get_image()
        raw_image.save(path)
        return raw_image
