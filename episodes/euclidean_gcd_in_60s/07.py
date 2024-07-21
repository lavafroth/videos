#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        expr = Tex(r'$k_2 \cdot g = q \cdot k_1 \cdot g + r$', font_size=150)[0].shift(2 * DOWN)
        self.add(expr)
        self.play(expr.animate.shift(2 * UP))
        expr_ = Tex(r'$k_2 \cdot g - q \cdot k_1 \cdot g = r$', font_size=150)[0]
        self.play(
            Transform(expr[:4], expr_[:4]),
            Transform(expr[4], expr_[11]),
            Transform(expr[5:11], expr_[5:11]),
            Transform(expr[11], expr_[4]),
            Transform(expr[12:], expr_[12:]),
        )
        self.wait(2)
