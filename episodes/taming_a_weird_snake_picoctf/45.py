#!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        phantom = stackvar(WHITE).next_to(stack, UP)
        phantom = phantom.next_to(phantom, UP)
        phantom = phantom.next_to(phantom, UP)
        dz = MonoText('.0').move_to(phantom)
        self.add(dz)

        raw = '''
>>> .0 = 42069
  File "<stdin>", line 1
    .0 = 42069
    ^^
SyntaxError: cannot assign to literal here.
Maybe you meant '==' instead of '='?
        '''.strip()
        code = MonoParagraph(raw, t2c={">>>": GREEN, "=": GREEN})
        self.play(Write(code[0][:3]))
        self.play(Transform(dz, code[0][3:5]))
        self.play(Write(code[0][5:]))
        self.wait(1)
        self.play(Write(code[1:]))
        self.wait(2)
