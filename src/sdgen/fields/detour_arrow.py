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
    padding = 7

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
        draw = ImageDraw.Draw(image)

        bezier_points = [# left curve
                  (0, left_height + 2 * padding),
                  (2 * padding, left_height + 2 * padding),
                  (0, 0),
                  (2 * padding, 0),
                  # subfield corners
                  (2 * padding, 2 * padding),
                  (width - 2 * padding, 2 * padding),
                  # right curve
                  (width - 2 * padding, 0),
                  (width, 0),
                  (width - 2 * padding, right_height + 2 * padding),
                  (width, right_height + 2 * padding)
                  ]
        
        bezier = make_bezier(bezier_points)
        samples = max(width, height) * 3.0
        half_thickness = thickness / 2
        for point in bezier([t/samples for t in range(int(samples))]):
            draw.ellipse((point[0] - half_thickness, point[1] - half_thickness,
                          point[0] + half_thickness, point[1] + half_thickness),
                         fill = self.fill, outline = self.fill)
#        #draw lines
#        
#        draw.line((padding * 2, padding * 2, padding, left_height + padding), width=thickness, fill=self.fill)
#        draw.line((width - padding * 2, padding * 2, width - padding, right_height + padding), width=thickness, fill=self.fill)
#        draw.line((padding * 3, padding, width - padding * 3, padding), width=thickness, fill=self.fill)
#
#        #draw outlines
#        half_thickness = thickness / 2
#        draw.pieslice((-padding - half_thickness, left_height - half_thickness,
#                       padding + half_thickness,
#                       left_height + padding * 2 + half_thickness), 0, 90,
#                      outline=self.fill, fill=self.fill)
#        draw.pieslice((padding * 2 - half_thickness, padding - half_thickness, padding * 4 + half_thickness,
#                       padding * 3 + half_thickness), 180, 270, outline=self.fill, fill=self.fill)
#        draw.pieslice((width - padding * 4 - half_thickness, padding - half_thickness, width - padding * 2 + half_thickness,
#                       padding * 3 + half_thickness), 270, 0, outline=self.fill, fill=self.fill)
#        draw.pieslice((width - padding - half_thickness, right_height - half_thickness, width + padding + half_thickness,
#                       right_height + padding * 2 + half_thickness), 90, 180,
#                      outline=self.fill, fill=self.fill)
#        
#        # fill transparent
#        transparent = (0, 0, 0, 0)
#        draw.pieslice((-padding + half_thickness, left_height + half_thickness,
#                       padding - half_thickness,
#                       left_height + padding * 2 - half_thickness), 0, 90,
#                      outline=transparent, fill=transparent)
#        draw.pieslice((padding * 2 + half_thickness, padding + half_thickness, padding * 4 - half_thickness,
#                       padding * 3 - half_thickness), 180, 270, outline=transparent, fill=transparent)
#        draw.pieslice((width - padding * 4 + half_thickness, padding + half_thickness, width - padding * 2 - half_thickness,
#                       padding * 3 - half_thickness), 270, 0, outline=transparent, fill=transparent)
#        draw.pieslice((width - padding + half_thickness, right_height + half_thickness, width + padding - half_thickness,
#                       right_height + padding * 2 - half_thickness), 90, 180,
#                      outline=transparent, fill=transparent)
        return ImageWrapper(image, width, height)
