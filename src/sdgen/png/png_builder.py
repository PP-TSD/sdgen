# -*- coding: utf-8 -*-
import Image
import ImageDraw

from ..builder import Builder


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
        fields = super(PNGBuilder, self).generate(data, path, config)

        image = Image.new('RGBA', (500, 500))

        for field in fields:
            image.paste(field.get_image(), field.get_position())

        image.save(path)
        return image
