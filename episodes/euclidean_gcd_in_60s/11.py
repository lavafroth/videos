#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        d1 = Tex(r'$b \div r$', font_size=150)[0].shift(2 * UP)
        d1_ = Tex(r'$b = q_1 \cdot r + r_1$', font_size=150)[0].shift(2 * UP)
        self.play(
            Write(d1)
        )
        self.play(
            Transform(d1[0], d1_[0]),
            Transform(d1[2], d1_[5]),
            Transform(d1[1], VGroup(d1_[1:5], d1_[6:]))
        )
        self.wait(1)
