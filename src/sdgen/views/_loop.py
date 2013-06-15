# -*- coding: utf-8 -*-
from sdgen.views._view import View
from sdgen.views.connections.connection import Connection
from sdgen.views.sequence import Sequence
from sdgen.fields.flattener import Flattener


class Loop(View):
    """
    Abstract loop container (left arrow, subfield, right arrow, loop-arrow).

    It uses framework design pattern class, each descendant have to implement:
    :func:`Loop.get_absolute_subfields_handlers`,
    :func:`Loop.get_arrow_position`,
    :func:`Loop.get_connection_class`,
    :func:`Loop.get_subfield_position`.
    Loop should have children in structure like:

    * Left arrow - :class:`sdgen.views.connections.connection.Connection`,
    * Subfield - :class:`sdgen.views._view.View`,
    * Right arrow - :class:`sdgen.views.connections.connection.Connection`,
    * Loop arrow - :class:`sdgen.views.connections._loop.LoopConnection`.

    Where each field (except subfield) is optional in input JSON and will be
    generated with default parameters if not given.

    .. attribute:: padding : float

        Space between loop-arrow and subfield.
        Default: 10

   .. attribute:: left_length : float

        Length of left arrow and left side of loop-arrow.
        Default: 15

   .. attribute:: rigth_length : float

        Length of right arrow and right side of loop-arrow.
        Default: 15
    """
    padding = 10
    left_length = 15
    right_length = 15
    # field starts with arrow
    arrowhead = True

    def get_absolute_subfields_handlers(self, subfield):
        """Return subfields handlers relative to result image.

        :param subfield: Rendered subfield.
        :type subfield: :class:`sdgen.utils.image_wrapper.ImageWrapper`
        :rtype: dict
        """
        raise NotImplementedError()

    def get_arrow_position(self, subfield):
        """Return position of loop arrow on result image.

        :param subfield: Rendered subfield.
        :type subfield: :class:`sdgen.utils.image_wrapper.ImageWrapper`
        :rtype: tuple
        """
        raise NotImplementedError()

    def get_connection_class(self):
        """Return class of loop-arrow view.

        :rtype: :class:`sdgen.views.connections._loop.LoopConnection`
        """
        raise NotImplementedError()

    def get_subfield_position(self, left_arrow_width):
        """Return subfield position on result image.

        :param left_arrow_width: Width of arrow in the left side of subfield.
        :type left_arrow_width: float
        :rtype: tuple
        """
        raise NotImplementedError()

    def add_children(self, children):
        extended = []
        connection_class = self.get_connection_class()

        # check if loop has only one child which is not Connection
        subviews = [v for v in children if not isinstance(v, Connection)]
        assert len(subviews) == 1, u'Loop-like field can have only one child (besides Connections)'

        # children schema. If child is not present in children it will be
        # rendered with default options.
        iterator = iter([Connection(length=self.left_length,
                                    mark=self.marked),  # left connection
                         View(mark=self.marked),
                         Connection(marker=None, length=self.right_length,
                                    mark=self.marked),  # right connection
                         connection_class(left_length = self.left_length,
                                          right_length = self.right_length,
                                          mark=self.marked)  # loop connection
                         ])
        # for each child defined in schema add it into extended list
        for child in children:
            item = iterator.next()
            while not isinstance(child, item.__class__):
                extended.append(item)
                item = iterator.next()
            extended.append(child)
        for item in iterator:
            extended.append(item)

        # trim sequence
        if isinstance(extended[1], Sequence):
            extended[1].trim_arrows()

        # generate headless arrow if subfield starts with arrow
        extended[0].sharp = not extended[1].arrowhead

        super(Loop, self).add_children(extended)

    def render(self):
        # render defined subfield
        left_arrow, subfield, right_arrow, loop_arrow = self.subfields
        left_arrow = self.render_subview(left_arrow)
        right_arrow = self.render_subview(right_arrow)
        subfield = self.render_subview(subfield)

        subfield_handlers = self.get_absolute_subfield_handlers(subfield)

        # Loop arrow could be rendered after subfield, cause it depends on
        # subfield's size. Set loop params and render it
        loop_arrow.set_subfield_params(subfield.get_size(), subfield_handlers)
        loop_arrow = self.render_subview(loop_arrow)

        # compute position of subimages
        subfield_position = self.get_subfield_position(left_arrow.get_width())
        left_arrow_y = (subfield_position[1] + subfield.get_handler('left') -
                        left_arrow.get_handler('right'))
        right_arrow_y = (subfield_position[1] + subfield.get_handler('right') -
                         right_arrow.get_handler('left'))

        # create container with subimages on their positions
        flattener = Flattener([
            (loop_arrow, self.get_arrow_position(subfield)),
            (left_arrow, (0, left_arrow_y)),
            (subfield, self.get_subfield_position(left_arrow.get_width())),
            (right_arrow, (subfield.get_width() + left_arrow.get_width(),
                           right_arrow_y))
        ])
        rendered_fields = self.render_view(flattener)

        # set handlers to begin of left arrow and end of right arrow
        handlers = {
            "left": left_arrow_y + left_arrow.get_handler("left"),
            "right": right_arrow_y + right_arrow.get_handler("right")
        }
        rendered_fields[0].update_handlers(handlers)

        return rendered_fields
