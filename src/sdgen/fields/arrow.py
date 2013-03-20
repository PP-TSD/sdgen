# -*- coding: utf-8 -*-

from _field import Field


class Arrow(Field):
    def __init__(self, size, thickness=1, marker="normal", fill="black"):
        """Base arrow class.
    
        Args:
            size (tuple): width, height of rectangle.
    
        Kwargs:
            thickness (int): thickness of arrow (in pixels).
            marker (str): size of arrowhead (normal|large|small)
            fill (str): color (default black).
        """
        size = size[0], size[1] + 10  #FIXME: marker size
        self.end = (max(size[0], 0), max(size[0], 0))
        self.start = (max(-size[0], 0), max(-size[1], 0))
        self.size = size
        self.thickness = thickness
        self.marker = marker
        self.fill = fill
