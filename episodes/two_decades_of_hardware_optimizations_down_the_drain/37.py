#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        scaling_factor = 1.2
        squares = VGroup(
            *[
                Square(1, color=BLUE, fill_color=BLUE, fill_opacity=0.4).shift(
                    2 * scaling_factor * UP + i * scaling_factor * DOWN + 4 * LEFT
                )
                for i in range(4)
            ]
        )

        comp_squares = squares.copy().shift(2.5 * RIGHT)
        anims = list(map(FadeIn, squares))
        anims.extend(map(FadeIn, comp_squares))
        anims = AnimationGroup(
            anims,
            lag_ratio=0.3
        )
        self.play(anims)

        simd_squares = Rectangle(width=1, height=4, grid_ystep=1, fill_opacity=0.4, fill_color=WHITE, color=WHITE).shift(1.5 * RIGHT + .5 * UP)
        comp_simd_squares = simd_squares.copy().shift(2.5 * RIGHT)
        regular = Group(squares, comp_squares)
        simd = Group(simd_squares, comp_simd_squares)
        self.play(Create(simd_squares))
        self.play(Create(comp_simd_squares))
        reg = Text('Regular\ninstructions').move_to(regular.get_edge_center(DOWN) + DOWN)
        sim = Text('SIMD').move_to(simd.get_edge_center(DOWN) + DOWN)
        self.play(map(FadeIn, (reg, sim)))
        for a, b in zip(squares, comp_squares):
            self.play(a.animate.shift(2.5/2 * RIGHT), b.animate.shift(2.5/2 * LEFT), run_time=0.6)

        self.play(simd_squares.animate.shift(2.5/2 * RIGHT), comp_simd_squares.animate.shift(2.5/2 * LEFT))
        self.wait(3)
        everything = Group(regular, simd, reg, sim)
        self.play(everything.animate.shift(6 * UP).fade(1))

        with open('assets/codes/portable_simd.glow') as handle:
            contents = handle.read()
        portable_simd_ = Text(contents, font_size=24).shift(UP)
        portable_simd = portable_simd_.copy().set_opacity(0).shift(6 * DOWN)

        self.play(Transform(portable_simd, portable_simd_))
        surr = Rectangle(color=BLUE, width=12, height=0.6).to_edge(DL).shift(0.16 * DOWN)
        self.play(Create(surr))
        self.wait(3)
        box = octicon('device-desktop-24', fill_color=WHITE).scale(0.6)
        tw = Text('Since 1999').shift(DOWN)
        self.play(
            Transform(portable_simd, box),
            Transform(surr, tw),
        )
        self.wait(4)
