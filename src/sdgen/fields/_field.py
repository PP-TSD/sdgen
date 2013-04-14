# -*- coding: utf-8 -*-
from sdgen._configurable_mixin import ConfigurableMixin
from sdgen.utils import helpers


class Field(ConfigurableMixin):
    """Abstract base *field* class.
    
    Each field represents simple or complex graphical element, for example:
    :class:`sdgen.fields.character.Character` or
    :class:`sdgen.fields.simple_arrow.SimpleArrow` described with set of
    params, like padding, width, font_size, etc.
    
    Fields are created by views (you can find them in :module:`sdgen.views`)
    with all needed parameters and then called to render by specific *Builder*.
    """
    marked = False

    def __init__(self, *args, **kwargs):
        """

        All frontend-configuration (such as font_color and so on) can be
        prefixed by marked_, which will be used when field/view is marked
        (marked=True).

        :param marked: True, if field should be marked.
        :type marked: bool. 
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
        """Render field in png
        
        This method should be overwritted in derived classes to render png
        image of field.
        """
        raise NotImplementedError()

    def to_svg(self):
        """Render field in svg.
        
        This method should be overwritted in derived classes to render svg
        image of field.
        """
        raise NotImplementedError()

    def pt_to_px(self, points):
        """Mapping :function:`pt_to_px` from :mod:`sdgen.lib.helpers`.
        
        Result of this method can be modified by setting antialiasing decorator
        on class.
        """
        return helpers.pt_to_px(points)

    def px_to_pt(self, points):
        """Mapping :function:`px_to_pt` from :mod:`sdgen.lib.helpers`.
        
        Result of this method can be modified by setting antialiasing decorator
        on class.
        """
        return helpers.px_to_pt(points)
