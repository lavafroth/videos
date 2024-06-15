#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        t = Text("cargo-expand", font=codefont, font_size=50)
        self.play(FadeIn(t))
        self.wait(2)
        c_2 = """cargo install cargo-expand
cargo expand --lib"""
        c_3 = """cargo install cargo-expand
cargo expand --bin mycrate"""
        c_2 = Code(code=c_2, language="bash", font_size=40, insert_line_no=False)[2]
        c_3 = Code(code=c_3, language="bash", font_size=40, insert_line_no=False)[2]
        self.play(
            Write(c_2[0][: len("cargo install ")]),
            ReplacementTransform(t, c_2[0][len("cargo install ") :]),
        )
        self.wait(2)
        self.play(Write(c_2[1]))
        lel = c_2[1][15:]
        lul = lel.copy()
        self.play(Transform(lel, c_3[1][15:]))
        self.wait(2)
        self.play(Transform(lel, lul))
        self.wait(2)

        rep = '''#[allow(unused_qualifications)]
impl ::core::convert::From<std::io::Error> for ParseError {
    #[allow(deprecated)]
    fn from(source: std::io::Error) -> Self {
        ParseError::Io { 0: source }
    }
}
'''
        rep = Code(code=rep, language="rust", font_size=30, insert_line_no=False)[2].shift(8 * DOWN)
        self.play(c_2.animate.shift(8 * UP), rep.animate.shift(8 * UP))
        self.wait(2)
