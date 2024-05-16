#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        arm = SVGMobject('assets/arm').scale(0.25)
        self.play(Write(arm))
        neon = Text('NEON', font_size=40).set_opacity(0)
        self.play(arm.animate.shift(LEFT), neon.animate.set_opacity(1).shift(RIGHT))

        text = Text('disabled by default', font_size=24).shift(DOWN)
        self.play(FadeIn(text))
        self.wait(4)
        self.play(FadeOut(text, arm, neon))
