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
        self.size = [max(size[0], -size[0], 1), max(size[1], -size[1], 1)]
        self.end = [max(size[0], 1), max(size[1], 1)]
        self.start = [max(-size[0], 1), max(-size[1], 1)]
        self.thickness = thickness
        self.marker = marker
        self.fill = fill
