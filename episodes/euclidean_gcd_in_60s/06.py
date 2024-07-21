#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        expr = Tex(r'$b = q \cdot a + r$', font_size=180)[0].shift(2 * DOWN)
        self.add(expr)

        gcd = Tex(r'$gcd(a, b) = g$', font_size=180)[0]
        ax = Tex(r'$a = k_1 \cdot g$', font_size=180)[0]
        bx = Tex(r'$b = k_2 \cdot g$', font_size=180)[0]
        gab = VGroup(gcd, ax, bx).set_y(0).arrange(direction=DOWN, buff=1.0).shift(4 * UP)
        self.add(gab)
        expr_ = Tex(r'$k_2 \cdot g = q \cdot k_1 \cdot g + r$', font_size=150)[0].shift(2 * DOWN)
        self.play(FadeOut(gcd))
        self.play(
            Transform(expr[1:4], expr_[4:7]),
            Transform(expr[-2:], expr_[-2:]),
            FadeOut(expr[0], expr[4]),
        )
        self.play(
            Transform(ax[2:], expr_[7:11]),
            FadeOut(ax[:2]),
        )
        self.play(
            Transform(bx[2:], expr_[:4]),
            FadeOut(bx[:2]),
        )
        self.wait(2)
