#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        raw = '''
def foo(a: int, b: int, c: str):
    pass
        '''
        pycode = Code(code=raw.strip(), font_size=32, language='python')[2].shift(3.5 * LEFT)
        su = SurroundingRectangle(pycode[0][8:14], color=BLUE, corner_radius=.05)
        self.play(Create(su))
        self.wait(.5)

        su_ = SurroundingRectangle(pycode[0][16:16+6], color=BLUE, corner_radius=.05)
        self.play(Transform(su, su_))
        self.wait(.5)

        su_ = SurroundingRectangle(pycode[0][16+6+2:16+6+2+6], color=BLUE, corner_radius=.05)
        self.play(Transform(su, su_))

        self.wait(4)
