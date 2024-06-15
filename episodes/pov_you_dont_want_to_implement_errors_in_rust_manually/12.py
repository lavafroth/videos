#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        cfg = Text("#[cfg]", color="GREEN", font=codefont, font_size=50)
        test = Text("#[test]", color="GREEN", font=codefont, font_size=50)
        self.add(cfg)
        parts = lambda cfg: [cfg[:2], cfg[2:-1], cfg[-1]]
        self.play(Transform(a,b) for a,b in zip(parts(cfg), parts(test)))
        self.wait(1)
