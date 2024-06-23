#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        uni = SVGMobject('university-svgrepo-com', fill_color=BLUE, fill_opacity=0.8).shift(3* LEFT)
        rust = SVGMobject('../assets/rustacean-flat-noshadow').shift(3*RIGHT)
        arrow = Arrow(start=2 * LEFT, end=1.6*RIGHT)
        self.play(AnimationGroup(
            Write(uni),
            Create(arrow),
            FadeIn(rust),
            lag_ratio=0.8,
        ))
        self.wait(2)
        dwaava = SVGMobject('java.svg').shift(2.5 * DOWN)
        self.play(FadeIn(dwaava))
        x_scale = 0.7
        x = [
            Line(start=x_scale * UR, end=x_scale * DL, stroke_width=5, color=RED).shift(2.5 * DOWN),
            Line(start=x_scale * UL, end=x_scale * DR, stroke_width=5, color=RED).shift(2.5 * DOWN)
        ]
        for line in x:
            self.play(Create(line), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(y) for y in x + [dwaava])
        self.wait(4)
        self.play(FadeOut(y) for y in (uni, arrow, rust))
