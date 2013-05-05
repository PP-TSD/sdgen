# -*- coding: utf-8 -*-


class ImageWrapper(object):
    '''
    Wrap object representing image. Provide additional features.

    Wrap image in any format working with coordinates (svg, png or other)
    and provide such features like getting size of image or handlers.
    '''
    name = None

    def __init__(self, image, width, height, name=None, handlers=None):
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
        self.name = name
        self.handlers = {
            "left": height/2.0,
            "right": height/2.0,
        }
        if isinstance(handlers, dict):
            self.handlers.update(handlers)

    def get_size(self):
        """
        Get (width, height) of image.
        """
        return self.width, self.height

    def get_width(self):
        """
        Get width of image.
        """
        return self.width

    def get_height(self):
        """
        Get height of image.
        """
        return self.height

    def get_handlers(self):
        """
        Get handlers.

        Returns:
            dict: y coordinate of all handlers.
        """
        return self.handlers

    def get_handler(self, handler):
        """
        Get handler with given name.

        Args:
            handler (str): Name of handler.

        Returns:
            float: y coordinate of concrete handler.
        """
        if not handler in self.handlers:
            raise KeyError("Invalid handler name.")
        return self.handlers[handler]

    def update_handlers(self, handlers):
        """
        Update handlers with given dict.

        Args:
            handlers (dict): y coordinates of handlers.
        """
        assert isinstance(handlers, dict), "handlers must be a dict"
        self.handlers.update(handlers)

    def get_image(self):
        """
        Get wrapper's content.

        Returns:
            object: return wrapper's content.
        """
        return self.image

    def get_image_with_name(self):
        return (self.name, self.image)

    def set_image(self, image):
        """
        Set wrapper's content.

        Returns:
            object: return wrapper's content.
        """
        self.image = image
        return image

    def scale_parameters(self, scale):
        """
        Scale width, height and handlers with given scale.

        Args:
            scale (float): scale, (0,1) makes image smaller, (1,..) larger.
        """
        self.width = self.width * scale
        self.height = self.height * scale
        for k, v in self.handlers.items():
            self.handlers[k] = v * scale
