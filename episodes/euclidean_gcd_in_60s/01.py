#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        a = Tex('$a\ \ \ b$', font_size=180)
        self.play(FadeIn(a))
        self.wait(2)
