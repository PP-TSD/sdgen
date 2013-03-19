# -*- coding: utf-8 -*-
import Image
import ImageDraw

from _field import Field
from sdgen.utils.image_wrapper import ImageWrapper


# factor of rounded corner 'top' position ROUND_FACTOR = 1 - 1 / sqrt(2)
ROUND_FACTOR = 0.2928932188134524756


class RoundedRectangle(Field):
    def __init__(self, size, thickness=1, fill="transparent", outline="black"):
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
        self.fill = fill
        self.outline = outline

        corner_padding = self.size[1] * ROUND_FACTOR
        self.handlers = {
                         "left-top": (corner_padding, corner_padding),
                         "left-bottom": (corner_padding,
                                         self.size[1] - corner_padding),
                         "right-top": (self.size[0] - corner_padding,
                                       corner_padding),
                         "right-bottom": (self.size[0] - corner_padding,
                                          self.size[1] - corner_padding),
                         }

    def to_png(self):
        image = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(image)
        fill = self.fill if not self.fill=="transparent" else (0, 0, 0, 0)

        width, height = self.size

        # outline
        draw.pieslice((0, 0, height, height), 180, 360,
                      fill=self.outline, outline=self.outline)
        draw.pieslice((width - height, 0, width, height), 0, 180,
                      fill=self.outline, outline=self.outline)
        draw.rectangle((height, 0, width - height - 1, height - 1),
                       fill=self.outline, outline=self.outline)
        #fill
        draw.pieslice((0 + self.thickness, 0 + self.thickness,
                       height - self.thickness, height - self.thickness), 180,
                      360, fill=fill, outline=fill)
        draw.pieslice((width - height + self.thickness, 0 + self.thickness,
                       width - self.thickness, height - self.thickness), 0,
                      180, fill=fill, outline=fill)
        draw.rectangle((height, 0 + self.thickness, width - height - 1,
                        height - self.thickness - 1), fill=fill, outline=fill)

        return ImageWrapper(image, width, height, self.handlers)
