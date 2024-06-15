#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        main = '''fn main() -> Result<(), ParseError> {
    let contents = std::fs::read_to_string("config.txt")?;
    let output = std::fs::OpenOptions::new()
        .create(true)
        .write(true)
        .open("output_objects")?;
    Ok(())
}
'''
        main = Code(code=main, language='rust', insert_line_no=False, font_size=32)[2].shift(8 * DOWN)

        c_2 = """#[derive(Error, Debug)]
pub enum ParseError {
    #[error("found unexpected character: {val}")]
    NonAscii{val: char},
    #[error("can't load over {} objects", i64::MAX)]
    TooManyObjects,
    #[error(transparent)]
    Io(#[from] std::io::Error),
    // ...
}
"""
        c_2 = Code(code=c_2, language="rust", font_size=38, insert_line_no=False)[2]

        self.add(c_2)
        self.play(x.animate.shift(8 * UP) for x in (c_2, main))
        self.wait(1)
        self.play(main.animate.shift(2 * UP))
        er = """Error: Io(Os {
    code: 2, 
    kind: NotFound, 
    message: "No such file or directory"
})"""

        er = Code(code=er, language="html", font_size=32, insert_line_no=False, background="window").to_edge(DOWN).shift(.2 * DOWN)
        t = Text("Output", font_size=32).next_to(er, direction=UP).shift(3.5 * LEFT)
        self.play(FadeIn(er[0]), Write(er[2]), FadeIn(t))
        self.wait(4)
        self.play(FadeOut(er,t,main))

