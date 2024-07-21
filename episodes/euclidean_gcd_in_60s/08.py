#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        expr = Tex(r'$k_2 \cdot g - q \cdot k_1 \cdot g = r$', font_size=150)[0]
        self.add(expr)
        expr_ = Tex(r'$g \cdot ( k_2 - q \cdot k_1 ) = r$', font_size=150)[0]
        self.play(
            Transform(expr[3], expr_[0]),
            Transform(expr[10], expr_[0]),
            Transform(expr[2], expr_[1]),
            Transform(expr[9], expr_[1]),
            Transform(expr[0:2], expr_[3:5]),
            Transform(expr[7:9], expr_[8:10]),
            Transform(expr[4:7], expr_[5:8]),
            Transform(expr[-2:], expr_[-2:]),
            Write(expr_[2]),
            Write(expr_[10]),
        )
        self.wait(2)
