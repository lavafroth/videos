#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        me = RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05, fill_color=WHITE, fill_opacity=1)
        self.add(me)
        self.play(me.animate.shift(4 * RIGHT))
        self.wait(1)
