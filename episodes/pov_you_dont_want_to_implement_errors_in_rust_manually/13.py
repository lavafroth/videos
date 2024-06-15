#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        test = Text("#[test]", color="GREEN", font=codefont, font_size=50)
        self.add(test)
        code = Code('test_inert.rs', font_size=32)[2]
        asld = -len(test)
        self.play(FadeIn(code[0:2]), FadeIn(code[3:]), Transform(test, code[2][asld:]))
        self.wait(3)
