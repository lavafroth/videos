#!/usr/bin/env manim
# this scene doesn't work since manim can't handle large chunks
# of text. lol get rekt
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        with open('assets/codes/snake.c') as handle:
            raw = handle.read()
        code = MonoParagraph(raw)[72:].to_edge(UL)
        self.add(code)
        self.wait(4)
