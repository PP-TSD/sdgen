# -*- coding: utf-8 -*-
"""Contains fields - basic elements of views.

Each field represents simple or complex graphical element, for example:
:class:`sdgen.fields.character.Character` or
:class:`sdgen.fields.simple_arrow.SimpleArrow` described with set of
parameters, like padding, width, font_size, etc.
These parameters are given in constructor, except parameters which are
dependent of generated subfields (Author of field with mentioned parameters
should ensure that exception will be raised if needed param is not setted).
Once created field can be builded by call to_* method, where asterisks means
name of wanted format, for example:
:method:`sdgen.fields.character.Character.to_png`.

There are predictions that only two format will be supported: png and svg.
"""
from alternation_arrow import AlternationArrow
from character import Character
from detour_arrow import DetourArrow
from flattener import Flattener
from rectangle import Rectangle
from return_arrow import ReturnArrow
from rounded_rectangle import RoundedRectangle
from simple_arrow import SimpleArrow
