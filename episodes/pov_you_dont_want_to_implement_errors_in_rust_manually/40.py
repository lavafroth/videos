#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c0 = '''#[derive(Error, Debug)]
pub enum MyError {
    Io(#[from] std::io::Error),
    // ...
}'''
        c0 = Code(code=c0, language='rust', insert_line_no=False, font_size=38)[2]

        c1 = '''#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[source]
        io: std::io::Error,
        #[source]
        parse: std::string::ParseError,
    },
    // ...
}'''
        c1 = Code(code=c1, language='rust', insert_line_no=False, font_size=38)[2]

        self.play(
            Transform(c0[:2], c1[:2]),
            Transform(c0[-2:], c1[-2:]),
            Transform(c0[2][:6], c1[2][:6]),
            Transform(c0[2][6], c1[2][6]),
            Transform(c0[2][7:-2], c1[3:7]),
            Transform(c0[2][-1], c1[7][-1]),
            Transform(c0[2][-2], c1[7][-2]),
        )
        self.wait(2)
