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
        cd1 = Tex(r'$r = q_2 \cdot r_1 + r_2$', font_size=150)[0].shift(.5 * UP)
        self.add(cd1)
        d1 = Tex(r'$r_1 \div r_2$', font_size=150)[0].shift(DOWN)
        d1_ = Tex(r'$r_1 = q_3 \cdot r_2 + r_3$', font_size=150)[0].shift(DOWN)
        self.play(
            Write(d1)
        )
        self.play(
            Transform(d1[0:2], d1_[0:2]),
            Transform(d1[3:], d1_[6:8]),
            Transform(d1[2], VGroup(d1_[2:6], d1_[8:]))
        )
        ell = Tex('$...$', font_size=150)[0].rotate(-PI/2).shift(2.5 * DOWN)
        self.play(Write(ell))
        d1 = Tex(r'$r_{n-2} \div r_{n-1}$', font_size=150)[0].shift(4 * DOWN)
        d1_ = Tex(r'$r_{n-2} = q_n \cdot r_{n-1} + r_n$', font_size=140)[0].shift(4 * DOWN)
        self.play(
            Write(d1)
        )
        self.play(
            Transform(d1[0:4], d1_[0:4]),
            Transform(d1[5:], d1_[8:12]),
            Transform(d1[4], VGroup(d1_[4:8], d1_[12:])),
        )
