#!/usr/bin/env manim
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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
        curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1])
        anims = []
        for char in nsiter:
            curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=1)
        self.wait(2)
        _nsiter = Text('54,956 ns/iter', font='Terminess Nerd Font Propo')
        self.play(FadeOut(text[:-21]), FadeOut(text[-8:]), Transform(nsiter, _nsiter), FadeOut(line))
        self.wait(2)
        self.play(nsiter.animate.shift(5 * UP).set_opacity(0))
