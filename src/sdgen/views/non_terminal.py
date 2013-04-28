# -*- coding: utf-8 -*-
import copy

from sdgen.fields import Character
from sdgen.fields import Rectangle
from sdgen.fields import Flattener
from _view import View
from group import Group


class NonTerminal(View):
    save_as_subimage = True
    font_name = "Times New Roman"
    font_typeface = "bold italic"
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

            nonterminal = Flattener([
                (border, (0, 0)),
                (text, (self.padding, self.padding))
            ])
            return self.render_view(nonterminal)
