# -*- coding: utf-8 -*-


class ImageWrapper(object):
    '''
    Wrap object representing image. Provide additional features.
    
    Wrap image in any format working with coordinates (svg, png or other)
    and provide such features like getting size of image or handlers.
    '''

    def __init__(self, image, width, height, handlers=None):
        '''
        Wrapper constructor.
        
        Args:
            image (object): Image, which should be wrapped.
            size (tuple): width and height of image.

        Kwargs:
            handlers (dict): dictionary with relative handlers positions.
        '''
        self.image = image
        self.width = width
        self.height = height
        self.handlers = {
                         "left": (0, height/2),
                         "right": (width, height/2),
                         "top": (width/2, 0),
                         "bottom": (width/2, height),
                         "left-top": (0, 0),
                         "left-bottom": (0, height),
                         "right-top": (width, 0),
                         "right-bottom": (width, height),
                        }
        if isinstance(handlers, dict):
            self.handlers.update(handlers)

    def get_size(self):
        """
        Get (width, height) of image.
        """
        return self.width, self.height

    def get_handlers(self):
        """
        Get handlers.
        
        Returns:
            dict: (x, y) of all handlers.
        """
        return self.handlers

    def get_handler(self, handler):
        """
        Get handler with given name.
        
        Args:
            handler (str): Name of handler.

        Returns:
            tuple: (x, y) of concrete handlers.
        """
        if not handler in self.handlers:
            raise KeyError, "Invalid handler name."
        return self.handlers[handler]
    
    def get_image(self):
        """
        Get wrapper's content.
        
        Returns:
            object: return wrapper's content.
        """
        return self.image
