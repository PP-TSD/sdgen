# -*- coding: utf-8 -*-
from _view import View
from connections.connection import Connection
from sdgen.views.connections.detour_connection import DetourConnection
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.flattener import Flattener
from sdgen.utils.antialiasing import antialiasing


class Detour(View):
    padding = 8
    thickness = 2

    def add_children(self, children):
        extended = []
        iterator = iter([Connection(render_config={'length': 2 * self.padding}),  # left connection
                         View(),
                         Connection(render_config={'marker': None, 'length': 2 * self.padding}),  # right connection
                         DetourConnection(left_length = 2 * self.padding, right_length = 2 * self.padding)  # detour connection
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

        detour_arrow.set_subfield_params(subfield.get_size(),
            {
                # in pixels
                "left": subfield.get_height() - subfield.get_handler('left'),
                "right": subfield.get_height() - subfield.get_handler('right')
            })
        detour_arrow = self.render_subview(detour_arrow)

        padding = (detour_arrow.get_width() - subfield.get_width()) / 2

        left_arrow_y = subfield.get_handler('left') - left_arrow.get_handler('right')
        right_arrow_y = subfield.get_handler('right') - right_arrow.get_handler('left')

        background = self.render_image(Rectangle((detour_arrow.get_width(), detour_arrow.get_height() + max(subfield.get_handlers().values())),
                                       thickness=0))

        flattener = Flattener(background, [(detour_arrow, (0, subfield.get_handler('left'))),
                                             (left_arrow, (0, left_arrow_y)),
                                             (subfield, (padding, 0)),
                                             (right_arrow, (subfield.get_width() + padding, right_arrow_y))])
        handlers = {
                    "left": subfield.get_handler('left'),
                    "right": subfield.get_handler('right')
                    }
        rendered_fields = self.render_view(flattener)
        rendered_fields[0].update_handlers(handlers)
        return rendered_fields
