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
    font_name = "Arial"
    font_size = 12
    font_typeface = "normal"
    font_color = "black"
    padding = 0
    background = "transparent"

    def __init__(self, text, *args, **kwargs):
        """Render text.

        Args:
            text (str): Text, which should be rendered.

        Kwargs:
            font_name (str): Name of font type, ex. 'arial'.
            font_size (int): Font size in points.
            font_typeface (str): Font typeface, ex. 'bold italic'.
            font_color (str): Font color.
            padding (int): text padding (in points).
            background (str): Background color.
        """
        super(Character, self).__init__(*args, **kwargs)
        self.text = text

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
        padding = self.pt_to_px(self.padding)
        font = self._get_font(self.font_name, self.font_size, self.font_typeface)
        image_size = [x + 2 * self.pt_to_px(self.padding)
                            for x in font.getsize(self.text)]
        background = (self.background if not self.background == "transparent"
                      else (0, 0, 0, 0))
        image = Image.new('RGBA', image_size, background)
        draw = ImageDraw.Draw(image)
        draw.text((padding,) * 2, self.text, font=font, fill=self.font_color)
        return ImageWrapper(image, *image_size)
