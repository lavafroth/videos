#!/usr/bin/env python
# coding: utf-8

from manim import *

class OverlayFS(Scene):
    def construct(self):
        git = SVGMobject("git",  fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6).scale(1.5)
        text = Text("git gud?", font="monospace").shift(2.5 * DOWN)
        self.play(AnimationGroup(
            Write(git),
            Write(text)
        ))
        self.wait(8)
        self.play(AnimationGroup(
            FadeOut(git),
            FadeOut(text)
        ))
