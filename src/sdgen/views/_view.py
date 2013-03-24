# -*- coding: utf-8 -*-
from sdgen._configurable_mixin import ConfigurableMixin


class View(ConfigurableMixin):
    """
    Base class for all fields in sdgen.
    """
    renderer = None

    def __init__(self, name=None, type=None, value=None, marked=False, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.subfields = []
        self.name = name
        self.value = value
        self.marked = marked

    def add_child(self, child):
        self.subfields.append(child)

    def add_children(self, children):
        self.subfields.extend(children)

    def _pairs(self, list_):
        """
        Iterator for list, returning pair elements (i, i+1).
        None sentinel is returned for element before first and after last.
        """
        list_ = [None] + list_ + [None]
        i = iter(list_)
        prev = i.next()
        for item in i:
            yield prev, item
            prev = item

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
