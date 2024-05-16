#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        dump = (
            Code('pdf_cont.c', font_size=22)[2]
            .to_edge(UL)
            .shift(UP)
        )
        self.add(dump)
        self.play(dump.animate.shift(7.5 * UP).scale(0.6))
        self.wait(4)
