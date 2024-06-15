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
    #[error("failed to create unix socket")]
    Permission,
    Timeout,
}
'''
        c_3 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to create unix socket")]
    Permission,
    #[error("timed out receiving request")]
    Timeout,
}
'''
        c_2 = Code(code=c_2, language='rust', font_size=40)
        c_3 = Code(code=c_3, language='rust', font_size=40)
        tfmr = CodeTransformer(c_2)
        tfmr.ingest(c_3)
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        self.wait(2)
