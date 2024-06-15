#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c1 = """use std::backtrace::Backtrace;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to read config")]
    Io {
        trace: Backtrace,
    },
    // ...
}
"""
        c1 = Code(code=c1, language="rust", font_size=32, insert_line_no=False)[2]
        self.add(c1)
        mye = Circle(color=WHITE, fill_color=WHITE).shift(3 * LEFT)
        myet = Text("MyError", font=codefont, font_size=32).move_to(mye)

        prov = Text("provide(...)", font=codefont, font_size=32).next_to(mye, buff=1).set_z_index(1)
        prov_surr = SurroundingRectangle(prov, color=BLUE, fill_color=BLUE, fill_opacity=.3, corner_radius=0.2).set_z_index(0)

        trace = Text("trace", font=codefont, font_size=32).next_to(prov, buff=1)
        trace_surr = SurroundingRectangle(trace, color=TEAL_D, fill_color=TEAL_D, fill_opacity=.3, corner_radius=0.05).set_z_index(0)

        chunks3 = lambda obj, x, y: (obj[:x], obj[x:y], obj[y:])
        pubenum, myerr, brace = chunks3(c1[4], 9, -2)
        space, trace_, bt = chunks3(c1[7], 8, 13)
        
        self.play(Create(mye), Transform(myerr, myet), FadeOut(pubenum, brace, space, bt, c1[:4], c1[5:7], c1[8:]),
                  Transform(trace_, trace), Create(prov_surr), Write(prov), Create(trace_surr))
        lines = [
            DashedLine(mye.get_edge_center(RIGHT), prov_surr.get_edge_center(LEFT)),
            DashedLine(prov_surr.get_edge_center(RIGHT), trace_surr.get_edge_center(LEFT)),
        ]
        for line in lines:
            self.play(Create(line), run_time=.5)
        self.wait(4)
        self.play(FadeOut(*lines, mye, prov_surr, trace_surr, myerr, prov, trace_))
