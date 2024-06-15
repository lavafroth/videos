#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        c_5 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    // ...
}
'''
        c_6 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    // ...
}
'''
        c_5 = Code(code=c_5, language='rust', font_size=38, insert_line_no=False)[2]
        c_6 = Code(code=c_6, language='rust', font_size=38, insert_line_no=False)[2]
        self.add(c_5)
        self.play(
            ReplacementTransform(c_5[:4], c_6[:4]),
            ReplacementTransform(c_5[-2:], c_6[-2:]),
            Write(c_6[5])
        )
        self.play(Write(c_6[4]))
        divider = Line(8 * LEFT, 8 * RIGHT).shift(5 * DOWN)
        self.play(divider.animate.shift(4 * UP), c_6.animate.shift(1.5 * UP))
        c = Code(code='''format!("can't load over {} objects", i64::MAX)''', language='rust', font_size=38, insert_line_no=False)[2].next_to(divider, direction=DOWN, buff=1.25)
        self.play(Write(c))
        self.wait(2)
        self.play(FadeOut(c, c_6, divider))
