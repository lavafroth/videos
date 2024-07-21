#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        t = Text('Please ')
        bear = SVGMobject('bear').scale(0.5)
        t2 = Text(' with me')
        vg = VGroup(t, bear, t2).arrange(buff=0.2)
        self.play(Write(vg))
        self.wait(3)
        self.play(vg.animate.shift(12 * LEFT).fade(1))
