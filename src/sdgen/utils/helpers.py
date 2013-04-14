# -*- coding: utf-8 -*-
import itertools
import os

import ImageFont

from sdgen.config import config, render_config, safeget

dpi = None
dpi_inv = None
fonts_paths = {}


def relative(point, diff):
    x, y = point
    x_diff, y_diff = diff
    return x + x_diff, y + y_diff


def size_from_vector(vector):
    return map(abs, vector)


def pt_to_px(points):
    """
    Converts points to pixels.
    """
    global dpi
    if not dpi:
        dpi = int(safeget(render_config, "render.dpi", 75)) / 75.0
    return int(points * dpi)


def px_to_pt(points):
    """
    Converts pixels to points.
    """
    global dpi_inv
    if not dpi_inv:
        dpi_inv = 75.0 / int(safeget(render_config, "render.dpi", 75))
    return float(points) * dpi_inv


def get_font_path(font_name, style="Regular"):
    """
    Search for passed font in directories from config

    If style has more than one word, it can be passed with any order.
    """
    global fonts_paths

    lower_font_name = font_name.strip().lower().replace(' ', '')
    lower_style = style.lower().strip()
    # possible style names (lowercased and un-spaced)
    lower_styles = sorted(["".join(s) for s in itertools.permutations(lower_style.split())])

    # font id, consisted of lower font name and sorted (by splitted name) lower font style
    font_id = (lower_font_name, lower_styles[0])

    # check for patch in "cache"
    if font_id in fonts_paths:
        return fonts_paths[font_id]

    # check for fonts, that has font_name (lowercased) in filename (lowercased)
    paths = []
    for directory in config.get('fonts', 'directories').split():
        for (dirpath, dirnames, filenames) in os.walk(directory):
            files = filter(lambda filename: lower_font_name in filename.lower(), filenames)
            paths.extend([os.path.join(dirpath, dirnames[0] if dirnames else '', file_) for file_ in files])

    # load candidate fonts and check if it's name and style match
    paths = list(set(paths))  # unique
    proper_path = None
    for font_path in paths:
        # load font
        f = ImageFont.truetype(font_path, 10)  # size can be any

        # lowercase and un-space font name and style
        imgfont_family = f.font.family.lower().replace(' ', '')
        imgfont_style = f.font.style.lower().replace(' ', '')

        # check for match
        if imgfont_family == lower_font_name and imgfont_style in lower_styles:
            proper_path = font_path
            break

    # save font path in cache
    fonts_paths[font_id] = proper_path
    return proper_path
