#!/usr/bin/env manim
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from custom import octicon

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')

        bench = Text('#[bench]', font="Terminess Nerd Font Propo")
        self.play(Write(bench))
        line = Line(5 * UP, 5 * DOWN).shift(2.5 * LEFT)
        rustup = Text('rustup toolchain install nightly', font="Terminess Nerd Font Propo", font_size=24).to_edge(UP).shift(.25 * UP + .2 * RIGHT)
        self.play(bench.animate.shift(5 * LEFT), Create(line), Write(rustup))
        _or = Text('or a flake.nix devshell', font_size=22, color=GRAY_A).to_edge(UP).shift(.2 * DOWN + .6 * LEFT)
        flake = Code('flake.nix', font_size=22)[2].to_edge(RIGHT).shift(.5 * DOWN)
        self.play(FadeIn(_or))
        self.play(FadeIn(flake))

        self.wait(1)
        self.play(FadeOut(x) for x in (flake, _or, rustup, line))
        bcode = Code('benchmark_snippet.rs', style='monokai', font_size=34)[2]
        self.play(Transform(bench, bcode[0]), FadeIn(bcode[1:]))
        self.wait(1)
        group = []
        init_call = bcode[2][17:21]
        init_call_copy = init_call.copy()
        for i, line in enumerate(bcode):
            if i == 2:
                group.extend(line[:17])
                group.extend(line[21:])
                continue
            group.extend(line[:])
        group.extend(bench[:])
        group = VGroup(*group)
        group_copy = group.copy()
        _group = group.copy().shift(10 * DOWN).set_opacity(0)

        binit = Code('benchmark_init.rs', font_size=24)[2].to_edge(LEFT)
        init_def = binit[0][3:7]

        group_1 = []
        for i, line in enumerate(binit):
            if i == 0:
                group_1.extend(line[:3])
                group_1.extend(line[7:])
                continue
            group_1.extend(line[:])
        group_1 = VGroup(*group_1)
        _group_1 = group_1.copy().shift(10 * UP).set_opacity(0)
        group_1_copy = _group_1.copy()

        self.play(
            Transform(init_call, init_def),
            Transform(_group_1, group_1),
            Transform(group, _group)
        )

        shapes = [
            Rectangle(width=2, height=1,color=PURPLE, fill_color=PURPLE, fill_opacity=0.6),
            Square(1, color=BLUE, fill_color=BLUE, fill_opacity=0.6),
            Circle(radius=0.5, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.6),
            Triangle(radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=0.6),
        ]

        anims = []
        for i, shape in enumerate(shapes):
            shape.to_edge(RIGHT).shift(i * 0.3 * DL + 0.5 * LEFT)
            anims.append(Create(shape))

        self.play(*anims)

        anims = []
        for shape in shapes:
            anims.append(shape.animate.shift(10 * UP).set_opacity(0))

        self.play(
            Transform(init_call, init_call_copy),
            Transform(_group_1, group_1_copy),
            Transform(group, group_copy),
            *anims,
        )

        self.wait(1)
