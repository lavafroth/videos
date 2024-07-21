#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        end_txt = Text("<listcomp>", font=codefont, font_size=32).set_z_index(2).shift(4 * RIGHT)
        end_txt_ = Text("<list comprehension>", font=codefont, font_size=32).set_z_index(2).shift(LEFT)
        self.add(end_txt)
        self.play(Transform(end_txt, end_txt_))
        self.wait(2)
