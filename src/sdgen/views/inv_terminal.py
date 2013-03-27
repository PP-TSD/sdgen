
# -*- coding: utf-8 -*-
from ._view import View
from .terminal import Terminal
from .inv_terminal_child import InvTerminalChild
from ..fields.rounded_rectangle import RoundedRectangle
from ..fields.flattener import Flattener


class InvTerminal(View):
    padding = 10

    def add_children(self, children):
        """
        Replace all Terminal children instances to InvTerminalChild instances
        with same config.
        """
        replaced_children = []
        for child in children:
            assert isinstance(child, Terminal)
            inv_terminal_child = InvTerminalChild(name=child.name,
                                                  type=child.type,
                                                  value=child.value,
                                                  mark=child.marked,
                                                  **child._passed_config)
            replaced_children.append(inv_terminal_child)
        super(InvTerminal, self).add_children(replaced_children)

    def render(self):
        padding = self.pt_to_px(self.padding)
        fields = map(self.render_subview, self.subfields)

        top_max_height = max([max(x.get_handlers().values()) for x in fields])

        width = sum(map(lambda f: f.get_width(), fields)) + 2 * padding
        height = max(map(lambda f: f.get_height(), fields)) + 2 * padding

        background = self.render_image(RoundedRectangle((width, height), fill="black"))

        def next_field():
            x = 0
            assert fields, "Empty group"
            # previous field can have not inline handlers (eg. _[]- )
            # it must be corrected in this field
            diff = fields[0].get_handler('right') - fields[0].get_handler('left')
            for field in fields:
                yield field, (x, diff + top_max_height - field.get_handler('left'))
                diff += field.get_handler('right') - field.get_handler('left')
                x += field.get_width()
        positioned_fields = list(next_field())

        field = Flattener(background, positioned_fields)
        return self.render_view(field)
