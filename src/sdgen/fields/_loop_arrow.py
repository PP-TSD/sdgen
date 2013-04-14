# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.utils.bezier import make_bezier

from _arrow import Arrow


class LoopArrow(Arrow):
    thickness = 3

    def __init__(self, width, left_height,
                 right_height, *args, **kwargs):
        super(LoopArrow, self).__init__(*args, **kwargs)
        # in pt
        self.width = width
        self.left_height = left_height
        self.right_height = right_height
        self.height = max(left_height, right_height)

    def get_bezier_points_lists(self):
        raise NotImplementedError()

    def get_line_points_lists(self):
        raise NotImplementedError()

    def get_polygons_points_lists(self):
        raise NotImplementedError()

    def get_handlers(self):
        raise NotImplementedError()

    def to_png(self):
        padding = self.pt_to_px(self.padding)
        left_length = self.pt_to_px(self.left_length)
        right_length = self.pt_to_px(self.right_length)
        width, height = (self.pt_to_px(self.width) + left_length + right_length,
                        self.pt_to_px(self.height) + 2 * padding)
        thickness = self.pt_to_px(self.thickness)

        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)

        for bezier_points in self.get_bezier_points_lists():
            bezier_points = map(lambda coordinates: tuple(map(self.pt_to_px, coordinates)), bezier_points)
            bezier = make_bezier(bezier_points)
            samples = height + 2.0 * padding
            half_thickness = thickness / 2.0

            for point in bezier([t/samples for t in range(int(samples))]):
                draw.ellipse((point[0] - half_thickness, point[1] - half_thickness,
                              point[0] + half_thickness, point[1] + half_thickness),
                             fill = self.fill, outline = self.fill)

        for line_points in self.get_line_points_lists():
            draw.line(map(self.pt_to_px, line_points), width=thickness, fill=self.fill)

        for polygon_points in self.get_polygons_points_lists():
            # polygon_points is a list of tuple with coordinates
            draw.polygon(map(lambda coordinates: tuple(map(self.pt_to_px, coordinates)), polygon_points),
                     fill=self.fill,
                     )
        return ImageWrapper(image, self.px_to_pt(width), self.px_to_pt(height), handlers=self.get_handlers(height))
