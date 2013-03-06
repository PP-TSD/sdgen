# -*- coding: utf-8 -*-
from PIL import ImageDraw

def rectangle(input, box, fill):
    """
    Draws rectangle with specified properties.

    :param input: input image to draw on
    :type name: PIL.Image
    :param box: rectangle coordinates. First two are top-left, second two
        are bottom-right
    :type state: tuple
    :param fill: fill color
    :type state: str
    """
    draw = ImageDraw.Draw(input)
    draw.rectangle(box, fill=fill) # The outer rectangle


def arrow(*args, **kwargs):
    pass


def circle(*args, **kwargs):
    pass

# to be continued
