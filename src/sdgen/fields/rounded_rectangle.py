# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.fields._field import antialiasing
from _field import Field
from sdgen.utils.image_wrapper import ImageWrapper


@antialiasing
class RoundedRectangle(Field):
    def __init__(self, size, thickness=1, fill="white", outline="black"):
        """Render rectangle with half-circles on sides.

        If width is less than height result will be circle with diameter=height

        Args:
            size (tuple): width, height of rectangle.

        Kwargs:
            thickness (int): thickness of rectangle (in pixels).
            fill (str): filling color (default transparent).
            outline (str): outline color (default black).
        """
        self.size = (max(size), size[1])
        self.thickness = thickness
        assert self.thickness <= min(self.size)/2, 'Thickness is too large'
        self.fill = fill
        self.outline = outline


    def to_png(self):
        size = tuple([self.pt_to_px(p) for p in self.size])
        thickness = self.pt_to_px(self.thickness)
        image = Image.new('RGBA', size)
        draw = ImageDraw.Draw(image)
        fill = self.fill if not self.fill=="transparent" else (0, 0, 0, 0)

        width, height = size
        half_height = int(height / 2)
        # outline
        draw.pieslice((0, 0, height - 1, height - 1), 90, 270,
                      fill=self.outline, outline=self.outline)
        draw.pieslice((width - height, 0, width - 1, height - 1), 270, 90,
                      fill=self.outline, outline=self.outline)
        draw.rectangle((half_height, 0, width - half_height - 1, height - 1),
                       fill=self.outline, outline=self.outline)
        #fill
        draw.pieslice((0 + thickness, 0 + thickness,
                       height - thickness - 1, height - thickness - 1), 90,
                      270, fill=fill, outline=fill)
        draw.pieslice((width - height + thickness, 0 + thickness,
                       width - thickness - 1, height - thickness - 1), 270,
                      90, fill=fill, outline=fill)
        draw.rectangle((half_height, 0 + thickness,
                        width - half_height - 1, height - thickness - 1),
                       fill=fill, outline=fill)

        return ImageWrapper(image, width, height)