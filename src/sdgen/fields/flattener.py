# -*- coding: utf-8 -*-
import Image
import ImageDraw

from _field import Field
from sdgen.utils.image_wrapper import ImageWrapper


class Flattener(Field):
    def __init__(self, background, images, padding=0):
        """Merge list of images.
    
        Insert i-th image into (i-1)-th on specified position,
        i = n, n-1, ..., 0.
        This field is usefull for views to join Images (packed in ImageWrapper)

        Args:
            background (ImageWrapper): base layer.
            images (tuple): (ImageWrapper, (x, y)) image and it's position
                relative to the background.
        """
        self.background = background
        self.images = images
        self.padding = padding

    def to_png(self):
        
        def paste_pixels(pixel1, pixel2):
            """ paste pixel2 on pixel1 """
            r1, g1, b1, a1 = pixel1
            r2, g2, b2, a2 = pixel2
            if a1 and a2:
                sub_merge = lambda x1, x2: x1 + (x2 - x1) * a2 / 255
                r3 = sub_merge(r1, r2)
                g3 = sub_merge(g1, g2)
                b3 = sub_merge(b1, b2)
                a3 = max(a1, a2)
                return r3, g3, b3, a3
            else:
                if not a1:
                    return pixel2
                else:
                    return pixel1
                    
        
        def transparent_paste(background, image, position):
            width, height = image.size
            for x in range(width):
                for y in range(height):
                    pixel = image.getpixel((x, y))
                    background_position = position[0] + x, position[1] + y
                    try:
                        background_pixel = background.getpixel(background_position)
                        background.putpixel(background_position,
                                        paste_pixels(background_pixel, pixel))
                    except IndexError:
                        # end of background image
                        break
        
        background_image = self.background.get_image()
        for image, position in self.images:
            transparent_paste(background_image, image.get_image(), position)
        self.background.set_image(background_image)
        return self.background
        