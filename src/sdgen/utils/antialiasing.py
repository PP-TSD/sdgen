# -*- coding: utf-8 -*-
import Image
from sdgen.utils import helpers
ANTIALIASING = 4


def antialiasing(klass):
    if hasattr(klass, 'pt_to_px'):
        def pt_to_px(self, points):
            return int(ANTIALIASING * self._original_pt_to_px(points))
    
        klass._original_pt_to_px = klass.pt_to_px
        klass.pt_to_px = pt_to_px
    
    if hasattr(klass, 'px_to_pt'):    
        def px_to_pt(self, pixels):
            return self._original_px_to_pt(pixels) / ANTIALIASING
    
        klass._original_px_to_pt = klass.px_to_pt
        klass.px_to_pt = px_to_pt
    
    if hasattr(klass, 'to_png'):
        def to_png(self, *args, **kwargs):
            image_wrapper = self._original_to_png(*args, **kwargs)
            image = image_wrapper.get_image()
            new_width = helpers.pt_to_px(image_wrapper.get_width())
            new_height = helpers.pt_to_px(image_wrapper.get_height())
            image_wrapper.image = image.resize((new_width, new_height), Image.ANTIALIAS)
            #image_wrapper.scale_parameters(1.0/ANTIALIASING)
            return image_wrapper
    
        klass._original_to_png = klass.to_png
        klass.to_png = to_png
    return klass