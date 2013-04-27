# -*- coding: utf-8 -*-
from _field import Field
from rectangle import Rectangle


class Flattener(Field):
    def __init__(self, images, **kwargs):
        """Merge list of images.
    
        Insert i-th image on (i-1)-th on specified position,
        i = n, n-1, ..., 0.
        This field is usefull for views to join Images (packed in ImageWrapper)

        Args:
            images (tuple): (ImageWrapper, (x, y)) image and it's position
                relative to the background.
        """
        super(Flattener, self).__init__(**kwargs)
        self.images = images
        
        max_width = max([image.get_width() + width for image, (width, height) in images])
        max_height = max([image.get_height() + height for image, (width, height) in images])
        
        self.background = Rectangle((max_width, max_height),
                                    thickness=kwargs.get('thickness', 0))
 
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
        
        background = self.background.to_png()
        background_image = background.get_image()
        for image, position in self.images:
            transparent_paste(background_image, image.get_image(), map(self.pt_to_px, position))
        background.set_image(background_image)
        return background
        