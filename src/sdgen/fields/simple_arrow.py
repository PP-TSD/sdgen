# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.image_wrapper import ImageWrapper
from arrow import Arrow


class SimpleArrow(Arrow):
    def to_png(self):
        arrowhead_ratio = {
                           "small": 1,
                           "normal": 2,
                           "large": 3
                           }[self.marker]

        arrow = 5 * arrowhead_ratio

        image = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(image)

        end_x, end_y = self.end
        draw.line([self.start, self.end], width=self.thickness, fill=self.fill)
        draw.polygon([self.end, (end_x - arrow, end_y - arrow/2),
                      (end_x - arrow, end_y + arrow/2)], fill=self.fill,
                     outline=self.fill)
        return ImageWrapper(image, *self.size)
