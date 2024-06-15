#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c0 = """use std::backtrace::Backtrace;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to read config")]
    Io {
        trace: Backtrace,
    },
    // ...
}
"""
        
        c1 = """use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to read config")]
    Io {
        #[backtrace]
        #[source]
        inner: std::io::Error,
    },
    // ...
}
"""
        c2 = c1.replace('source', 'from')
        c0 = Code(code=c0, language="rust", font_size=32, insert_line_no=False)[2]
        c1 = Code(code=c1, language="rust", font_size=32, insert_line_no=False)[2]
        c2 = Code(code=c2, language="rust", font_size=32, insert_line_no=False)[2]
        self.play(FadeIn(c0))
        self.wait(2)
        
        self.play(
            Transform(c0[1:7], c1[:6]),
            FadeOut(c0[0], c0[7]),
            Transform(c0[-3:], c1[-3:]),
            Write(c1[6:9]),
        )
        self.wait(2)
        chunks3 = lambda obj, x, y: (obj[:x], obj[x:y], obj[y:])
        c1c = chunks3(c1[7], 8, -1)
        c2c = chunks3(c2[7], 8, -1)
        self.play(
            Transform(a, b) for a, b in zip(c1c, c2c)
        )
        self.wait(2)
