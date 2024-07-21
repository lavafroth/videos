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
        cd2 = Tex(r'$r = q_2 \cdot r_1 + r_2$', font_size=150)[0].shift(.5 * UP)
        cd3 = Tex(r'$r_1 = q_3 \cdot r_2 + r_3$', font_size=150)[0].shift(DOWN)
        ell = Tex('$...$', font_size=150)[0].rotate(-PI/2).shift(2.5 * DOWN)
        cd4 = Tex(r'$r_{n-2} = q_n \cdot r_{n-1} + r_n$', font_size=140)[0].shift(4 * DOWN)
        self.add(cd1, cd2, cd3, ell, cd4)
        rn = cd4[13:]
        eq = Tex(r'$=$', font_size=140)[0].rotate(PI/2).next_to(rn, direction=DOWN)
        zero = Tex(r'$0$', font_size=140)[0].next_to(eq, direction=DOWN)
        eq_zero = VGroup(eq, zero)
        self.play(Write(eq_zero))
        self.wait(1)
        rect = SurroundingRectangle(cd4[8:12], color=TEAL_D, buff=.3)
        self.play(Create(rect))
        clone = cd4[8:12].copy()
        d = Tex(r'$g = r_{n-1}$', font_size=150)[0]
        self.play(
            (map(FadeOut, (rect, cd1, cd2, cd3, cd4, ell, eq_zero))),
            Transform(clone, d[2:]),
            Write(d[:2]),
        )
        self.wait(2)
