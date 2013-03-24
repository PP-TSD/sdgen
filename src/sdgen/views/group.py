# -*- coding: utf-8 -*-
from itertools import tee, izip

from ._view import View
from .connection import Connection
from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.fields.character import Character
from sdgen.fields.rectangle import Rectangle
from sdgen.fields.simple_arrow import SimpleArrow
from sdgen.fields.flattener import Flattener


class Group(View):
    render_config_key = "group"
    default_render_config = {
        "padding": 10,
        "arrow.height": 1,
        "arrow.width": 10,
        "border.size": 1
    }

    def get_arrow(self, x_offset, y_offset):
        arrow = SimpleArrow((self.arrow_width, self.arrow_height)).to_png()
        arrow.set_position(x_offset, y_offset)
        return arrow

    def render(self):
        # render ImageWrappers of fields
        fields = [subfield.render() for subfield in self.subfields]

#        connections = []
#        # add connections
#        for i in range(len(fields) - 1):
#            if not isinstance(self.subfields[i], Connection) and not isinstance(self.subfields[i+1], Connection):
#                connection = Connection(fields[i], fields[i+1])
#                connections.append((connection, i+1))

#        padding = 10
        
#        for connection, position in reversed(connections):
#            fields.insert(position, connection.render())

        header = self.render_image(Character(self.name, font_color="white", background="black"))
        header_height = header.height + self.border_size

        max_height = max(map(lambda f: f.get_height(), fields))

        def next_field():
            x = self.padding
            for field in fields:
                yield field, (x, header_height + self.padding + (max_height - field.get_height())/2)
                x += field.get_width()

        width = sum(map(lambda f: f.get_width(), fields)) + 2*self.padding
        height = max_height + header_height + 2*self.padding

        background = self.render_image(Rectangle((width, height)))
        field = Flattener(background, [(header, (0, 0))] + list(next_field()))

        return self.render_image(field)
