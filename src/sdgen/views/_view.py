# -*- coding: utf-8 -*-
from sdgen._configurable_mixin import ConfigurableMixin
from sdgen.utils import helpers


class View(ConfigurableMixin):
    """
    Abstract base class for all views in sdgen. Should NOT be used directly in
    input data.

    View is logical element. It can contains another views (view is treated as
    container) and should know, what fields (:class:`sdgen.fields._field.Field`)
    should be used to generate this view.

    Views are created by builder (:class:`sdgen.builder.Builder`) to match input
    data (input data view param usually match View subclasses names).

    All frontend-configuration (such as font_name and so on) can be prefixed
    by marked, which will be used when field/view is marked (marked=True).

    Default view configuration (can be used in all subclasses):

    .. attribute:: thickness : float

        Thickness of element (in points).
        Default: 3

    .. attribute:: padding : float

        Space between element border and content.
        Default: 10

    .. attribute:: font_name : str

        Font family name.
        Default: Arial

    .. attribute:: font_size : float

        Size of font (in points).
        Default: 12

    .. attribute:: font_typeface : str

        Font style.
        Default: regular
    """
    renderer = None  # Field function name called to render subfield image, for example 'to_png'
    save_as_subimage = False  # True if separate rendered image for view
    arrowhead = False  # True if view starts with arrow

    # default configuration
    thickness = 3
    padding = 10
    font_name = "Arial"
    font_size = 12
    font_typeface = "regular"
    marked_background = "yellow"
    marked_font_color = "red"

    def __init__(self, name=None, value=None, mark=False, *args, **kwargs):
        """
        Initializes View object.

        :param name: name of view
        :type name: str
        :param value: value of view, which should be rendered on image
        :type value: str
        :param mark: True or 'yes' if view (with all descendant views and
            fields) should be highlited
        :type mark: bool or str
        """
        super(View, self).__init__(*args, **kwargs)
        self.subfields = []
        self.rendered = []

        self.name = name
        self.value = value
        self.marked = True if mark in (True, 'yes') else False

    def add_child(self, child):
        """
        Add child (another view) to this view.

        :param child: view to add as a child
        :type child: `sdgen.views._views.View`
        """
        self.subfields.append(child)

    def add_children(self, children):
        """
        Extend list of subfields by passed list of children

        :param children: list of views to extend current children
        :type children: list
        """
        self.subfields.extend(children)

    def _pairs(self, list_):
        """
        Iterator for list, returning pair elements (i, i+1).
        None sentinel is returned for element before first and after last.

        :param list_: list to iterate
        :type list: list

        :returns: tuple of i and i+1 element from input list in each iteration
        :rtype: tuple
        """
        list_ = [None] + list_ + [None]
        i = iter(list_)
        prev = i.next()
        for item in i:
            yield prev, item
            prev = item

    def get_field(self, field, *args, **kwargs):
        """
        Proxy to get field from view.

        With this proxy, information about view marking is passed to field.

        :param field: field class
        :type field: `sdgen.fields._field.Field`

        :returns: field instance
        """
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

        By default, generates same image as render.
        """
        return self.render(*args, **kwargs)

    def render_subview(self, view):
        """
        Render subview and add it (and all views that should be saved) to
        rendered list.

        This method should be called to render all subviews of view!

        :param view: view to be rendered
        :type view: `sdgen.views._view.View`

        :returns: rendered view
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
        Renders view with all subfields. Should be overwritten in subclasses.

        :returns: `sdgen.utils.image_wrapper.ImageWrapper` object
        """
        raise NotImplementedError()

    def render_image(self, field):
        """
        Render image by calling renderer function from field.
        """
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
        """
        Converts points to pixels.

        .. deprecated:: 0.0.3
            Use :func:`helpers.pt_to_px` directly instead.
        """
        return helpers.pt_to_px(points)

    def px_to_pt(self, points):
        """
        Converts pixels to points.

        .. deprecated:: 0.0.3
            Use :func:`helpers.px_to_pt` directly instead.
        """
        return helpers.px_to_pt(points)
