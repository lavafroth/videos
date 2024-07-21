#!/usr/bin/env manim
from manim import *
from hackermanim import *

width = int(1080)
height = int(1920)
config.frame_size = [width, height]

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        d1_ = Tex(r'$g = r_{n-1}$', font_size=150)[0]
        d1 = Tex(r'$Euclidean\ GCD\ Algorithm$', font_size=100)[0]
        d2 = Tex(r'$in \leq 60s$', font_size=150)[0]
        grp = VGroup(d1, d2).set_y(0).arrange(direction=DOWN, buff=1.0)
        self.play(Transform(d1_, d1))
        self.play(Write(d2))
        self.wait(4)
