#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        c_1 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    Permission,
    Timeout,
}
'''
        c_2 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error()]
    Permission,
    Timeout,
}
'''
        c_1 = Code(code=c_1, language='rust', font_size=40)
        c_2 = Code(code=c_2, language='rust', font_size=40)
        tfmr = CodeTransformer(c_1)
        tfmr.ingest(c_2)
        self.add(*tfmr.writables())
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        self.wait(2)
