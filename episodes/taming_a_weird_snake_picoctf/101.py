#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        ch = Text("252", font=codefont, font_size=40).shift(2 * LEFT)
        chn = Text("ü", font=codefont, font_size=40).shift(2 * RIGHT)
        end = chn.get_edge_center(LEFT)
        start = ch.get_edge_center(RIGHT)
        disp = (end - start) * RIGHT
        end = start + disp
        a = Arrow(start, end)
        self.play(FadeIn(ch))
        self.play(Create(a))
        self.play(FadeIn(chn))
        self.wait(2)
