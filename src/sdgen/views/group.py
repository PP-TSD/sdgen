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
        "header.padding": 5,
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
        padding = self.pt_to_px(self.padding)
        fields = [subfield.render() for subfield in self.subfields]
        border_size = self.pt_to_px(self.border_size)

        header = self.render_image(Character(self.name, font_color="white", background="black", padding=self.header_padding))
        
        def get_height(fields):
            top_max_height = max([max(x.get_handlers().values()) for x in fields])
            bottom_max_height = max([x.get_height() - max(x.get_handlers().values()) for x in fields])
            return header.height + top_max_height + bottom_max_height + 2 * (padding + border_size)
        
        width = sum(map(lambda f: f.get_width(), fields)) + 2 * (padding + border_size)
        height = get_height()
        
        def next_field():
            x = padding + border_size
            for field in fields:
                yield field, (x, border_size + header.height + self.padding + (height - field.get_height())/2)
                x += field.get_width()

        background = self.render_image(Rectangle((width, height), thickness=self.border_size))
        field = Flattener(background, [(header, (border_size, ) * 2)] + list(next_field()))

        return self.render_image(field)
