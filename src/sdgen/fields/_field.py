# -*- coding: utf-8 -*-
from sdgen._configurable_mixin import ConfigurableMixin


class Field(ConfigurableMixin):
    """ Base field class. """

    def __init__(self, *args, **kwargs):
        super(Field, self).__init__(*args, **kwargs)
        if not hasattr(self, 'marked'):
            self.marked = kwargs.get('marked', False)

    def __getattribute__(self, attrname):
        """
        When self.marked is set to True, the try to return self.marked_{name}
        if setted, else returns value assigned to passed attribute name
        """
        if attrname not in ['marked']:
            marked_name = "_".join(("marked", attrname))
            if getattr(self, "marked", False) and hasattr(self, marked_name):
                return object.__getattribute__(self, marked_name)
        return object.__getattribute__(self, attrname)

    def to_png(self):
        raise NotImplementedError()

    def to_svg(self):
        raise NotImplementedError()

    def pt_to_px(self, points):
        return int(points)

    def px_to_pt(self, points):
        return float(points)
