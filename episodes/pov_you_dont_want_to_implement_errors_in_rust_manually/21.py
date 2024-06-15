#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        c_2 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error()]
    Permission,
    Timeout,
}
'''
        c_3 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to create unix socket")]
    Permission,
    Timeout,
}
'''
        c_2 = Code(code=c_2, language='rust', font_size=40)[2]
        c_3 = Code(code=c_3, language='rust', font_size=40)[2]
        anims = AnimationGroup(
            Transform(c_2[:4], c_3[:4]),
            Transform(c_2[4][:len('    #[error(')], c_3[4][:len('    #[error(')]),
            Transform(c_2[4][-2:], c_3[4][-2:]),
            Transform(c_2[5:], c_3[5:]),
            Write(c_3[4][len('    #[error('):-2]),
        )
        self.play(anims)
