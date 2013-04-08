# -*- coding: utf-8 -*-
from sdgen.views._view import View
from sdgen.views.connections.connection import Connection
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.flattener import Flattener


class Loop(View):
    padding = 10
    thickness = 2

    def get_connection_class(self):
        raise NotImplementedError()

    def get_handlers_relative_to_subfield(self, subfield, padding):
        raise NotImplementedError()

    def get_arrow_position(self, handlers):
        raise NotImplementedError()

    def get_subfield_position(self, left_arrow_width, padding):
        raise NotImplementedError()

    def add_children(self, children):
        extended = []
        connection_class = self.get_connection_class()
        iterator = iter([Connection(render_config={'length': 3 * self.padding}, mark=self.marked),  # left connection
                         View(mark=self.marked),
                         Connection(render_config={'marker': None, 'length': 3 * self.padding}, mark=self.marked),  # right connection
                         connection_class(left_length = 3 * self.padding, right_length = 3 * self.padding, mark=self.marked)  # loop connection
                         ])

        for child in children:
            item = iterator.next()
            while not isinstance(child, item.__class__):
                extended.append(item)
                item = iterator.next()
            extended.append(child)
        for item in iterator:
            extended.append(item)

        super(Loop, self).add_children(extended)

    def render(self):
        left_arrow, subfield, right_arrow, loop_arrow = self.subfields
        left_arrow = self.render_subview(left_arrow)
        right_arrow = self.render_subview(right_arrow)
        subfield = self.render_subview(subfield)

        relative_handlers = self.get_handlers_relative_to_subfield(subfield, self.pt_to_px(self.padding))

        loop_arrow.set_subfield_params(subfield.get_size(),
           relative_handlers)
        loop_arrow = self.render_subview(loop_arrow)

        padding = self.pt_to_px(self.padding)

        left_arrow_y = self.get_subfield_position(left_arrow.get_width(), padding)[1] + subfield.get_handler('left') - left_arrow.get_handler('right')
        right_arrow_y = self.get_subfield_position(left_arrow.get_width(), padding)[1] + subfield.get_handler('right') - right_arrow.get_handler('left')

        background = self.render_image(Rectangle((loop_arrow.get_width(),
                subfield.get_height() + 2 * padding), thickness=0))

        flattener = Flattener(background, [(loop_arrow, self.get_arrow_position(subfield)),
                                             (left_arrow, (0, left_arrow_y)),
                                             (subfield, self.get_subfield_position(left_arrow.get_width(), padding)),
                                             (right_arrow, (subfield.get_width() + left_arrow.get_width(), right_arrow_y))])
        handlers = {
                    "left": self.get_subfield_position(left_arrow.get_width(), padding)[1] + subfield.get_handler('left'),
                    "right": self.get_subfield_position(left_arrow.get_width(), padding)[1] + subfield.get_handler('right')
                    }
        rendered_fields = self.render_view(flattener)
        rendered_fields[0].update_handlers(handlers)
        return rendered_fields
