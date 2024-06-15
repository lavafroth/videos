#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')

        bt = Text("backtrace", font=codefont, font_size=40, color=WHITE)
        self.add(bt)
        bt_ = Text("RUST_BACKTRACE=1", font=codefont, font_size=34, color=WHITE).shift(2 * DOWN)
        bt__ = Text("RUST_BACKTRACE=1", font=codefont, font_size=34, color=WHITE).shift(2.5 * DOWN).set_opacity(0)
        self.play(ReplacementTransform(bt__, bt_))
        self.wait(2)
        self.play(FadeOut(bt_))
        co = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to read config")]
    Io {
        #[backtrace]
        trace: MyCustomBacktrace,
    },
    // ...
}
'''
        code = Code(code=co, language='rust', font_size=32, insert_line_no=False)[2]
        self.play(FadeIn(code[:6], code[7:]), Transform(bt, code[6][10:-1]))
        writes = (code[6][8:10], code[6][-1])
        self.play(map(Write, writes))
        self.wait(2)
