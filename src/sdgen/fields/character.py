# -*- coding: utf-8 -*-
import os

import Image
import ImageFont
import ImageDraw

from _field import Field
from sdgen.config import config


class Character(Field):
    """Character field.

    Render text.
    """
    def _get_font(self, font_type, size, typeface):
        """Get font with given parameters.
        """
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

    def to_png(self, text, font_type='Arial', size=10, typeface='normal'):
        """Render png image with text (without paddings).

        Args:
            text (str): Text, which should be rendered.

        Kwargs:
            font_type (str): Name of font type, ex. 'arial'.
            size (int): Font size in points.
            typeface (str): Font typeface, ex. 'bold italic'.

        Returns:
            Image. Rendered image.
        """
        font = self._get_font(font_type, size, typeface)
        image_size = font.getsize(text)
        image = Image.new('RGBA', image_size)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font)
        return image
