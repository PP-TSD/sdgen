# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.image_wrapper import ImageWrapper
from arrow import Arrow

class DetourArrow(Arrow):
    render_config_key = "detour"
    padding = 2

    def __init__(self, width, left_height, right_height, *args, **kwargs):
        super(DetourArrow, self).__init__(*args, **kwargs)
        self.width = width  # in px
        self.left_height = left_height  # in px
        self.right_height = right_height  # in px
        self.height = max(left_height, right_height)

    def to_png(self):
        padding = self.pt_to_px(self.padding)
        width, height = self.width + 4 * padding, self.height + 2 * padding
        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)
        draw.line((padding, padding * 2, padding, self.left_height + padding), width=self.pt_to_px(self.thickness), fill=self.fill)
        draw.line((width - padding, padding * 2, width - padding, self.right_height + padding), width=self.pt_to_px(self.thickness), fill=self.fill)
        draw.line((padding * 2, padding, width - padding * 2, padding), width=self.pt_to_px(self.thickness), fill=self.fill)

        #TODO:  thickness
        draw.pieslice((-padding, self.left_height, padding,
                       self.left_height + padding * 2), 0, 90,
                      outline=self.fill)
        draw.pieslice((padding, padding, padding * 3,
                       padding * 3), 180, 270, outline=self.fill)
        draw.pieslice((width - padding * 3, padding, width - padding,
                       padding * 3), 270, 0, outline=self.fill)
        draw.pieslice((width - padding, self.right_height, width + padding,
                       self.right_height + padding * 2), 90, 180,
                      outline=self.fill)
        return ImageWrapper(image, width, height)