#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        code = Code("cfg.rs", font_size=32)[2]
        self.add(code)
        text = Text("Compiling for Linux").to_edge(UP)
        self.play(FadeIn(text))
        rect = Rectangle(
            width=code[1].width + 0.25, height=code[1].height * 2 + 0.25
        ).move_to((code[1].get_center() + code[0].get_center()) / 2 + 0.5 * RIGHT)
        self.wait(2)
        self.play(Create(rect))
        self.play(AnimationGroup(Unwrite(code[0:2]), FadeOut(rect), lag_ratio=0.7))
        self.play(code[3:].animate.shift(0.5 * UP))
        self.play(FadeOut(text))
        cfg = Text("#[cfg]", color="GREEN", font=codefont, font_size=50)
        l = code[3]
        a, b = cfg[:-1], cfg[-1]
        _a, _b = l[:5], l[-1]
        self.play(
            Transform(_a, a), Transform(_b, b), FadeOut(code[4:]), FadeOut(l[5:-1])
        )
        self.wait(1)
