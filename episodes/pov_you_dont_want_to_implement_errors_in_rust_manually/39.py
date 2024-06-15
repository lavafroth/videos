#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        main = '''#[derive(Error, Debug)]
pub enum MyError {
    Io(#[from] std::io::Error),
    // ...
}'''
        main = Code(code=main, language='rust', insert_line_no=False, font_size=38)[2]
        self.play(FadeIn(main))

        c_2 = """#[derive(Error, Debug)]
pub enum MyError {
    Io(#[from] #[source] std::io::Error),
    // ...
}
"""
        c_2 = Code(code=c_2, language="rust", font_size=38, insert_line_no=False)[2]

        self.play(
            Transform(main[:2], c_2[:2]),
            Transform(main[2][:15], c_2[2][:15]),
            Transform(main[2][-17:], c_2[2][-17:]),
            Transform(main[-2:], c_2[-2:]),
        )
        a = c_2[2][15:-17]
        a.set_opacity(.5)
        i = Text('implicit', font_size=32).shift(2 * DOWN + 3 * RIGHT)
        self.play(Write(a))
        r = CurvedArrow(i.get_edge_center(LEFT) + .1 * LEFT, a.get_edge_center(DOWN) + .1 * DOWN, angle=-PI/4)
        self.play(Write(i), Create(r))
        self.wait(3)
        self.play(FadeOut(i, r, a))

        c_2 = '''#[derive(Error, Debug)]
pub enum MyError {
    Io(#[from] std::io::Error),
    // ...
}'''
        c_2 = Code(code=c_2, language='rust', insert_line_no=False, font_size=38)[2]

        self.play(
            Transform(main[:2], c_2[:2]),
            Transform(main[2][:15], c_2[2][:15]),
            Transform(main[2][-17:], c_2[2][-17:]),
            Transform(main[-2:], c_2[-2:]),
        )
