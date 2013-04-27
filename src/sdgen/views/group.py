# -*- coding: utf-8 -*-
from sdgen.fields import Character
from sdgen.fields import Rectangle
from sdgen.fields import Flattener
from connections import Connection
from sequence import Sequence
from _view import View


class Group(View):
    padding = 10
    header_padding = 5
    arrow_height = 1
    arrow_width = 10
    border_size = 1

    def add_children(self, children):
        extended_children = []
        if children:
            #first connection
            if isinstance(children[0], Connection):
                extended_children.append(children[0])
                children = children[1:]
            else:
                extended_children.append(Connection(mark=self.marked))
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

        # render all subviews and save this one, that should be saved to files
        fields = map(self.render_subview, self.subfields)
        border_size = self.border_size

        # black rect with title
        header = self.render_image(self.get_field(Character, self.name, render_config_key='header', font_color="white", background="black", padding=self.header_padding, marked=False))

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

        background = self.render_image(self.get_field(Rectangle, (width, height), thickness=self.border_size, marked=False))
        field = Flattener([(background, (0,0)),
                    (header, (border_size, ) * 2),
                    (left_arrow, (left_arrow_x, left_arrow_y)),
                    (sequence, (sequence_x, subfields_y)),
                    (right_arrow, (right_arrow_x, right_arrow_y))])

        # final render of this view
        return self.render_view(field)
