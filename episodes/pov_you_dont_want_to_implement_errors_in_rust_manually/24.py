#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        c_4 = '''#[derive(Error, Debug)]
pub enum ParseError {
    NonAscii,
    // ...
}
'''
        c_5 = '''#[derive(Error, Debug)]
pub enum ParseError {
    NonAscii(char),
    // ...
}
'''
        c_4 = Code(code=c_4, language='rust', font_size=38)[2]
        c_5 = Code(code=c_5, language='rust', font_size=38)[2]
        self.add(c_4)
        self.play(
            Transform(c_4[:2], c_5[:2]),
            Transform(c_4[3:], c_5[3:]),
            Transform(c_4[2][-1], c_5[2][-1]),
            Write(c_5[2][-7:-1])
        )
