# -*- coding: utf-8 -*-
from views import alternation, detour, group, inv_terminal, non_terminal, quantity, quantity_above, quantity_detour, quantity_return, sequence, terminal
from views.connections import connection

# classes for views names
views_classes = {
    "Alternation": alternation.Alternation,
    "Connection": connection.Connection,
    "Detour": detour.Detour,
    "Group": group.Group,
    "InvTerminal": inv_terminal.InvTerminal,
    "NonTerminal": non_terminal.NonTerminal,
    "QuantityAbove": quantity_above.QuantityAbove,
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
        view_name = data.get('view') or data.get('type')
        if not view_name or view_name not in views_classes:
            return None
        view = views_classes[view_name](**data)
        mark_child = 'mark' in data and data['mark'] in (True, 'yes')
        if data.get('children'):
            children = []
            for child in data['children']:
                if mark_child and not 'mark' in child:
                    child['mark'] = mark_child
                child_view = self._parse_data(child)
                if child_view:
                    children.append(child_view)
            if children:
                view.add_children(children)
        return view

    def generate(self, data, input_path, output_dir, *args, **kwargs):
        """
        Builds data structure represented by views.

        Args:
            data (dict): structured data represeting diagaram
            path (str): path to output files
            config (dict): diagram-specific configuration
        """
        self.data = self._parse_data(data)
        result = self.data.render()
        return result
