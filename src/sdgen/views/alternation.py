# -*- coding: utf-8 -*-
from connections.alternation_connection import AlternationConnection
from ._view import View


class Alternation(View):
    padding = 5
    arrow_width = 10
    
    def add_children(self, children):
        assert children, "Alternation children lists shouldn't be empty"
        extended = []
        # dict for fast navigation over connections (linked with children)
        # each child should have "left" and "right" connection generated
        self.alternation_connections = {}
        
        for i in len(children):
            if isinstance(children[i], Connection):
                # children list should be:
                # *(child | connection,child,connection)+
                assert len(children) >= i + 2, "Inproper children list"
                assert ((isinstance(children[i + 1], View) and
                        isinstance(children[i + 2], AlternationConnection)),
                        "Inproper children list")
                extended.extend(children[i:i + 2])
                child = children[i + 1]
                left = children[i],
                right = children[i + 2],
                i += 2
            else:
                left = AlternationConnection()
                right = AlternationConnection()
                child = children[i]

            extended.append(child)
            self.alternation_connections[child] = dict(left=left, right=right)

        super(InvTerminal, self).add_children(replaced_children)
    
    def render(self):
        padding = self.pt_to_px(self.padding)
        arrow_width = self.pt_to_px(self.arrow_width)
        
        left_connections = []
        right_connections = []
        total_height = sum([c.get_height() for c in self.subfield])