# -*- coding: utf-8 -*-
from sdgen._configurable_mixin import ConfigurableMixin


class Field(ConfigurableMixin):
    marked = False

    def __init__(self, *args, **kwargs):
        """
        Base field class.

        All frontend-configuration (such as font_color and so on) can be prefixed
        by marked_, which will be used when field/view is marked (marked=True)

        Kwargs:
            marked (boolean): True, if field should be marked
        """
        super(Field, self).__init__(*args, **kwargs)

    def __getattribute__(self, attrname):
        """
        When self.marked is set to True, then try to return self.marked_{name}
        if setted, else returns value assigned to passed attribute name
        """
        if attrname not in ['marked']:
            marked_name = "_".join(("marked", attrname))
            if getattr(self, "marked", False) and hasattr(self, marked_name):
                return object.__getattribute__(self, marked_name)
        return object.__getattribute__(self, attrname)

    def to_png(self):
        """
        This method should be overwritted in derived classes to render png image
        of field.
        """
        raise NotImplementedError()

    def to_svg(self):
        """
        This method should be overwritted in derived classes to render svg image
        of field.
        """
        raise NotImplementedError()

    def pt_to_px(self, points):
        """
        Converts points to pixels.
        """
        return int(points)

    def px_to_pt(self, points):
        """
        Converts pixels to points.
        """
        return float(points)
