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

        raw = '''
>>> .0 = 42069
  File "<stdin>", line 1
    .0 = 42069
    ^^
SyntaxError: cannot assign to literal here.
Maybe you meant '==' instead of '='?
        '''.strip()
        code = MonoParagraph(raw, t2c={">>>": GREEN, "=": GREEN})
        self.add(code)

        raw = '''
def foo(a: int, b: int, c: str):
    pass
        '''
        pycode = Code(code=raw.strip(), font_size=32, language='python')[2]
        self.wait(1)
        self.play(FadeOut(code))
        self.play(Write(pycode))
        self.play(pycode.animate.shift(3.5 * LEFT))
        header = Text('Bytecode\nrepresentation', font_size=32)
        dz = MonoText('.0')
        dz_copy = dz.copy()
        g = VGroup(header, dz).arrange(DOWN).shift(3.5 * RIGHT)
        self.play(FadeIn(header, shift=UP))
        self.wait(1)
        c = Circle(radius=.2, color=WHITE, fill_color=WHITE, fill_opacity=1).move_to(dz)
        self.play(Create(c))
        self.wait(1)
        self.play(ReplacementTransform(c, dz[0]))
        su = SurroundingRectangle(pycode[0][8:14], color=BLUE, corner_radius=.05)
        self.play(Write(dz[1]))
        self.wait(3.5)

        dz_ = MonoText('.1').move_to(dz)
        su_ = SurroundingRectangle(pycode[0][16:16+6], color=BLUE, corner_radius=.05)
        self.play(Transform(dz[1], dz_[1]))
        self.wait(.5)

        dz_ = MonoText('.2').move_to(dz)
        su_ = SurroundingRectangle(pycode[0][16+6+2:16+6+2+6], color=BLUE, corner_radius=.05)
        self.play(Transform(dz[1], dz_[1]))

        self.wait(1)
        stack.shift(2.5 * DOWN + 4 * RIGHT)
        phantom = stackvar(WHITE).next_to(stack, UP)
        phantom = phantom.next_to(phantom)
        phantom = phantom.next_to(phantom)
        dz_copy.move_to(phantom)
        self.play(FadeOut(pycode, header), Transform(dz, dz_copy))
        self.wait(1)
