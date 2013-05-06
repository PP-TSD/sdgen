# -*- coding: utf-8 -*-
from sdgen.views.connections.connection import Connection


class LoopConnection(Connection):
    """
    Abstract loop connection.
    
    Ancestor of
    :class:`sdgen.views.connections.return_connection.ReturnConnection` and
    :class:`sdgen.views.connections.detour_connection.DetourConnection`.
    
    Each descendant should provide :func:`self.get_loop_arrow_class`.
    After initialization and before render :func:`self.set_subfield_params`
    should be called, otherwise render will raise exception. This behavior
    is result of wrapping subfield by LoopConnection, so size of connection
    could be set only when subfield is rendered.
    """
    def get_loop_arrow_class(self):
        """Return class of loop-arrow field.

        :rtype: :class:`sdgen.fields._loop_arrow.LoopArrow`
        """
        raise NotImplementedError

    def set_subfield_params(self, size, handlers):
        """Provide informations about size and handlers of wrapped subfield.
        
        :param size: Size of wrapped subfield.
        :type size: tuple
        :param handlers: Wrapped subfield's handlers.
        :type handlers: dict
        """
        self.subfield_width, self.subfield_height = size  # in pt
        self.left_height, self.right_height = handlers['left'], handlers['right']
        self.subfield_size = True

    def render(self):
        assert getattr(self, 'subfield_size', False), "Subfield size undefined"
        arrow_class = self.get_loop_arrow_class()
        loop = arrow_class(self.subfield_width,
                           self.left_height,
                           self.right_height,
                           left_length=self.left_length,
                           right_length=self.right_length,
                           marked=self.marked)
        return self.render_view(loop)
