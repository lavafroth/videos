#!/usr/bin/env manim
from manim import *
class CodeBlock(Scene):
    def construct(self):
        clock = SVGMobject("clock", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        self.play(Write(clock))
        self.wait(4)
        self.play(FadeOut(clock))
