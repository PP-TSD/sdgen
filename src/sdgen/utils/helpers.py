# -*- coding: utf-8 -*-


def relative(point, diff):
    x, y = point
    x_diff, y_diff = diff
    return x + x_diff, y + y_diff

def size_from_vector(vector):
    return map(abs, vector)
