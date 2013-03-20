# -*- coding: utf-8 -*-
import Image
import ImageDraw

from _field import Field
from sdgen.utils.image_wrapper import ImageWrapper


class Rectangle(Field):
    render_config_key = "rectangle"

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
        self.thickness = thickness or self.from_render_config("thickness") or 1
        self.fill = fill or self.from_render_config("fill") or "transparent"
        self.outline = outline or self.from_render_config("outline") or "black"

    def to_png(self):
        image = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(image)
        fill = self.fill if not self.fill=="transparent" else (0, 0, 0, 0)
        width, height = self.size

        draw.rectangle((0, 0, width - 1, height - 1),
                       fill=self.outline, outline=self.outline)
        draw.rectangle((0 + self.thickness, 0 + self.thickness,
                        width - 1 - self.thickness,
                        height - 1 - self.thickness),
                       fill=fill, outline=fill)
        return ImageWrapper(image, *self.size)
