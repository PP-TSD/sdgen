# -*- coding: utf-8 -*-
from _field import Field


class Arrow(Field):
    marker = "normal"
    thickness = 3
    fill = "black"
    marked_fill = "red"

    def __init__(self, *args, **kwargs):
        """Base arrow class.

        
        :param thickness: Thickness of arrow line (in points).
        :type thickness: float. 
        :param marker: Size of arrowhead (normal|large|small).
        :type marker: str.
        :param fill: Color (default black).
        :type fill: str.
        """
        super(Arrow, self).__init__(*args, **kwargs)
        marker_to_int = {
            "small": 2,
            "normal": 3,
            "large": 4
        }
        self.marker = marker_to_int.get(self.marker, 0) * self.thickness
