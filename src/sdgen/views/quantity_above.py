# -*- coding: utf-8 -*-
from sdgen.fields import Character
from sdgen.fields import Flattener
from _view import View


class QuantityAbove(View):
    """
    View with centered quantity above children.

    QuantityAbove must has only one children!
    """
    padding = 3

    def add_children(self, children):
        super(QuantityAbove, self).add_children(children)
        self.arrowhead = self.subfields[0].arrowhead
        assert len(self.subfields) == 1

    def render(self):
        quantity = self.render_image(self.get_field(Character, self.value))
        subfield = self.render_subview(self.subfields[0])

        width = max(quantity.get_width(), subfield.get_width())
        # height = sum((quantity.get_height(), self.padding, subfield.get_height()))

        # backgroudn without border
        # background = self.render_image(self.get_field(Rectangle, (width, height), thickness=0, marked=False))

        quantity_x = (width - quantity.get_width())/2
        subfield_x = (width - subfield.get_width())/2
        subfield_y = quantity.get_height() + self.padding

        quantity_above = Flattener([(quantity, (quantity_x, 0)),
                                    (subfield, (subfield_x, subfield_y))])
        handlers = {
            "left": subfield_y + subfield.get_handler('left'),
            "right": subfield_y + subfield.get_handler('right'),
            'left-x': subfield_x,
            'right-x': subfield_x + subfield.get_width(),
        }
        rendered_fields = self.render_view(quantity_above)
        rendered_fields[0].update_handlers(handlers)
        return rendered_fields
