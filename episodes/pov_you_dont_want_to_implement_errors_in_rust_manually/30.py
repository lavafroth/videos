#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"
class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        er = '''error[E0277]: the trait `From<std::io::Error>` is not implemented for
`ParseError`, which is required by `Result<(), ParseError>:
FromResidual<Result<Infallible, std::io::Error>>`'''
        er = Paragraph(er, t2c={'error[E0277]': RED}, font=codefont, font_size=28).to_edge(DOWN).shift(.3 * DOWN)
        self.add(er)

        c_6 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    // ...
}
'''
        c_6 = Code(code=c_6, language='rust', font_size=38, insert_line_no=False)[2].shift(8 * UP).set_opacity(0)
        c_7 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    #[error("failed to read config")]
    Io,
    // ...
}
'''
        c_7 = Code(code=c_7, language='rust', font_size=38, insert_line_no=False)[2]
        self.play(c_6.animate.shift(8 * DOWN).set_opacity(1))
        self.wait(2)
        self.play(
            ReplacementTransform(c_6[:6], c_7[:6]),
            ReplacementTransform(c_6[-2:], c_7[-2:]),
            Write(c_7[-4:-2])
        )
        self.wait(2)
        c_8 = '''#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    #[error("failed to read config")]
    Io(std::io::Error),
    // ...
}
'''
        c_8 = Code(code=c_8, language='rust', font_size=38, insert_line_no=False)[2]
        crib = len('error[E0277]: the trait `From<')-3
        l, o, r = er[0][:crib], er[0][crib:crib+14], er[0][crib+14:] + er[1:]
        self.play(
            ReplacementTransform(c_7[:7], c_8[:7]),
            ReplacementTransform(c_7[-2:], c_8[-2:]),
            ReplacementTransform(c_7[-3][:len('    Io')], c_8[-3][:len('    Io')]),
            Write(c_8[-3][len('    Io')]),
            Write(c_8[-3][-2]),
            ReplacementTransform(o, c_8[-3][len('    Io('):-2]),
            ReplacementTransform(c_7[-3][-1:], c_8[-3][-1:]),
            FadeOut(l, r)
        )
        self.wait(2)
        
