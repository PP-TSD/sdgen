# -*- coding: utf-8 -*-
import Image
import ImageFont
import ImageDraw

from sdgen.config import config
from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.utils import helpers

from _field import Field


class Character(Field):
    render_config_key = "character"
    font_name = "Arial"
    font_size = 12
    font_typeface = "regular"
    font_color = "black"
    marked_font_color = "red"
    padding = 3
    background = "transparent"
    marked_background = "transparent"

    def __init__(self, text, *args, **kwargs):
        """Render text.

        Args:
            text (str): Text, which should be rendered.

        Kwargs:
            font_name (str): Name of font type, ex. 'arial'.
            font_size (float): Font size in points.
            font_typeface (str): Font typeface, ex. 'bold italic'.
            font_color (str): Font color.
            padding (float): text padding.
            background (str): Background color.
        """
        super(Character, self).__init__(*args, **kwargs)
        self.text = text

    def _get_font(self, font_type, size, typeface):
        """Get font with given parameters."""
        font_path = helpers.get_font_path(font_type, typeface)

        if font_path:
            return ImageFont.truetype(font_path, helpers.pt_to_px(size))
        return ImageFont.load_default()

    def to_png(self):
        padding = self.pt_to_px(self.padding)
        font = self._get_font(self.font_name, self.font_size, self.font_typeface)
        image_size = [x + 2 * padding for x in font.getsize(self.text)]
        background = (self.background if not self.background == "transparent"
                      else (0, 0, 0, 0))
        image = Image.new('RGBA', image_size, background)
        draw = ImageDraw.Draw(image)
        draw.text((padding,) * 2, self.text, font=font, fill=self.font_color)
        return ImageWrapper(image, *map(self.px_to_pt, image_size))

