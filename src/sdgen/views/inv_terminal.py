# -*- coding: utf-8 -*-
from ._view import View
from .terminal import Terminal
#from .inv_terminal_child import InvTerminalChild


class InvTerminal(View):
    render_config_key = "inv_terminal"

    # def add_children(self, children):
    #     """
    #     Replace all Terminal children instances to InvTerminalChild instances
    #     with same config.
    #     """
    #     replaced_children = []
    #     for child in children:
    #         assert isinstance(child, Terminal)
    #         inv_terminal_child = InvTerminalChild(name=child.name,
    #                                               type=child.type,
    #                                               value=child.value,
    #                                               mark=child.mark,
    #                                               **child._passed_config)
    #         replaced_children.append(inv_terminal_child)
    #     super(InvTerminal, self).add_children(replaced_children)
