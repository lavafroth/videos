#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        p = octicon('file-24', fill_color=WHITE).scale(0.6)
        subtext = Text('snake', font=codefont, font_size=34)
        vg = VGroup(p, subtext).arrange(DOWN, buff=0.2)
        self.play(FadeIn(p))
        self.play(Write(subtext))

        with open('assets/codes/snake.smol') as f:
            contents = f.read()

        t = Text(contents, font=codefont, font_size=32).to_edge(UL)
        self.play(Transform(vg, t))
