#!/usr/bin/env manim
from manim import *
from manim import Transform as T, ReplacementTransform as RT
from hackermanim import *
codefont = "Terminess Nerd Font Propo"

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        th = Text("Thanks for watching!")
        self.play(Write(th))
        self.wait(3)
        pal =SVGMobject('palette', fill_color=WHITE).rotate(-PI/4)
        self.play(
            RT(th, pal)
        )
        self.wait(2)
        self.play(
            pal.animate.to_edge(UR)
        )
        self.wait(5)
