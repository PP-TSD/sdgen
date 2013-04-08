# -*- coding: utf-8 -*-
from sdgen.config import render_config, safeget

dpi = None
dpi_inv = None


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
        dpi = int(safeget(render_config, "render.dpi", 75)) / 75
    return int(points) * dpi


def px_to_pt(points):
    """
    Converts pixels to points.
    """
    global dpi_inv
    if not dpi_inv:
        dpi_inv = 75 / int(safeget(render_config, "render.dpi", 75))
    return float(points) * dpi_inv
