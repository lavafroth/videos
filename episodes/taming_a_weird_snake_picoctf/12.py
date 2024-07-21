#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font='Poppins')
        Code.set_default(font=codefont, style="monokai")

        fb = octicon('file-binary-24', fill_color=WHITE)
        self.add(fb)
        self.play(fb.animate.scale(0.5).shift(2 * UP))
        vm = SVGMobject('server-24').set_z_index(1).scale(0.7)
        self.play(FadeIn(vm))
        self.play(fb.animate.shift(2 * DOWN))
        self.wait(1)
