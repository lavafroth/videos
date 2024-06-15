#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c3 = """#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[source]
        io: std::io::Error,
        #[from]
        parse: std::string::ParseError,
    },
    // ...
}"""
        c3 = Code(code=c3, language="rust", insert_line_no=False, font_size=38)[
            2
        ].set_opacity(0.5)

        c4 = """#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[error("failed to read config")]
        source: std::io::Error,
    },
    // ...
}"""
        c4 = Code(code=c4, language="rust", insert_line_no=False, font_size=38)[2]

        for line in c3[5:7]:
            line.set(color=RED)
            line.set_opacity(1)

        self.add(c3)
        self.play(
            Transform(c3[:3], c4[:3]),
            Transform(c3[-3:], c4[-3:]),
            FadeOut(c3[5:7], c3[3]),
            Transform(c3[4][10:], c4[4][14:]),
            Transform(c3[4][:10], c4[4][:14]),
            Write(c4[3])
        )
        self.wait(2)
