# -*- coding: utf-8 -*-
import Image
import ImageDraw

from _field import Field
from sdgen.utils.image_wrapper import ImageWrapper


class Rectangle(Field):
    def __init__(self, size, thickness=1, fill="transparent", outline="black"):
        """Render rectangle.
    
        Args:
            size (tuple): width, height of rectangle.
    
        Kwargs:
            thickness (int): thickness of rectangle (in pixels).
            fill (str): filling color (default transparent).
            outline (str): outline color (default black).
        """
        self.size = size
        self.thickness = thickness
        self.fill = fill
        self.outline = outline

    def to_png(self):
        image = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(image)
        fill = self.fill if not self.fill=="transparent" else (0, 0, 0, 0)
        width, height = self.size

        draw.rectangle((0, 0, width - 1, height - 1),
                       fill=self.outline, outline=self.outline)
        draw.rectangle((0 + self.thickness, 0 + self.thickness,
                        width - 1 - self.thickness,
                        height - 1 - self.thickness),
                       fill=fill, outline=fill)
        return ImageWrapper(image, *self.size)
