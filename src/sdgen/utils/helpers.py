# -*- coding: utf-8 -*-


def relative(point, diff):
    x, y = point
    x_diff, y_diff = diff
    return x + x_diff, y + y_diff
