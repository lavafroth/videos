#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        line = Arrow(10 * LEFT, 10 * RIGHT, stroke_width=4)
        self.add(line)
        self.play(line.animate.shift(16 * LEFT))
        text = Text('''Compiling clean_code v0.1.0 (/home/chrs/Workspace/clean_code)
    Finished `bench` profile [optimized] target(s) in 0.58s
     Running unittests src/lib.rs (target/release/deps/clean_code-3affde07f20d1563)

running 1 test
test m01_trait::tests::total_area                  ... bench:      54,956 ns/iter (+/- 280)''',
                t2c={'Compiling':GREEN, 'Finished':GREEN, 'Running': GREEN, '[277:282]': GREEN},
                font_size=24,
                font="Terminess Nerd Font Propo",
            )

        self.play(Write(text))

        nsiter = text[-21:-8]
        self.play(ripple(nsiter), run_time=1)
        self.wait(2)
        _nsiter = Text('54,956 ns/iter', font='Terminess Nerd Font Propo')
        self.play(FadeOut(text[:-21]), FadeOut(text[-8:]), Transform(nsiter, _nsiter), FadeOut(line))
        self.wait(2)
        self.play(nsiter.animate.shift(5 * UP).set_opacity(0))
