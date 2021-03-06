# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.antialiasing import antialiasing
from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.utils import helpers

from _field import Field


@antialiasing
class RoundedRectangle(Field):
    thickness = 2
    fill = "transparent"
    outline = "black"
    marked_outline = "red"
    marked_fill = "yellow"

    def __init__(self, size, *args, **kwargs):
        """Render rectangle with half-circles on sides.

        If width is less than height result will be circle with diameter=height

        Args:
            size (tuple): width, height of rectangle.

        Kwargs:
            thickness (float): thickness of rectangle (in points).
            fill (str): filling color (default transparent).
            outline (str): outline color (default black).
        """
        super(RoundedRectangle, self).__init__(*args, **kwargs)
        self.size = (max(size), size[1])
        assert self.thickness <= min(self.size)/2, 'Thickness is too large'

    def to_png(self):
        size = tuple([self.pt_to_px(p) for p in self.size])
        thickness = self.pt_to_px(self.thickness)
        image = Image.new('RGBA', size)
        draw = ImageDraw.Draw(image)
        fill = helpers.standarize_colors(self.fill)

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

        return ImageWrapper(image, *self.size)