# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.utils.bezier import make_bezier
from sdgen.utils.antialiasing import antialiasing

from _arrow import Arrow


@antialiasing
class AlternationArrow(Arrow):
    arrow_width = 50

    def __init__(self, size, handlers, left_length=0, right_length=0,*args, **kwargs):
        """
        Generate alternation arrow (curve arrow with marker)
        
        Args:
            size (tuple): size of rect which opaque arrows set
            handlers (dict): wanted arrow handlers
        
        Kwargs:
            left_length (float): length of horizontal line in left of arrow (pt)
            right_length (float): length of horizontal line in right of arrow
        """
        super(AlternationArrow, self).__init__(*args, **kwargs)
        # in pt
        self.size = size
        self.left_length = left_length
        self.right_length = right_length
        self.handlers = handlers
    
    def to_png(self):
        # values in pixels
        left_length = self.pt_to_px(self.left_length)
        right_length = self.pt_to_px(self.right_length)
        width, height = self.pt_to_px(self.size[0]) + left_length + right_length, self.pt_to_px(self.size[1])
        thickness = self.pt_to_px(self.thickness)
        left_handler = self.pt_to_px(self.handlers['left'])
        right_handler = self.pt_to_px(self.handlers['right'])
        arrow_width = self.pt_to_px(self.arrow_width)
        marker = self.pt_to_px(self.marker)

        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)
        
        bezier_points = [(left_length, left_handler),
                         (left_length + arrow_width, left_handler),
                         (left_length, right_handler),
                         (left_length + arrow_width, right_handler)]
        
        bezier = make_bezier(bezier_points)
        samples = float(max(left_length, right_length) + height)
        half_thickness = thickness / 2.0

        for point in bezier([t/samples for t in range(int(samples))]):
            draw.ellipse((point[0] - half_thickness, point[1] - half_thickness,
                          point[0] + half_thickness, point[1] + half_thickness),
                         fill = self.fill, outline = self.fill)

        for line_points in [(0, left_handler, left_length, left_handler),
                            (left_length + arrow_width, right_handler,
                             width - marker, right_handler)]:
            draw.line(line_points, width=thickness, fill=self.fill)
        
        if right_length > marker:
            for polygon_points in [[(width, right_handler),
                                   (width - marker, right_handler - marker / 3),
                                   (width - marker, right_handler + marker / 3)
                                   ]]:
                # polygon_points is a list of tuple with coordinates
                draw.polygon(polygon_points,
                         fill=self.fill,
                         )
        return ImageWrapper(image, self.px_to_pt(width), self.px_to_pt(height), handlers=self.handlers)
