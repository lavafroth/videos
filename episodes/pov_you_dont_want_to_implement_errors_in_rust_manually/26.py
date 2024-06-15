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
    #[error("found unexpected character: {0}")]
    NonAscii(char),
    // ...
}
'''
        c_6 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {0:?}")]
    NonAscii(char),
    // ...
}
'''
        c_5 = Code(code=c_5, language='rust', font_size=38, insert_line_no=False)[2]
        c_6 = Code(code=c_6, language='rust', font_size=38, insert_line_no=False)[2]
        self.add(c_5)
        t = Text('.0th member', font_size=40).shift(1.5 * DOWN + 2 * RIGHT)
        a = CurvedArrow(t.get_edge_center(LEFT) + .1 * LEFT, c_5[3][-4].get_edge_center(DOWN) + .1 * DOWN, angle=-PI/4)
        _a = CurvedArrow(t.get_edge_center(RIGHT) + .1 * RIGHT, c_5[2][-5].get_edge_center(DOWN) + .1 * DOWN, angle=PI/4)
        anims = []
        curve = ParametricFunction(lambda t: np.array([0, 0.2 * np.sin(PI * t), 0]), t_range=[0, 1])
        for char in c_5[3][-6:-2]:
            curve = curve.copy().move_to(char.get_center() + 0.1 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=.1))

        self.play(Create(a), FadeIn(t))
        self.play(Create(_a))

        anims = []
        curve = ParametricFunction(lambda t: np.array([0, 0.2 * np.sin(PI * t), 0]), t_range=[0, 1])
        for char in c_5[2][-6:-3]:
            curve = curve.copy().move_to(char.get_center() + 0.1 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=.1))

        self.wait(2)
        crib = len('    #[error("found unexpected character: {0')
        t_ = Text('debug formatted', font_size=40).next_to(t, direction=DOWN)
        self.play(
            ReplacementTransform(c_5[:2], c_6[:2]),
            ReplacementTransform(c_5[2][:crib], c_6[2][:crib]),
            ReplacementTransform(c_5[2][-4:], c_6[2][-4:]),
            ReplacementTransform(c_5[3:], c_6[3:]),
            Write(c_6[2][crib:-4]),
            FadeIn(t_)
        )
        self.wait(6)
