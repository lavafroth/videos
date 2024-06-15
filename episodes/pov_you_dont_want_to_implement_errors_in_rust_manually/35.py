#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c_1 = """#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    #[error("failed to read config")]
    Io(#[from] std::io::Error),
    // ...
}
"""
        c_2 = """#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    #[error(transparent)]
    Io(#[from] std::io::Error),
    // ...
}
"""
        c_1 = Code(code=c_1, language="rust", font_size=38, insert_line_no=False)[2]
        c_2 = Code(code=c_2, language="rust", font_size=38, insert_line_no=False)[2]
        self.add(c_1)
        before_target = c_1[:6]
        after_target = c_1[-2:]
        chunks3 = lambda obj, x, y: (obj[:x], obj[x:y], obj[y:])

        e_1 = chunks3(c_1[6], 12, -2)
        e_2 = chunks3(c_2[6], 12, -2)
        self.play(before_target.animate.set_opacity(0.5), after_target.animate.set_opacity(0.5))
        self.play(Transform(a, b) for a, b in zip(e_1, e_2))
        self.wait(1)
        self.play(before_target.animate.set_opacity(1), after_target.animate.set_opacity(1))
        self.wait(2)

