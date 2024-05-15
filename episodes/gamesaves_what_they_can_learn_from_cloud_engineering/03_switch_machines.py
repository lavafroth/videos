#!/usr/bin/env python
# coding: utf-8

from manim import *

class SwitchMachines(Scene):
    def construct(self):
        codespace = SVGMobject("codespaces.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        desktop = SVGMobject("desktop.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)

        codespace.scale(0.5)
        desktop.scale(0.5)

        desktop.shift(3 * RIGHT)
        codespace.shift(3 * LEFT)

        self.play(AnimationGroup(
            Write(desktop),
            Write(codespace)
        ))

        arrow = Arrow(start=codespace, end=desktop)
        arrow.shift(0.25 * UP)
        self.play(FadeIn(arrow))

        self.wait(2)

        self.play(AnimationGroup(FadeOut(codespace), FadeOut(desktop), FadeOut(arrow)))
