# -*- coding: utf-8 -*-
import Image
import ImageFont

from _field import Field


class Character(Field):
    """Character field.
    
    Render text.
    """
    def _get_font(self, font_type, typeface):
        """Get font with given parameters.
        """
        pass
    
    
    def to_png(self, text, font_type='Arial', size=10, typeface='normal'):
        """Render png image with text.
        
        Args:
            text (str): Text, which should be rendered.
            
        Kwargs:
            font_type (str): Name of font type, ex. 'arial'.
            size (int): Font size in points.
            typeface (str): Font typeface, ex. 'bold italic'.
        
        Returns:
            Image. Rendered image.
        """
        raise NotImplementedError()
