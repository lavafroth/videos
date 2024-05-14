#!/usr/bin/env python
# coding: utf-8

from manim import *

class Sc(Scene):
    def construct(self):
        c = Circle(radius=1.5, color=WHITE, fill_color=WHITE, fill_opacity=1)
        self.play(c.animate.shift(2 * LEFT))
        rect = RoundedRectangle(width=3, height=1, corner_radius=0.2, fill_opacity=0.3).shift(2 * RIGHT)
        line = Line(start=0.5 * LEFT, end=0.5*RIGHT, color=WHITE)
        fmt = Text('fmt(...)', font='monospace', font_size=26).move_to(rect.get_center())
        access = Code(code='let error_string = format!(trait_object);', language='rust', font_size=26)[2].shift(2.5 * DOWN)
        curved_arrow = CurvedArrow(start_point=access.get_edge_center(RIGHT) + 0.25 * RIGHT, end_point=rect.get_edge_center(RIGHT), angle=PI)
        self.play(Write(access), AnimationGroup(Create(line), Create(rect), Write(fmt), lag_ratio=0.8))
        self.play(Create(curved_arrow))
        self.wait(2)
        self.play(FadeOut(c, rect, line, curved_arrow, access, fmt))
        self.wait(1)
