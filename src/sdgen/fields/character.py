# -*- coding: utf-8 -*-
import os

import Image
import ImageFont
import ImageDraw

from _field import Field
from sdgen.config import config


class Character(Field):
    def __init__(self, text, font_type='Arial', size=10, typeface='normal'):
        """Render text (without paddings).
    
        Args:
            text (str): Text, which should be rendered.
    
        Kwargs:
            font_type (str): Name of font type, ex. 'arial'.
            size (int): Font size in points.
            typeface (str): Font typeface, ex. 'bold italic'.
        """
        self.text = text
        self.font_type = font_type
        self.size = size
        self.typeface = typeface

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
        font = self._get_font(self.font_type, self.size, self.typeface)
        image_size = font.getsize(self.text)
        image = Image.new('RGBA', image_size)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), self.text, font=font)
        return image
