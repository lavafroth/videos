#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        code = Code('deriverror.rs', font_size=32)[2]
        self.add(code)
        f = Text('#[from]', font=codefont, font_size=40, color=GREEN_D)
        rest = code[0:2] + code[3:] + code[2][:7] + code[2][15:]
        self.play(ReplacementTransform(code[2][7:14], f), FadeOut(rest))
        self.wait(1)
