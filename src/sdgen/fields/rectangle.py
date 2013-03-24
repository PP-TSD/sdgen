# -*- coding: utf-8 -*-
import Image
import ImageDraw

from _field import Field
from sdgen.utils.image_wrapper import ImageWrapper


class Rectangle(Field):
    render_config_key = "rectangle"
    default_render_config = {
        "thickness": 1,
        "fill": "transparent",
        "outline": "black"
    }

    def __init__(self, size, thickness=None, fill=None, outline=None, *args, **kwargs):
        """Render rectangle.

        Args:
            size (tuple): width, height of rectangle.

        Kwargs:
            thickness (int): thickness of rectangle (in pixels).
            fill (str): filling color (default transparent).
            outline (str): outline color (default black).
        """
        super(Rectangle, self).__init__(*args, **kwargs)
        self.size = size

    def to_png(self):
        image = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(image)
        fill = self.fill if not self.fill=="transparent" else (0, 0, 0, 0)
        width, height = self.size
        thickness = self.pt_to_px(self.thickness)

        draw.rectangle((0, 0, width - 1, height - 1),
                       fill=self.outline, outline=self.outline)
        draw.rectangle((0 + thickness, 0 + thickness,
                        width - 1 - thickness,
                        height - 1 - thickness),
                       fill=fill, outline=fill)
        return ImageWrapper(image, *self.size)
