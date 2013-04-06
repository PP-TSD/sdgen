# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.utils.bezier import make_bezier
from arrow import Arrow
from sdgen.utils.antialiasing import antialiasing


@antialiasing
class DetourArrow(Arrow):
    render_config_key = "detour"
    padding = 6

    def __init__(self, width, left_height,
                 right_height, *args, **kwargs):
        super(DetourArrow, self).__init__(*args, **kwargs)
        # in pt
        self.width = width
        self.left_height = left_height
        self.right_height = right_height
        self.height = max(left_height, right_height)

    def get_bezier_points_lists(self):
        total_width = self.width + self.right_length + self.left_length
        return [# left curve
                [(0, 0),
                (self.left_length / 2.0, 0),
                (0, self.left_height + self.padding),
                (self.left_length, self.left_height + self.padding)],
                # right curve
                [(total_width - self.right_length, self.right_height + self.padding),
                (total_width, self.right_height + self.padding),
                (total_width - self.right_length / 2.0, 0),
                (total_width, 0)]
                ]

    def get_line_points_lists(self):
        return [
                # horizontal line between curves
                (self.left_length, self.left_height + self.padding,
                 self.width + self.left_length,
                 self.right_height + self.padding)
                ]
    
    def get_polygons_points_lists(self):
        polygons = []
        relative = lambda (x1, y1), (x2, y2): (x1 + x2, y1 + y2)
        
        points = self.get_line_points_lists()[0]
        assert len(points) == 4, "Line should be 4-touple with 2 points coordinates"
        center = (points[0] + points[2]) / 2.0, (points[1] + points[3]) / 2.0
        return [
                # marker coordinates
                [relative(center, (self.marker / 2.0, 0)),
                 relative(center, (-self.marker / 2.0, -self.marker / 3.0)),
                 relative(center, (-self.marker / 2.0, self.marker / 3.0))]
                ]
    
    def to_png(self):
        padding = self.pt_to_px(self.padding)
        left_length = self.pt_to_px(self.left_length)
        right_length = self.pt_to_px(self.right_length)
        left_height = self.pt_to_px(self.left_height)
        right_height = self.pt_to_px(self.right_height)
        width, height = self.pt_to_px(self.width) + left_length + right_length, self.pt_to_px(self.height) + 2 * padding
        thickness = self.pt_to_px(self.thickness)

        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)
        
        for bezier_points in self.get_bezier_points_lists():
            bezier_points = map(lambda coordinates: tuple(map(self.pt_to_px, coordinates)), bezier_points)
            bezier = make_bezier(bezier_points)
            samples = max(width, height) * 3.0
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
        return ImageWrapper(image, width, height)
