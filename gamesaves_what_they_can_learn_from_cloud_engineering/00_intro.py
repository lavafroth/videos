#!/usr/bin/env python
# coding: utf-8

from manim import *

class Intro(Scene):
    def construct(self):
        dead_cells = SVGMobject("dead_cells.svg", fill_color=RED, stroke_color=RED, fill_opacity=0.6)
        self.play(Write(dead_cells))
        self.play(dead_cells.animate.shift(2 * LEFT))

        archlinux = SVGMobject("archlinux_logo.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        archlinux.shift(2 * RIGHT)
        self.play(Write(archlinux))

        self.wait(2)
        self.play(AnimationGroup(
            FadeOut(dead_cells),
            FadeOut(archlinux)
        ))
