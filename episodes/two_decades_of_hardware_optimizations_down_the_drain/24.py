#!/usr/bin/env manim
from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from custom import CodeTransformer, octicon


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
        vecalloc_rest = (dump[:4], dump[8:])
        self.play(x.animate.set_opacity(0.5) for x in vecalloc_rest)
        self.wait(2)
        self.play(x.animate.set_opacity(1) for x in vecalloc_rest)
