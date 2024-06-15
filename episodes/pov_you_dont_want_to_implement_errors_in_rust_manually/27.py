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
    #[error("found unexpected character: {0:?}")]
    NonAscii(char),
    // ...
}
'''
        c_6 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    // ...
}
'''
        c_5 = Code(code=c_5, language='rust', font_size=38, insert_line_no=False)[2]
        c_6 = Code(code=c_6, language='rust', font_size=38, insert_line_no=False)[2]
        self.add(c_5)
        t = Text('.0th member', font_size=40).shift(1.5 * DOWN + 2 * RIGHT)
        t_ = Text('debug formatted', font_size=40).next_to(t, direction=DOWN)
        a = CurvedArrow(t.get_edge_center(LEFT) + .1 * LEFT, c_5[3][-3].get_edge_center(DOWN) + .1 * DOWN, angle=-PI/4)
        _a = CurvedArrow(t.get_edge_center(RIGHT) + .1 * RIGHT, c_5[2][-6].get_edge_center(DOWN) + .1 * DOWN, angle=PI/4)
        self.add(t, t_, a, _a)
        crib = len('    #[error("found unexpected character: {')
        crib_ = len('    NonAscii')
        t__ = Text("named\nmember 'val'", font_size=40).shift(1.5 * DOWN + 2 * RIGHT)
        self.play(
            ReplacementTransform(c_5[3][-1], c_6[3][-1]),
            ReplacementTransform(c_5[3][crib_:-1], c_6[3][crib_:-1]),
            ReplacementTransform(c_5[2][crib:-4], c_6[2][crib:-4]),
            ReplacementTransform(Group(t, t_), t__),
        )
        self.wait(4)
        self.play(FadeOut(t__, a, _a))
