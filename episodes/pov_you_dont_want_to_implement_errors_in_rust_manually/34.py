#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        rep = """#[allow(unused_qualifications)]
impl ::core::convert::From<std::io::Error> for ParseError {
    #[allow(deprecated)]
    fn from(source: std::io::Error) -> Self {
        ParseError::Io { 0: source }
    }
}
"""
        rep = Code(code=rep, language="rust", font_size=30, insert_line_no=False)[2]
        self.add(rep)
        ripple = rep[1][len("impl ") : len("impl ::core::convert::From")]
        anims = []
        curve = ParametricFunction(
            lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]
        )
        for char in ripple:
            curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=1.5)
        self.play(rep.animate.shift(UP))
        t = Text("Implicitly included as ", font_size=32).to_edge(DOWN).shift(2 * UP)
        crib = 18
        back_crib = 7
        oneline = lambda src: Code(code=src, language="rust", font_size=38)[2][0].next_to(t, direction=DOWN)
        code = oneline("use std::prelude::v1::From;")
        code_1 = oneline("use std::prelude::rust_2015::From;")
        code_2 = oneline("use std::prelude::rust_2018::From;")
        code_3 = oneline("use std::prelude::rust_2021::From;")
        self.play(FadeIn(t))
        self.play(Write(code))
        chunks = lambda cowd: (cowd[:crib], cowd[crib:-back_crib], cowd[-back_crib:])
        chunks_0 = chunks(code)
        chunks_1 = chunks(code_1)
        chunks_2 = chunks(code_2)
        chunks_3 = chunks(code_3)
        self.wait(1)
        self.play(Transform(a, b) for a, b in zip(chunks_0, chunks_1))
        self.wait(1)
        self.play(Transform(a, b) for a, b in zip(chunks_0, chunks_2))
        self.wait(1)
        self.play(Transform(a, b) for a, b in zip(chunks_0, chunks_3))
        self.wait(2)
        self.play(FadeOut(*chunks_0, t), rep.animate.shift(DOWN))
        self.wait(1)
        ripple = rep[4]
        anims = []
        curve = ParametricFunction(
            lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]
        )
        for char in ripple:
            curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=2)
        lop = len('    fn from(')
        lup = len('        ParseError::Io { 0: ')
        cl = rep[3][lop:lop+6].copy()
        dl = rep[4][lup:lup+6]
        self.wait(1)
        self.play(Transform(cl, dl))
        self.play(FadeOut(cl))
        self.play(FadeOut(rep))
