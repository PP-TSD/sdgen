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
        width, height = self.size
        if width < arrow:
            width = arrow
            self.end[0] += width
            self.size[0] += width
        
        if height < arrow:
            height = arrow
            self.start[1] += arrow/2
            self.end[1] += arrow/2
            self.size[1] += arrow

        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)

        end_x, end_y = self.end
        draw.line(tuple(self.start + self.end), width=self.thickness, fill=self.fill)
        draw.polygon([tuple(self.end), (end_x - arrow, end_y - arrow/3),
                     (end_x - arrow, end_y + arrow/3)], fill=self.fill,
                     outline=self.fill)
        return ImageWrapper(image, *self.size)
