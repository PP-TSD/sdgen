# -*- coding: utf-8 -*-
from views import alternation, connection, group, inv_terminal, non_terminal, quantity, quantity_above, quantity_detour, quantity_return, sequence, terminal

# classes for views names
views_classes = {
    "Alternation": alternation.Alternation,
    "Connection": connection.Connection,
    "Group": group.Group,
    "InvTerminal": inv_terminal.InvTerminal,
    "NonTerminal": non_terminal.NonTerminal,
    "Quantity": quantity.Quantity,
    "QuantityAbove": quantity_above.QuantityAbove,
    "QuantityDetour": quantity_detour.QuantityDetour,
    "QuantityReturn": quantity_return.QuantityReturn,
    "Sequence": sequence.Sequence,
    "Terminal": terminal.Terminal
}


class Builder(object):
    """
    Abstract builder for syntax diagrams.
    """
    def __init__(self):
        self.data = None

    def _parse_data(self, data):
        """
        Parse data and returns View subclass corresponding to top-level data
        entity
        """
        if not data.get('view') or data['view'] not in views_classes:
            return None
        view = views_classes[data['view']](**data)
        if data.get('children'):
            for child in data['children']:
                child_view = self._parse_data(child)
                if child_view:
                    view.add_child(child_view)
        return view

    def generate(self, data, path, config):
        """
        Builds data structure represented by views.

        Args:
            data (dict): structured data represeting diagaram
            path (str): path to output files
            config (dict): diagram-specific configuration
        """
        self.data = self._parse_data(data)
