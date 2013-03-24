# -*- coding: utf-8 -*-

from _field import Field


MARKER = 5  # detaults marker length (in points)

class Arrow(Field):
    def __init__(self, thickness=1, marker="normal", fill="black"):
        """Base arrow class.

        Kwargs:
            thickness (int): thickness of arrow (in points).
            marker (str): size of arrowhead (normal|large|small)
            fill (str): color (default black).
        """
        self.thickness = thickness
        self.marker = {
                       None: None,
                       "small": 1,
                       "normal": 2,
                       "large": 3
                      }[marker] * MARKER
        self.fill = fill
