# -*- coding: utf-8 -*-
from sdgen.fields import Rectangle
from sdgen.fields import Flattener
from connections.alternation_connection import AlternationConnection
from connections.connection import Connection
from _view import View


class Alternation(View):
    arrow_width = 50
    padding = 5
    left_padding = 0
    right_padding = 0
    subfields_padding = 12

    def add_children(self, children):
        assert children, "Alternation children lists shouldn't be empty"
        extended = []
        # dict for fast navigation over connections (linked with children)
        # each child should have "left" and "right" connection generated
        self.alternation_connections = {}

        for i in range(len(children)):
            if isinstance(children[i], Connection):
                # children list should be:
                # (child | connection,child,connection)+
                assert len(children) >= i + 2, "Inproper children list"
                assert not isinstance(children[i + 1], Connection), "Inproper children list"
                assert isinstance(children[i + 2], AlternationConnection), "Inproper children list"
                extended.extend(children[i:i + 2])
                child = children[i + 1]
                left = children[i],
                right = children[i + 2],
                i += 2
            else:
                left = self.get_field(AlternationConnection)
                right = self.get_field(AlternationConnection)
                child = children[i]

            extended.append(child)
            self.alternation_connections[child] = dict(left=left, right=right)

        super(Alternation, self).add_children(extended)

    def render(self):
        padding = self.padding
        arrow_width = self.arrow_width
        left_padding = self.left_padding
        right_padding = self.right_padding

        rendered_subfields = dict((subfield, self.render_subview(subfield)) for subfield in self.subfields)

        total_height = sum([c.get_height() for c in rendered_subfields.values()]) + padding * (len(self.subfields) - 1)
        total_width = max([c.get_width() for c in rendered_subfields.values()]) + 2 * self.subfields_padding

        # size of rectangle with arrows (without horizontal lines)
        left_box_size = arrow_width + left_padding, total_height
        right_box_size = arrow_width + right_padding, total_height

        # list with rendered children and their positions
        subimages = []

        # y position of each subfield
        top_offside = 0
        for subfield in self.subfields:
            rendered = rendered_subfields[subfield]
            # subfields with different width should have horizontal connections
            hline_length = (total_width - rendered.get_width()) / 2
            # join generated subfield to all subimages list
            subimages.append((rendered, (left_box_size[0] + hline_length, top_offside)))

            # set left arrow params (dependent of subfields)
            left_arrow = self.alternation_connections[subfield]['left']
            left_handlers = {
                'left': total_height/2,
                'right': top_offside + rendered.get_handlers()['left']
            }
            left_arrow.set_arrow_handlers(left_box_size, left_handlers,
                                          left_length=left_padding,
                                          right_length=hline_length)
            subimages.append((self.render_subview(left_arrow), (0, 0)))

            right_arrow = self.alternation_connections[subfield]['right']
            right_handlers = {
                'right': total_height/2,
                'left': top_offside + rendered.get_handlers()['right']
            }
            right_arrow.set_arrow_handlers(right_box_size, right_handlers,
                                          left_length=hline_length,
                                          right_length=right_padding)
            subimages.append((self.render_subview(right_arrow),
                              (total_width + left_box_size[0] - hline_length, 0)))
            top_offside += rendered.get_height() + padding

        background = self.render_image(Rectangle((total_width + 2 * arrow_width + left_padding + right_padding, total_height),
                        thickness=0))

        flattener = Flattener(background, subimages)

        return self.render_view(flattener)
