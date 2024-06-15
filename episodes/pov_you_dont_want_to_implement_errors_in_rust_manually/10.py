#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        cfg = Text('#[cfg]', color='GREEN', font=codefont, font_size=50)
        self.play(Write(cfg))
        code = Code('cfg.rs', font_size=32)[2]
        l = code[0]
        a, b = cfg[:-1], cfg[-1]
        _a, _b = l[:5], l[-1]
        self.play(Transform(a, _a), Transform(b, _b), FadeIn(code[1:]), FadeIn(l[5:-1]))
        self.wait(4)
