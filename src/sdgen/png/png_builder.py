# -*- coding: utf-8 -*-
import os

import Image

from sdgen.builder import Builder
from sdgen.views._view import View
from sdgen.config import render_config, safeget


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

        default_png_config = {
            'dpi': 120
        }
        png_config = safeget(render_config, "png", default_png_config)
        render_config["render"] = png_config

        image = super(PNGBuilder, self).generate(data, input_path, output_dir)

        result = []
        output_file_path = ""

        # save all generated images
        for (file_nr, img) in enumerate(image):
            img_name, raw_image = img.get_image_with_name()

            # dpi
            dpi = png_config.get("dpi")
            if dpi:
                dpi = int(dpi)
                raw_image.info["dpi"] = (dpi, dpi)

            # scale
            ratio = png_config.get("scale")
            if ratio:
                ratio = float(ratio)
                assert 0 < ratio <= 1
                if ratio != 1:
                    new_dimensions = tuple([int(x * ratio) for x in raw_image.size])
                    raw_image = raw_image.resize(new_dimensions, Image.ANTIALIAS)

            if output_dir and img_name:
                file_name = img_name.lower().replace(' ', '_') + '.png'
                output_file_path = os.path.join(output_dir, file_name)
                raw_image.save(output_file_path)

            result.append((img_name, raw_image))
        return result
