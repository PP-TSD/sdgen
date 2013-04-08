# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.antialiasing import antialiasing
from sdgen.utils.image_wrapper import ImageWrapper
from arrow import Arrow


@antialiasing
class SimpleArrow(Arrow):
    length = 20

    """ Arrow from left to right. """
    def to_png(self):
        width = self.pt_to_px(self.length)
        height = self.pt_to_px(self.marker * 2.0 / 3 or self.thickness + 1)
        marker = self.pt_to_px(self.marker)
        thickness = self.pt_to_px(self.thickness)
        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)

        draw.line((0, height/2, width, height/2), width=thickness, fill=self.fill)
        draw.polygon([(width, height / 2),
                      (width - marker, height / 2 - marker / 3),
                     (width - marker, height / 2 + marker / 3)],
                     fill=self.fill,
                     )
        return ImageWrapper(image, self.length, self.px_to_pt(height))
