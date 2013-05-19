# -*- coding: utf-8 -*-
from sdgen.fields import Character
from sdgen.fields import Rectangle
from sdgen.fields import Flattener
from sequence import Sequence
from _view import View


class Group(View):
    """
    Group view.

    Contains header in top-left corner and children putted in sequence. Group
    is placed in rectangled border.

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
        # add all children to sequence (it is transparent for user)
        # and set this sequence as it's only child:
        sequence = Sequence(mark=self.marked, arrows_surround=True)
        sequence.add_children(children)
        super(Group, self).add_children([sequence])

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

        # default sizes if group doesn't have children (wait, what?)
        width = header.get_width() + 2 * border_size
        height = header.get_height() + 2 * border_size

        params = []

        if fields:
            # sequence is it's child
            sequence, = fields
            # width and height of image
            width = max(
                # compute width of all subfields (plus paddings and borders)
                sequence.get_width() + 2 * (padding + border_size),
                width
            )
            # take header_height, child height and paddings
            height = (header.get_height() + sequence.get_height() +
                2 * (padding + border_size))

            # position of sequence with children
            sequence_y = header.get_height() + padding + border_size
            sequence_x = border_size + padding

            params = [(sequence, (sequence_x, sequence_y))]

        # render background (rectangle with frame)
        background = self.render_image(self.get_field(Rectangle,
            (width, height), thickness=self.border_size, marked=False))

        # add frame and header to the top of fields layers
        params[0:0] = [(background, (0, 0)), (header, (border_size, ) * 2)]

        field = Flattener(params)

        # final render of this view
        return self.render_view(field)
