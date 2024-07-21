#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        expr = Tex(r'$g \cdot ( k_2 - q \cdot k_1 ) = r$', font_size=150)[0]
        self.add(expr)
        expr_ = Tex(r'$g \cdot k_3 = r$', font_size=150)[0]
        self.play(
            ReplacementTransform(expr[:2], expr_[:2]),
            ReplacementTransform(expr[-2:], expr_[-2:]),
            ReplacementTransform(expr[2:-2], expr_[-4:-2]),
        )
        expr = Tex(r'$r = g \cdot k_3$', font_size=150)[0]
        self.play(
            ReplacementTransform(expr_[-1], expr[0]),
            ReplacementTransform(expr_[-2], expr[1]),
            ReplacementTransform(expr_[0:-2], expr[2:]),
        )
        self.wait(1)
        self.play(expr.animate.shift(4 * UP).set_opacity(0))
