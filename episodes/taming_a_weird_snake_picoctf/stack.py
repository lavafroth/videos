#!/usr/bin/env manim
from manim import *
from hackermanim import *

def stackvar(color, opacity=0.5):
    return RoundedRectangle(
        width=4,
        height=1,
        color=color,
        fill_color=color,
        fill_opacity=opacity,
        corner_radius=0.05,
    )

n = 3
stack = VGroup(*(stackvar(BLUE).fade(x / n) for x in range(n))).arrange(DOWN)
