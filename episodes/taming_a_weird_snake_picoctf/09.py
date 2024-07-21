#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        py = SVGMobject('python').scale(1.2)
        py_ = py.copy().shift(.5 * UP)
        l = Text('<listcomp>', font=codefont, font_size=34).next_to(py_, DOWN)
        self.play(Transform(py, py_), FadeIn(l))
        m = Text('list comprehension', font=codefont, font_size=34).next_to(py_, DOWN)
        self.wait(1)
        self.play(
            ReplacementTransform(l[1:5], m[:4]),
            ReplacementTransform(l[5:-1], m[4:]),
            FadeOut(l[0], l[-1])
        )
        self.wait(3)
        self.play(FadeOut(m), py.animate.shift(.5 * DOWN))
        self.wait(1)
