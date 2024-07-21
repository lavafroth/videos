#!/usr/bin/env manim
from manim import *
from hackermanim import *
import string

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        p = SVGMobject('picoctf-logo-horizontal-white.svg')
        self.play(Write(p))
        self.wait(1)
        t = Text('"Weird snake"').shift(1.5 * DOWN)
        a = Arrow(p.get_edge_center(DOWN) + 1.5 * UP, t.get_edge_center(UP))
        agr = AnimationGroup(
            p.animate.shift(1.5 * UP),
            Create(a),
            FadeIn(t),
            lag_ratio=0.3
        )
        self.play(agr)
        self.wait(2)
        self.play((FadeOut(x) for x in (a, t)), p.animate.move_to(ORIGIN))
        self.wait(1)
        f = SVGMobject('flag', fill_color=WHITE).scale(0.5).shift(2 * RIGHT)
        lol = VGroup(p.copy().scale(0.7), f).arrange(buff=1.0)
        self.play(ReplacementTransform(p, lol[0]), FadeIn(lol[1]))
        self.wait(2)
        cmu = SVGMobject('cmu').shift(UP)
        self.play(FadeIn(cmu), lol.animate.shift(DOWN))
        self.wait(3)
