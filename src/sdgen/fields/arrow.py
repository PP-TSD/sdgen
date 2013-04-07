# -*- coding: utf-8 -*-
from sdgen.fields._field import Field


MARKER = 5  # detaults marker length (in points)


class Arrow(Field):
    thickness = 2
    marker = "normal"
    fill = "black"
    marked_fill = "red"

    def __init__(self, *args, **kwargs):
        """
        Base arrow class.

        Kwargs:
            thickness (int): thickness of arrow (in points).
            marker (str): size of arrowhead (normal|large|small).
            fill (str): color (default black).
        """
        super(Arrow, self).__init__(*args, **kwargs)
        marker_to_int = {
            "small": 1,
            "normal": 2,
            "large": 3
        }
        self.marker = marker_to_int.get(self.marker, 0) * MARKER
