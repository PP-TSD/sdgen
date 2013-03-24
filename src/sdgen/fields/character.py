# -*- coding: utf-8 -*-
import os

import Image
import ImageFont
import ImageDraw

from _field import Field
from sdgen.config import config
from sdgen.utils.image_wrapper import ImageWrapper


class Character(Field):
    render_config_key = "character"
    default_render_config = {
        "font.name": "Arial",
        "font.size": 12,
        "font.typeface": "normal",
        "font.color": "black",
        "background": "transparent"
    }

    def __init__(self, text, *args, **kwargs):
        """Render text (without paddings).

        Args:
            text (str): Text, which should be rendered.

        Kwargs:
            font_name (str): Name of font type, ex. 'arial'.
            font_size (int): Font size in points.
            font_typeface (str): Font typeface, ex. 'bold italic'.
            font_color (str): Font color.
            background (str): Background color.
        """
        super(Character, self).__init__(*args, **kwargs)
        self.text = text
        # self.font_type = font_type or self.from_render_config("font.name") or "Arial"
        # self.size = size or self.from_render_config("font.size") or 12
        # self.typeface = typeface or self.from_render_config("font.typeface") or "normal"
        # self.color = color or self.from_render_config("font.color") or "black"
        # self.background = background or self.from_render_config("background") or "transparent"

    def _get_font(self, font_type, size, typeface):
        """Get font with given parameters."""
        font_type = font_type.lower()
        for directory in config.get('fonts', 'directories').split():
            for (dirpath, dirnames, filenames) in os.walk(directory):
                files = [name for name in filenames
                         if font_type in name.lower()]
                #TODO: bold, italic, normal
                if files:
                    path = os.path.join(dirpath,
                                        dirnames[0] if dirnames else '',
                                        files[0])
                    return ImageFont.truetype(path, size)
        return ImageFont.load_default()

    def to_png(self):
        font = self._get_font(self.font_name, self.font_size, self.font_typeface)
        image_size = font.getsize(self.text)
        background = (self.background if not self.background == "transparent"
                      else (0, 0, 0, 0))
        image = Image.new('RGBA', image_size, background)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), self.text, font=font, fill=self.font_color)
        return ImageWrapper(image, *image_size)
