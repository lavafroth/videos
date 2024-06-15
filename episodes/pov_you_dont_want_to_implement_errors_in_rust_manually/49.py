#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c0 = """use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to read config")]
    Io {
        #[backtrace]
        trace: MyCustomBacktrace,
    },
    // ...
}
"""
        c1 = """use std::backtrace::Backtrace;
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
        c0 = Code(code=c0, language="rust", font_size=32, insert_line_no=False)[2]
        c1 = Code(code=c1, language="rust", font_size=32, insert_line_no=False)[2]
        self.add(c0)
        self.play(
            Write(c1[0]),
            Transform(c0[:6], c1[1:7]),
            Transform(c0[-3:], c1[-3:]),
            Transform(c0[-4][:15], c1[-4][:15]),
            FadeOut(c0[-4][15:-1]),
            Transform(c0[6][10:-1], c1[-4][15:-1]),
            FadeOut(c0[6][:10], c0[6][-1]),
            Transform(c0[-4][-1], c1[-4][-1]),
        )
        self.wait(2)
