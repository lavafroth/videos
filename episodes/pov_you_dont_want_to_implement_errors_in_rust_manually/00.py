#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        
        rect = RoundedRectangle(corner_radius=.5, width=4*2, height=4*2*9/16, color=WHITE).shift(7 * DOWN)
        self.play(rect.animate.shift(7 * UP))
        self.wait(8)
        self.play(rect.animate.shift(8 * DOWN))
