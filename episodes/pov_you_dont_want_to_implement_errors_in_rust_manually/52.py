#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c1 = """use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    #[error("failed to read config")]
    Io {
        #[backtrace]
        #[from]
        inner: std::io::Error,
    },
    // ...
}
"""
        c1 = Code(code=c1, language="rust", font_size=32, insert_line_no=False)[2]
        self.add(c1)
        mye = Circle(color=WHITE, fill_color=WHITE, radius=1.2).shift(3 * LEFT)
        myet = Text("MyError", font=codefont, font_size=32).next_to(mye, UP)

        chunks3 = lambda obj, x, y: (obj[:x], obj[x:y], obj[y:])
        pubenum, myerr, brace = chunks3(c1[3], 9, -2)

        smol = Circle(color=YELLOW, fill_color=YELLOW).move_to(mye)
        smolt = Text("io::Error", font=codefont, font_size=32, color=YELLOW).move_to(
            smol
        )
        inner, ioerr, comma = chunks3(c1[8], 20, -1)

        self.play(
            Create(mye),
            ReplacementTransform(myerr, myet),
            FadeOut(pubenum, brace),
            Create(smol),
            ReplacementTransform(ioerr, smolt),
            FadeOut(inner, comma),
            FadeOut(c1[:3], c1[4:8], c1[-3:])
        )

        mye_ = Circle(color=WHITE, fill_color=WHITE).move_to(mye).shift(UP)

        self.play(
            smol.animate.shift(2 * DOWN),
            Transform(mye, mye_),
            myet.animate.shift(UP),
            smolt.animate.shift(2 * DOWN),
        )

        prov = (
            Text("provide(...)", font=codefont, font_size=32)
            .next_to(mye, buff=1)
            .set_z_index(1)
        )
        prov_surr = SurroundingRectangle(
            prov, color=BLUE, fill_color=BLUE, fill_opacity=0.3, corner_radius=0.2
        ).set_z_index(0)

        prov_1 = (
            Text("provide(...)", font=codefont, font_size=32)
            .next_to(smol, buff=1)
            .set_z_index(1)
        )
        prov_1_surr = SurroundingRectangle(
            prov_1, color=BLUE, fill_color=BLUE, fill_opacity=0.3, corner_radius=0.2
        ).set_z_index(0)
        

        trace = Text("Backtrace", font=codefont, font_size=32).next_to(prov_1, buff=1)
        trace_surr = SurroundingRectangle(trace, color=TEAL_D, fill_color=TEAL_D, fill_opacity=.3, corner_radius=0.05).set_z_index(0)

        lines = [
            DashedLine(mye.get_edge_center(RIGHT), prov_surr.get_edge_center(LEFT)),
            DashedLine(smol.get_edge_center(RIGHT), prov_1_surr.get_edge_center(LEFT)),
            DashedLine(prov_1_surr.get_edge_center(RIGHT), trace_surr.get_edge_center(LEFT)),
        ]

        self.play(
            Create(prov_surr),
            Write(prov),
            Create(prov_1_surr),
            Write(prov_1),
            Create(lines[0]),
            Create(lines[1]),
        )

        self.play(
            Create(trace_surr), Write(trace), Create(lines[2])
        )
        self.wait(2)

        prov_2 = (
            Text("provide(...)", font=codefont, font_size=32)
            .set_z_index(1)
        )
        prov_2_surr = SurroundingRectangle(
            prov_2, color=BLUE, fill_color=BLUE, fill_opacity=0.3, corner_radius=0.2
        ).set_z_index(0)

        trace_ = Text("Backtrace", font=codefont, font_size=32).next_to(prov_2, buff=1)
        trace_surr_ = SurroundingRectangle(trace_, color=TEAL_D, fill_color=TEAL_D, fill_opacity=.3, corner_radius=0.05).set_z_index(0)

        new_lines = [
            DashedLine(mye.get_edge_center(RIGHT), prov_2_surr.get_edge_center(LEFT)),
            DashedLine(smol.get_edge_center(RIGHT), prov_2_surr.get_edge_center(LEFT)),
            DashedLine(prov_2_surr.get_edge_center(RIGHT), trace_surr_.get_edge_center(LEFT)),
        ]
        
        self.play(
            Transform(prov, prov_2),
            Transform(prov_1, prov_2),
            Transform(prov_surr, prov_2_surr),
            Transform(prov_1_surr, prov_2_surr),
            Transform(trace, trace_),
            Transform(trace_surr, trace_surr_),
            *(Transform(a, b) for a, b in zip(lines, new_lines))
        )
        self.wait(8)
