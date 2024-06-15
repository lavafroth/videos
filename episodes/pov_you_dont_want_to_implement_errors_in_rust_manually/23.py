#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        c_3 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to create unix socket")]
    Permission,
    #[error("timed out receiving request")]
    Timeout,
}
'''
        c_3 = Code(code=c_3, language='rust', font_size=40)[2]
        self.add(c_3)
        c_4 = '''#[derive(Error, Debug)]
pub enum ParseError {
    NonAscii,
    // ...
}
'''
        c_4 = Code(code=c_4, language='rust', font_size=38)[2].shift(8 * DOWN)
        self.play(c_3.animate.shift(8 * UP), c_4.animate.shift(8 * UP))
        self.wait(4)
        anims = []
        curve = ParametricFunction(lambda t: np.array([0, 0.2 * np.sin(PI * t), 0]), t_range=[0, 1])
        for char in c_4[2][:-1]:
            curve = curve.copy().move_to(char.get_center() + 0.1 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=.1))
        self.wait(2)
