# -*- coding: utf-8 -*-
try:
    from sdgen.svg import to_svg # backward compatibility
except ImportError:
    to_svg = lambda *a: None
from sdgen.main import to_png
