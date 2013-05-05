# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.antialiasing import antialiasing
from sdgen.utils.image_wrapper import ImageWrapper

from _arrow import Arrow


@antialiasing
class SimpleArrow(Arrow):
    """Arrow from left to right. """
    length = 20
    sharp = True

    def __init__(self, *args, **kwargs):
        """Straight, horizontal arrow ended with marker.

        :attribute length: float
        length of arrow with marker (in points).
        """
        super(SimpleArrow, self).__init__(*args, **kwargs)
        self.sharp = self.sharp

    def to_png(self):
        width = self.pt_to_px(self.length)
        height = self.pt_to_px(self.marker * 2.0 / 3 or self.thickness)
        marker = self.pt_to_px(self.marker)
        thickness = self.pt_to_px(self.thickness)
        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)

        draw.line((0, height/2, width - marker * self.sharp, height/2),
                  width=thickness, fill=self.fill)
        draw.polygon([(width, height / 2),
                      (width - marker, height / 2 - marker / 3),
                     (width - marker, height / 2 + marker / 3)],
                     fill=self.fill,
                     )
        return ImageWrapper(image, self.length, self.px_to_pt(height))
