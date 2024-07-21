#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        cd1 = Tex(r'$b = q_1 \cdot r + r_1$', font_size=150)[0].shift(2 * UP)
        self.add(cd1)
        d1 = Tex(r'$r \div r_1$', font_size=150)[0].shift(.5 *UP)
        d1_ = Tex(r'$r = q_2 \cdot r_1 + r_2$', font_size=150)[0].shift(.5 * UP)
        self.play(
            Write(d1)
        )
        self.play(
            Transform(d1[0], d1_[0]),
            Transform(d1[2:4], d1_[5:7]),
            Transform(d1[1], VGroup(d1_[1:5], d1_[7:]))
        )
