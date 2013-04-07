# -*- coding: utf-8 -*-
from _loop_arrow import LoopArrow
from sdgen.utils.antialiasing import antialiasing
from sdgen.utils.helpers import relative

@antialiasing
class ReturnArrow(LoopArrow):
    render_config_key = "return"

    def get_bezier_points_lists(self):
        total_width = self.width + self.right_length + self.left_length
        return [# left curve
                [(self.left_length / 2, self.padding),
                (0, self.padding),
                (0, self.left_height),
                (self.left_length / 2, self.left_height)],
                # right curve
                [(total_width - self.right_length / 2, self.right_height),
                (total_width, self.right_height),
                (total_width, self.padding),
                (total_width - self.right_length / 2, self.padding)]
                ]

    def get_line_points_lists(self):
        return [
                # horizontal line between curves
                (self.left_length / 2, self.padding,
                 self.width + self.left_length * 3 / 2, self.padding)
                ]
    
    def get_polygons_points_lists(self):
        polygons = []
        
        points = self.get_line_points_lists()[0]
        assert len(points) == 4, "Line should be 4-touple with 2 points coordinates"
        center = (points[0] + points[2]) / 2.0, (points[1] + points[3]) / 2.0
        return [
                # marker coordinates
                [relative(center, (-self.marker / 2.0, 0)),
                 relative(center, (self.marker / 2.0, -self.marker / 3.0)),
                 relative(center, (self.marker / 2.0, self.marker / 3.0))]
                ]

    def get_handlers(self, height):
        return {
                "left": height,
                "right": height,
                }