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
    NonAscii(char),
    // ...
}
'''
        c_5 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {0}")]
    NonAscii(char),
    // ...
}
'''
        c_4 = Code(code=c_4, language='rust', font_size=38)
        c_5 = Code(code=c_5, language='rust', font_size=38, insert_line_no=False)
        self.add(c_4[2])
        tfmr = CodeTransformer(c_4)
        tfmr.ingest(c_5)
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        self.wait(4)
