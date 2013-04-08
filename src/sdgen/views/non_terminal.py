# -*- coding: utf-8 -*-
import copy

from ._view import View
from .group import Group
from ..fields.character import Character
from ..fields.rectangle import Rectangle
from ..fields.flattener import Flattener


class NonTerminal(View):
    save_as_subimage = True
    padding = 5

    def render_subimage(self):
        # create a group view, that should be saved as separated image
        config = copy.deepcopy(self._passed_config)
        if 'view' in config:
            del config['view']
        if 'children' in config:
            del config['children']
        group = Group(name=self.name, type_=self.type, value=self.value, mark=self.marked, save_as_subimage=True, **config)
        group.add_children(self.subfields)
        return group.render()

    def render(self):
            text = self.render_image(self.get_field(Character, self.name))
            border = self.render_image(self.get_field(Rectangle, tuple(p + self.padding * 2 for p in text.get_size())))

            nonterminal = Flattener(border, [(text, (self.padding,) * 2)])
            return self.render_view(nonterminal)
