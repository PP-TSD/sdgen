# -*- coding: utf-8 -*-
from sdgen.fields import SimpleArrow
from sdgen.views._view import View


class Connection(View):
    """
    Base connection, rendered as an arrow.

    .. attribute:: thickness : float

        Thickness of an arrow.
        Default: 3

    .. attribute:: marker : str

        Arrowhead size. Possible options are: small, normal, large.
        Default: normal.

    .. attribute:: length : str

        Length of an arrow.
        Default: 15

    .. attribute:: sharp : bool

        True if arrow should has sharp arrowhead.
        Default: True
    """
    thickness = 3
    marker = "normal"
    length = 15
    sharp = True

    def render(self):
        return self.render_view(self.get_field(SimpleArrow, marker=self.marker, length=self.length, marked=self.marked, sharp=self.sharp))
