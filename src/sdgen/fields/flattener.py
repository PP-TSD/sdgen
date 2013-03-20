# -*- coding: utf-8 -*-
import Image
import ImageDraw

from _field import Field
from sdgen.utils.image_wrapper import ImageWrapper


class Flattener(Field):
    def __init__(self, background, images):
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

    def to_png(self):
        background_image = self.background.get_image()
        for image, position in self.images:
            background_image.paste(image.get_image(), position,
                                   image.get_image())
        self.background.set_image(background_image)
        return self.background
        