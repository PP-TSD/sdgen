# -*- coding: utf-8 -*-
import os
import sys

from ..builder import Builder
from ..views._view import View


class PNGBuilder(Builder):
    """
    PNG syntax diagrams generator.
    """
    def generate(self, data, input_path, output_dir, *args, **kwargs):
        """
        Generate png image with given data and configuration.

        Args:
            data:

        Kwargs:
            font_type (str): Name of font type, ex. 'arial'.
            size (int): Font size in points.
            typeface (str): Font typeface, ex. 'bold italic'.

        Returns:
            Image. Rendered image.
        """
        View.renderer = "to_png"

        image = super(PNGBuilder, self).generate(data, input_path, output_dir)
        # save as input file name with png extension
        output_file_tmpl = "{output_dir}{sep}{base_file}_{file_nr}.png"
        sep = os.path.sep
        base_file = os.path.splitext(os.path.basename(input_path))[0]

        # save all generated images
        for (file_nr, img) in enumerate(image):
            raw_image = img.get_image()
            output_file_path = output_file_tmpl.format(**locals())
            raw_image.save(output_file_path)
        return raw_image
