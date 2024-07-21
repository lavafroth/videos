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
        rect = SurroundingRectangle(expr[0], buff=0.4, color=TEAL)
        rect_r = SurroundingRectangle(expr[-1], buff=0.4, color=TEAL)
        self.play(Create(rect), Create(rect_r))
        self.play(FadeOut(rect), FadeOut(rect_r))
        self.wait(2)
