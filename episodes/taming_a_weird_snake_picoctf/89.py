#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        codefont = "Terminess Nerd Font Propo"
        Code.set_default(font=codefont, style="monokai")
        te = Text('earlier', font=codefont, font_size=40)
        t = octicon('triangle-left-24', fill_color=WHITE).shift(3.2 * DOWN + RIGHT).scale(0.2)
        t1 = t.copy().shift(.2 * RIGHT)
        ts = VGroup(t, t1)
        VGroup(ts, te).arrange().to_edge(DL)
        self.play(Write(te), AnimationGroup(
                      (FadeIn(x, shift=LEFT) for x in ts),
                      lag_ratio=0.5
                  ))
        self.wait(5)
