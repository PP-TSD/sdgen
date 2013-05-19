# -*- coding: utf-8 -*-
from sdgen.fields import Flattener
from _view import View
from connections.connection import Connection


class Sequence(View):
    """
    Sequence of views, separated by arrow.

    Arrows can be specified by putting
    :class:`sdgen.views.connections.connection.Connection` in children.
    If connection is not specified, default is used.
    """
    arrowhead = True

    def add_children(self, children):
        new_children = []
        for el1, el2 in self._pairs(children):
            if isinstance(el1, Sequence):
                el1.trim_arrows()

            el1_conn = isinstance(el1, Connection)
            el2_conn = isinstance(el2, Connection)
            # if one of siblings is connection
            if el1_conn != el2_conn:
                if el1 is None:
                    continue
                if el1_conn and el2 and el2.arrowhead:
                    el1.sharp = False
                new_children.append(el1)
            else:
                # if siblings are not separated by connection or this is last
                if not (el1_conn or el2_conn) and el1 is not None:
                    new_children.append(el1)
                # check if connection should be sharp
                sharp = not el2.arrowhead if el2 else True
                new_children.append(Connection(mark=self.marked, sharp=sharp))

        super(Sequence, self).add_children(new_children)

    def trim_arrows(self):
        """ Delete sourrounding arrows """
        self.subfields = self.subfields[1:-1]
        if self.subfields[0]:
            self.arrowhead = self.subfields[0].arrowhead
        else:
            self.arrowhead = False

    def render(self):
        # render ImageWrappers of fields
        fields = map(self.render_subview, self.subfields)

        top_max_height = max([max(x.get_handlers().values()) for x in fields])

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

        # get y coordinate of last fields and add it's right handler
        right_handler = (positioned_fields[-1][1][1] +
            positioned_fields[-1][0].get_handler('right'))
        field = Flattener(list(next_field()))

        handlers = {
            "left": top_max_height,
            "right": right_handler
        }
        rendered_fields = self.render_view(field)
        rendered_fields[0].update_handlers(handlers)
        return rendered_fields
