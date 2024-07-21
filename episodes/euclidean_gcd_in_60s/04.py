#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        div_ = Tex('$b \div a$', font_size=180)[0].shift(4 * UP)
        quo = Tex('$quotient = q$', font_size=180)[0]
        rem = Tex('$remainder = r$', font_size=180)[0]
        qr = VGroup(quo, rem).set_y(0).arrange(direction=DOWN, buff=1.0)
        expr = Tex(r'$b = q \cdot a + r$', font_size=180)[0]
        self.add(div_, qr)
        self.play(
            Transform(div_[0], expr[0]),
            Transform(div_[-1], expr[4]),
            FadeOut(div_[1]),
            Transform(quo[-1], expr[2]),
            Transform(rem[-1], expr[-1]),
            FadeOut(quo[:-1]),
            FadeOut(rem[:-1]),
            Write(expr[1]),
            Write(expr[3]),
            Write(expr[5]),
        )
        self.wait(2)
