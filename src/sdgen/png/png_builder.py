# -*- coding: utf-8 -*-
import os
import sys

from ..builder import Builder
from ..views._view import View


class PNGBuilder(Builder):
    """
    PNG syntax diagrams generator.
    """
    def generate(self, data, path):
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

        image = super(PNGBuilder, self).generate(data, path)
        raw_image = image.get_image()
        # save as running script name with png extension
        path = os.path.join(path, os.extsep.join((os.path.splitext(sys.argv[0])[0], 'png')))
        raw_image.save(path)
        return raw_image
