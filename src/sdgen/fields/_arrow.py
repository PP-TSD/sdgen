# -*- coding: utf-8 -*-
from _field import Field


class Arrow(Field):
    """Abstract arrow class."""
    marker = "normal"  #: size of arrowhead, default: "normal"
    thickness = 2.0  #: line thickness in points, default 3.0
    fill = "black"  #: arrow color, default: "black"
    marked_fill = "red"  #: marked arrow color, default: "red"

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
