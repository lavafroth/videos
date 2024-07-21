#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        end_box = RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05)
        end_txt = Text("<listcomp>", font=codefont, font_size=32).move_to(end_box).set_z_index(2)
        end_txt.shift(4 * RIGHT)
        self.add(end_txt)
