#!/usr/bin/env manim
from manim import *
from hackermanim import *
import string

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        f = SVGMobject('flag-race', color=WHITE, fill_opacity=0).scale(5).shift(1.5 * DOWN)
        self.play(Write(f), run_time=5)
