#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        implerr = Code('implerror.rs')[2]
        self.play(FadeIn(implerr))
        self.play(implerr.animate.set_opacity(0.5))
        x_scale = 1.2
        x = [
            Line(start=x_scale * UR, end=x_scale * DL, stroke_width=5, color=RED),
            Line(start=x_scale * UL, end=x_scale * DR, stroke_width=5, color=RED)
        ]
        for line in x:
            self.play(Create(line), run_time=0.5)
        self.wait(2)
        grp = Group(*x, implerr)

        t = Text('thiserror', font=codefont, font_size=40)
        self.play(ReplacementTransform(grp, t))
        self.play(t.animate.shift(1 * LEFT))
        e = Text('::Error', font=codefont, t2c={'Error': GREEN}, font_size=40).next_to(t, buff=0.15)
        self.play(FadeIn(e))
        self.wait(1)
