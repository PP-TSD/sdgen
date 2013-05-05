# -*- coding: utf-8 -*-
from sdgen.fields import Character
from sdgen.fields import Rectangle
from sdgen.fields import Flattener
from connections import Connection
from sequence import Sequence
from _view import View


class Group(View):
    """
    Group view.

    Contains header in top-left corner and children putted in sequence. Group is
    placed in rectangled border.

    .. attribute:: padding : float

        Space between element border and content (in points).
        Default: 10

    .. attribute:: arrow_height : float

        Thickness of sequence arrow (in points).
        Default: 1

    .. attribute:: arrow_width : float

        Arrow width (in points).
        Default: 10

    .. attribute:: border_size : float

        Thickness of border (in points).
        Default: 1

    .. attribute:: header_padding : float

        Space between header border and it's content (in points).
        Default: 10

    .. attribute:: header_font_color : str

        Font color of header content.
        Default: white

    .. attribute:: header_background : str

        Background color of header.
        Default: black

    .. attribute:: header_font_typeface : str

        Header font style.
        Default: bold italic

    .. attribute:: header_font_type : str

        Header font family.
        Default: Arial

    .. attribute:: header_font_size : float

        Header font size (in points).
        Default: 14
    """

    padding = 10
    header_padding = 10
    header_font_color = "white"
    header_background = "black"
    header_font_typeface = "bold italic"
    header_font_type = "Arial"
    header_font_size = 14
    arrow_height = 1
    arrow_width = 10
    border_size = 1

    def add_children(self, children):
        extended_children = []
        if children:
            #first connection
            if isinstance(children[0], Connection):
                children[0].sharp = not children[1].arrowhead if len(children) > 1 and children[1] else True
                extended_children.append(children[0])
                children = children[1:]
            else:
                extended_children.append(Connection(mark=self.marked, sharp=not children[0].arrowhead))
            #last connection
            if children:
                if isinstance(children[-1], Connection):
                    extended_children.append(children[-1])
                    children = children[:-1]
                else:
                    extended_children.append(Connection(mark=self.marked))
            sequence = Sequence(mark=self.marked)
            sequence.add_children(children)
            extended_children.insert(1, sequence)
        super(Group, self).add_children(extended_children)

    def render(self):
        # render ImageWrappers of fields
        padding = self.padding
        width = 0
        height = 0

        # render all subviews and save this one, that should be saved to files
        fields = map(self.render_subview, self.subfields)
        border_size = self.border_size

        # black rect with title
        header = self.render_image(self.get_field(Character, self.name,
            render_config_key='header', font_color=self.header_font_color,
            background=self.header_background, padding=self.header_padding,
            font_typeface=self.header_font_typeface,
            font_size=self.header_font_size, font_type=self.header_font_type,
            marked=False))

        params = []

        if fields:
            left_arrow, sequence, right_arrow = fields
            # width and height of image
            width = max(sum(map(lambda f: f.get_width(), fields)) + 2 * (padding + border_size), header.get_width())
            height = header.get_height() + sequence.get_height() + 2 * (padding + border_size)

            # position of box with children and children
            subfields_y = header.get_height() + padding + border_size
            left_arrow_x = border_size + padding
            left_arrow_y = subfields_y + sequence.get_handler('left') - left_arrow.get_handler('right')
            sequence_x = left_arrow_x + left_arrow.get_width()
            right_arrow_x = sequence_x + sequence.get_width()
            right_arrow_y = subfields_y + sequence.get_handler('right') - right_arrow.get_handler('left')

            params.extend([(left_arrow, (left_arrow_x, left_arrow_y)),
                           (sequence, (sequence_x, subfields_y)),
                           (right_arrow, (right_arrow_x, right_arrow_y))])

        background = self.render_image(self.get_field(Rectangle, (width, height), thickness=self.border_size, marked=False))
        params[0:0] = [(background, (0, 0)), (header, (border_size, ) * 2)]

        field = Flattener(params)

        # final render of this view
        return self.render_view(field)
