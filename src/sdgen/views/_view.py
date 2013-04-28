# -*- coding: utf-8 -*-
from sdgen._configurable_mixin import ConfigurableMixin
from sdgen.utils import helpers


class View(ConfigurableMixin):
    """
    Base class for all fields in sdgen.
    """
    renderer = None
    save_as_subimage = False  # True if separate rendered image for view
    arrowhead = False  # True if view starts with arrow

    def __init__(self, name=None, type_=None, value=None, mark=False, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.subfields = []
        self.rendered = []
        self.name = name
        self.value = value
        if value:
            self.value = self.value.decode('utf-8')
        self.type = type_
        self.marked = True if mark in (True, 'yes') else False

    def add_child(self, child):
        self.subfields.append(child)

    def add_children(self, children):
        self.subfields.extend(children)

    def _pairs(self, list_):
        """
        Iterator for list, returning pair elements (i, i+1).
        None sentinel is returned for element before first and after last.
        """
        list_ = list_ + [None]
        i = iter(list_)
        prev = i.next()
        for item in i:
            yield prev, item
            prev = item

    def get_field(self, field, *args, **kwargs):
        if 'marked' not in kwargs:
            kwargs['marked'] = self.marked
        render_config_key = self._render_config_key
        if 'render_config_key' in kwargs:
            render_config_key = kwargs['render_config_key']
            del kwargs['render_config_key']
        return field(render_config_key=render_config_key, *args, **kwargs)

    def render_subimage(self, *args, **kwargs):
        """
        Called when view has save_as_subimage == True

        By default, generates same image as render
        """
        return self.render(*args, **kwargs)

    def render_subview(self, view):
        """
        Render subview and add it (and all views that should be saved) to
        rendered list.

        This method should be called to render all subviews of view!
        """
        rendered = view.render()
        # add rendered view to rendered list
        if view.save_as_subimage:
            self.rendered.extend(view.render_subimage())
        # extend rendered list by generated earlier views that should be saved
        self.rendered.extend(rendered[1:])
        return rendered[0]

    def render(self):
        """
        Renders view with all subfields

        Returns:
            ImageWrapper object
        """
        raise NotImplementedError()

    def render_image(self, field):
        if self.renderer and hasattr(field, self.renderer):
            img = getattr(field, self.renderer)()
            img.name = self.name
            return img
        else:
            raise NotImplementedError('Renderer {function} is not supported\
                     for {field_name} field.'.format(function=self.renderer,
                                    field_name=field.__class__.__name__))

    def render_view(self, view):
        """
        Renders view and returns rendered view with all rendered subviews,
        which was created during rendering of this view.

        This method should be called at the end of view rendering to return
        final rendered view and all subviews that should be saved.
        """
        return [self.render_image(view)] + self.rendered

    def pt_to_px(self, points):
        return helpers.pt_to_px(points)

    def px_to_pt(self, points):
        return helpers.px_to_pt(points)
