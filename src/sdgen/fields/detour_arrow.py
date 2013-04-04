# -*- coding: utf-8 -*-
import Image
import ImageDraw

from sdgen.utils.image_wrapper import ImageWrapper
from sdgen.utils.bezier import make_bezier
from arrow import Arrow
from _field import antialiasing


@antialiasing
class DetourArrow(Arrow):
    render_config_key = "detour"
    padding = 10

    def __init__(self, width, left_height, right_height, *args, **kwargs):
        super(DetourArrow, self).__init__(*args, **kwargs)
        self.width = width  # in pt
        self.left_height = left_height  # in pt
        self.right_height = right_height  # in pt
        self.height = max(left_height, right_height)

    def to_png(self):
        padding = self.pt_to_px(self.padding)
        width, height = self.pt_to_px(self.width) + 4 * padding, self.pt_to_px(self.height) + 2 * padding
        thickness = self.pt_to_px(self.thickness)
        image = Image.new('RGBA', (width, height))
        left_height = self.pt_to_px(self.left_height)
        right_height = self.pt_to_px(self.right_height)
        marker = self.pt_to_px(self.marker)
        draw = ImageDraw.Draw(image)

        bezier_points_lists = [# left curve
                  [(0, 0),
                  (padding, 0),
                  (0, left_height + padding),
                  (2 * padding, left_height + padding)],
                  # right curve
                  [(width - 2 * padding, right_height + padding),
                  (width, right_height + padding),
                  (width - padding, 0),
                  (width, 0)]
                  ]
        
        for bezier_points in bezier_points_lists:
            bezier = make_bezier(bezier_points)
            samples = max(width, height) * 3.0
            half_thickness = thickness / 2
            
            for point in bezier([t/samples for t in range(int(samples))]):
                draw.ellipse((point[0] - half_thickness, point[1] - half_thickness,
                              point[0] + half_thickness, point[1] + half_thickness),
                             fill = self.fill, outline = self.fill)

        relative = lambda (x1, y1), (x2, y2): (x1 + x2, y1 + y2)
        
        line_points = (2 * padding, left_height + padding, width - 2 * padding, right_height + padding)
        line_center = (line_points[0] + line_points[2]) / 2, line_points[1]
        
        draw.line(line_points, width=thickness, fill=self.fill)
        draw.polygon([relative(line_center, (marker / 2, 0)),
                      relative(line_center, (-marker / 2, -marker / 3)),
                      relative(line_center, (-marker / 2, marker / 3))],
                     fill=self.fill,
                     )
        return ImageWrapper(image, width, height)
