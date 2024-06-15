#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        t = Text('std::io::Result', font=codefont)
        self.play(Write(t))
        main = '''fn main() -> Result<(), ParseError> {
    let contents = std::fs::read_to_string("config.txt")?;
    let output = std::fs::OpenOptions::new()
        .create(true)
        .write(true)
        .open("output_objects")?;
    Ok(())
}
'''
        main = Code(code=main, language='rust', insert_line_no=False, font_size=32)[2]
        self.play(ReplacementTransform(t, main))
        box=Rectangle(color=BLUE, height=main[2:6].height - 0.1, width=main[0][0].width * 49).shift(1 * LEFT)
        b = Rectangle(color=BLUE, height=main[1].height - .15, width=main[1].width + .2).shift(1.65 * UP * main[1].height + .4 * RIGHT)
        self.play(Create(box))
        self.wait(2)
        self.play(Transform(box, b))
        er = '''error[E0277]: the trait `From<std::io::Error>` is not implemented for
`ParseError`, which is required by `Result<(), ParseError>:
FromResidual<Result<Infallible, std::io::Error>>`'''
        er = Paragraph(er, t2c={'error[E0277]': RED}, font=codefont, font_size=28).to_edge(DOWN).shift(.3 * DOWN)
        self.play(Write(er))
        self.play(FadeOut(box))
        self.play(main.animate.shift(8 * DOWN).set_opacity(0))
