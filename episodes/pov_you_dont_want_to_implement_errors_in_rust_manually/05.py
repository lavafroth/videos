#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        f = Text('#[error]', font=codefont, font_size=40, color=GREEN_D)
        f_copy = f.copy()
        self.add(f)
        code = Code('expanded.rs')[2].shift(LEFT/4)
        self.play(Transform(f, code))
        self.wait(3)
        self.play(Transform(f, f_copy))
        self.wait(2)
