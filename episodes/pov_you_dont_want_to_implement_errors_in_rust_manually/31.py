#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c_0 = """#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    #[error("failed to read config")]
    Io(std::io::Error),
    // ...
}
"""
        c_0 = Code(code=c_0, language="rust", font_size=38, insert_line_no=False)[2]
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
        c_1 = Code(code=c_1, language="rust", font_size=38, insert_line_no=False)[2]
        self.add(c_0)
        crib = len("    Io(")
        crib_1 = len("std::io::Error),")
        self.play(
            Transform(c_0[7][:crib], c_1[7][:crib]),
            Transform(c_0[7][-crib_1:], c_1[7][-crib_1:]),
            Write(c_1[7][crib:-crib_1]),
        )
        c_0.add(c_1[7][crib:-crib_1])
        self.wait(2)

        com = octicon("gear-24", fill_color=WHITE).scale(0.3)
        com1 = (
            octicon("gear-16", fill_color=WHITE).scale(0.3 * 16 / 24).shift(0.35 * DR)
        )
        cogs = Group(com, com1).shift(4 * RIGHT)
        cogs.scale(1.5)

        a = Arrow(c_0.get_edge_center(RIGHT) + 6 * LEFT, c_0.get_edge_center(RIGHT) + 3 * LEFT)
        self.play(c_0.animate.shift(6 * LEFT), Create(a), FadeIn(cogs))
        self.play(
            Rotate(com, angle=0.5 * PI, about_point=com.get_center()),
            Rotate(com1, angle=1.5 * PI, about_point=com1.get_center()),
        )
        c_2 = """impl From<std::io::Error> for ParseError {
    fn from(source: std::io::Error) -> Self {
        // ...
    }
}"""
        c_2 = Code(code=c_2, language="rust", font_size=38, insert_line_no=False)[2].shift(13 * RIGHT)
        a_ = Arrow(cogs.get_edge_center(RIGHT), cogs.get_edge_center(RIGHT) + 3 * RIGHT)
        self.play(Create(a_))
        self.play(Group(c_0, cogs, a, a_).animate.shift(13 * LEFT), c_2.animate.shift(13 * LEFT))
        self.wait(1)
        self.play(FadeOut(a_))
        self.wait(1)
        self.play(c_2.animate.shift(8 * UP))
