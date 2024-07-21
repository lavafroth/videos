#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        end_box = RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05).shift(4 * RIGHT)
        end_txt = Text("(  )", font=codefont, font_size=40)
        self.play(Transform(end_box, end_txt))
        self.wait(2)
