#!/usr/bin/env manim
from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from custom import CodeTransformer, octicon


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        loop = Code("pdf_loop.c", font_size=22)[2].to_edge(LEFT).shift(UP)
        hide = [loop[:29], loop[30:]]

        for x in hide:
            x.set_opacity(0.5)

        self.add(loop)

        group_offt = 5 * RIGHT
        xmm3 = VGroup(
            *[
                Square(0.5, fill_color=GREEN, fill_opacity=0.8, color=GREEN).shift(
                    4 * RIGHT + 0.5 * DOWN * x + 2 * UP
                )
                for x in range(4)
            ]
        )

        xmm3_label = Text(
            "xmm3", font="Terminess Nerd Font Propo", font_size=22
        ).move_to(xmm3[3].get_edge_center(DOWN) + 0.5 * DOWN)

        self.add(xmm3, xmm3_label)
        self.play(xmm3.animate.shift(1.5 * LEFT), xmm3_label.animate.shift(1.5 * LEFT))

        accums = [
            Text("accum{}".format(x), font="Terminess Nerd Font Propo", font_size=28).shift(
                DOWN + x * 0.5 * DOWN + 4 * RIGHT
            )
            for x in range(1, 5)
        ]

        self.play(map(Write, accums))

        xmm0 = VGroup(
            *[
                Square(0.5, fill_color=WHITE, fill_opacity=0.5, color=WHITE).shift(
                    4 * RIGHT + 0.5 * DOWN * x + 2 * UP
                )
                for x in range(4)
            ]
        )

        self.play(Transform(a, b) for a, b in zip(accums, xmm0))

        xmm0 = VGroup(*accums)
        
        xmm0_label = Text(
            "xmm0", font="Terminess Nerd Font Propo", font_size=22
        ).move_to(xmm0[3].get_edge_center(DOWN) + 0.5 * DOWN)

        self.play(Write(xmm0_label))
        mulps_inst = loop[30]
        mulps = mulps_inst[-len("mulps xmm3, xmm5") :]
        self.play(
            loop[:30].animate.set_opacity(0.5),
            loop[31:].animate.set_opacity(0.5),
            mulps_inst.animate.set_opacity(1),
        )
        self.wait(1)
        mul = Tex("+")[0].move_to(xmm3.get_edge_center(RIGHT) + 0.5 * RIGHT)
        mulps_copy = mulps.copy()
        self.play(
            mulps.animate.move_to(
                xmm3[0].get_edge_center(UP) + 0.8 * RIGHT + 0.5 * UP
            ).scale(1.5),
            FadeIn(mul),
        )
        self.wait(3)
        xmm3_ = VGroup(
            *[
                Square(0.5, fill_color=WHITE, fill_opacity=0.4, color=WHITE).shift(
                    4 * RIGHT + 0.5 * DOWN * x + 2 * UP
                )
                for x in range(4)
            ]
        )
        self.play(
            Transform(xmm3, xmm3_),
            Transform(xmm3_label, xmm0_label),
            Transform(xmm0, xmm3_),
            FadeOut(mul),
        )
        self.wait(1)
        self.play(Transform(mulps, mulps_copy))
        self.play(FadeOut(loop, xmm3, xmm0, xmm3_label, xmm0_label))
