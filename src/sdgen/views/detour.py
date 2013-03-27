# -*- coding: utf-8 -*-
from _view import View
from connections.connection import Connection
from sdgen.fields.detour_arrow import DetourArrow
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.flattener import Flattener


class Detour(View):
    render_config_key = "detour"
    padding = 10
    thickness = 2

    def add_children(self, children):
        extended = []
        # TODO: replace hard-coded length with flexible one (dependent on character and so on)
        iterator = iter([Connection(render_config={'marker': None, 'length': 15}),  # left connection
                         View(),
                         Connection(render_config={'marker': None}),  # right connection
                         Connection()  # detour connection
                         ])

        for child in children:
            item = iterator.next()
            while not isinstance(child, item.__class__):
                extended.append(item)
                item = iterator.next()
            extended.append(child)
        for item in iterator:
            extended.append(item)

        super(Detour, self).add_children(extended)

    def render(self):
        left_arrow, subfield, right_arrow, detour_arrow = self.subfields
        left_arrow = self.render_subview(left_arrow)
        right_arrow = self.render_subview(right_arrow)
        subfield = self.render_subview(subfield)

        detour_arrow = self.render_image(DetourArrow(*map(self.px_to_pt, (subfield.get_width(),
                                                     subfield.get_handler('left'),
                                                     subfield.get_handler('right'))),
                                                     marked=detour_arrow.marked))
        padding = (detour_arrow.get_width() - subfield.get_width()) / 2

        left_arrow_y = subfield.get_handler('left') - left_arrow.get_handler('right') + padding
        right_arrow_y = subfield.get_handler('right') - left_arrow.get_handler('left') + padding

        background = self.render_image(Rectangle((subfield.get_width() + 2 * padding, subfield.get_height() + 2 * padding),
                                       thickness=0))
        flattener = Flattener(background, [(detour_arrow, (0, 0)),
                                             (left_arrow, (0, left_arrow_y)),
                                             (subfield, (padding,) * 2),
                                             (right_arrow, (subfield.get_width() + padding, right_arrow_y))])
        handlers = {
                    "left": subfield.get_handler('left') + padding,
                    "right": subfield.get_handler('right') + padding
                    }
        rendered_fields = self.render_view(flattener)
        rendered_fields[0].update_handlers(handlers)
        return rendered_fields
