# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.utils import helpers

from _field import Field


class Rectangle(Field):
    thickness = 1
    fill = "transparent"
    outline = "black"
    marked_outline = "red"
    marked_fill = "yellow"

    def __init__(self, size, *args, **kwargs):
        """Render rectangle.

        Args:
            size (tuple): width, height of rectangle.

        Kwargs:
            thickness (int): thickness of rectangle border.
            fill (str): filling color (default transparent).
            outline (str): outline color (default black).
        """
        super(Rectangle, self).__init__(*args, **kwargs)
        self.size = size

    def to_png(self):
        size = map(self.pt_to_px, self.size)
        image = Image.new('RGBA', size)
        draw = ImageDraw.Draw(image)
        fill = helpers.standarize_colors(self.fill)
        width, height = size
        thickness = self.pt_to_px(self.thickness)

        draw.rectangle((0, 0, width - 1, height - 1),
                       fill=self.outline, outline=self.outline)
        draw.rectangle((0 + thickness, 0 + thickness,
                        width - 1 - thickness,
                        height - 1 - thickness),
                       fill=fill, outline=fill)
        return ImageWrapper(image, *self.size)
