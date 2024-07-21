#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        o = Tex('$a\ \ \ b$', font_size=180)[0]
        a = o[0]
        b= o[-1]
        div = Tex('$<$', font_size=180)
        div_ = Tex('$b \div a$', font_size=180)[0]
        self.add(o)
        self.play(
            ReplacementTransform(a, div_[-1]),
            ReplacementTransform(b, div_[0]),
            ReplacementTransform(div, div_[1]),
        )
        self.wait(1)

        q = Tex('$quotient = q$', font_size=180)[0]
        r = Tex('$remainder = r$', font_size=180)[0]
        qr = VGroup(q, r).set_y(0).arrange(direction=DOWN, buff=1.0)
        self.play(div_.animate.shift(4 * UP), Write(qr))
        self.wait(2)
