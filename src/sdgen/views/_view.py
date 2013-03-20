# -*- coding: utf-8 -*-


class View(object):
    """
    Base class for all fields in sdgen.
    """
    renderer = None

    def __init__(self, name=None, type=None, value=None, marked=False, *args, **kwargs):
        self.subfields = []
        self.name = name
        self.value = value
        self.marked = marked

    def add_child(self, child):
        self.subfields.append(child)

    def render(self):
        """
        Renders view with all subfields

        Returns:
            ImageWrapper object
        """
        raise NotImplementedError()

    def render_image(self, field):
        if self.renderer and hasattr(field, self.renderer):
            return getattr(field, self.renderer)()
        else:
            raise NotImplementedError('Renderer {function} is not supported\
                     for {field_name} field.'.format(function=self.renderer,
                                    field_name=field.__class__.__name__))
