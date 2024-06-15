#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        code = Code('test_inert.rs', font_size=32)[2]
        self.add(code)
        code_ = Code('test_inert.rs')[2].to_edge(LEFT)
        self.play(ReplacementTransform(code, code_))
        scale = 1.5
        l = Line(start= scale * UP, end= scale * DOWN).shift(.5 * LEFT)
        self.play(Create(l))
        output = '''cargo test
   Compiling demo v0.1.0 (/tmp/demo)
    Finished test target(s) in 0.46s
     Running unittests src/lib.rs
     (target/debug/deps/demo-2d39e92491b0e5b3)

running 1 test
test tests::test_dijkstra_correctness ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s'''
        output = Paragraph(output, font_size=24, font=codefont, t2c={'Compiling': GREEN, 'Finished': GREEN, 'Running': GREEN, 'ok': GREEN}).shift(6.9 * RIGHT)
        self.play(Write(output[0]))
        w = Text('inert').to_edge(DOWN)
        self.play(Write(output[1:]), FadeIn(w))
        self.wait(2)
        self.play(FadeOut(output), FadeOut(w))
        output = '''cargo b --release
Compiling demo v0.1.0 (/tmp/demo)
 Finished release [optimized] target(s) in 0.37s'''
        output = Paragraph(output, font_size=24, font=codefont, t2c={'Compiling': GREEN, 'Finished': GREEN, 'Running': GREEN, 'ok': GREEN}).shift(3.25 * RIGHT)
        self.play(Write(output[0]))
        test_fn = code_[2:-1]
        rest_up = code_[:2]
        rest_down = code_[-1]
        scale = .75
        w = Text('active').to_edge(DOWN)
        l_ = Line(UP, DOWN).shift(.5 * LEFT)
        self.play(FadeOut(test_fn), rest_up.animate.shift(scale * DOWN), rest_down.animate.shift(scale * UP), Write(w), Transform(l, l_))
        self.play(Write(output[1:]))
        self.wait(2)
        self.play(FadeOut(rest_up, rest_down, output, l))
        self.wait(1)
