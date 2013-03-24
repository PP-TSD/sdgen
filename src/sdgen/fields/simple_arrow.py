# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.fields._field import antialiasing
from sdgen.utils.image_wrapper import ImageWrapper
from arrow import Arrow


@antialiasing
class SimpleArrow(Arrow):
    length = 10

    """ Arrow from left to right. """
    def to_png(self):
        width, height = map(self.pt_to_px, (self.length, self.marker * 2.0 / 3))
        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)
        draw.line((0, height/2, width, height/2), width=self.pt_to_px(self.thickness), fill=self.fill)
        draw.polygon([(width, height / 2),
                      (width - self.marker, height / 2 - self.marker / 3),
                     (width - self.marker, height / 2 + self.marker / 3)],
                     fill=self.fill,
                     )
        return ImageWrapper(image, width, height)
