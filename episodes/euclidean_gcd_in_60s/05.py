#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        expr = Tex(r'$b = q \cdot a + r$', font_size=180)[0]
        self.add(expr)
        self.play(expr.animate.shift(2 * DOWN))

        gcd = Tex(r'$gcd(a, b) = g$', font_size=180)[0]
        ax = Tex(r'$a = k_1 \cdot g$', font_size=180)[0]
        bx = Tex(r'$b = k_2 \cdot g$', font_size=180)[0]
        gab = VGroup(gcd, ax, bx).set_y(0).arrange(direction=DOWN, buff=1.0).shift(4 * UP)
        self.play(Write(gcd))
        self.play(Transform(gcd[4].copy(), ax[0]), Transform(gcd[-1].copy(), ax[-1]), Write(ax[1:-1]))
        self.play(Transform(gcd[6].copy(), bx[0]), Transform(gcd[-1].copy(), bx[-1]), Write(bx[1:-1]))
        # expr = Tex(r'$k_2 \cdot g = q \cdot k_1 \cdot g + r$', font_size=150)[0].shift(DOWN)
        # self.add(expr)
        self.wait(2)
