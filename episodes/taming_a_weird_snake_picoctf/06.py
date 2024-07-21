#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        with open('assets/codes/snake.c') as f:
            contents = f.read()

        t = Text(contents, font=codefont, font_size=32).to_edge(UL)
        self.add(t)
        self.play(t.animate.to_edge(DL))
        self.wait(1)
