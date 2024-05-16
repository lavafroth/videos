#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        loop = Code("pdf_loop.c", font_size=22)[2].to_edge(LEFT).shift(UP)
        hide = [loop[:20], loop[24:27], loop[29:]]

        for x in hide:
            x.set_opacity(0.5)

        self.add(loop)

        group_offt = 5 * RIGHT
        xmm3 = VGroup(
            *[
                Square(0.5, fill_color=TEAL_D, fill_opacity=0.8, color=TEAL_D).shift(
                    2.5 * RIGHT + 0.5 * DOWN * x + 2 * UP
                )
                for x in range(4)
            ]
        )

        xmm3_label = Text(
            "xmm3", font="Terminess Nerd Font Propo", font_size=22
        ).move_to(xmm3[3].get_edge_center(DOWN) + 0.5 * DOWN)

        self.add(xmm3, xmm3_label)

        xmm5 = VGroup(
            *[
                Square(0.5, fill_color=YELLOW, fill_opacity=0.5, color=YELLOW).shift(
                    4 * RIGHT + 0.5 * DOWN * x + 2 * UP
                )
                for x in range(4)
            ]
        )
        xmm5_label = Text(
            "xmm5", font="Terminess Nerd Font Propo", font_size=22
        ).move_to(xmm5[3].get_edge_center(DOWN) + 0.5 * DOWN)

        self.add(xmm5, xmm5_label)
        mulps_inst = loop[29]
        mulps = mulps_inst[-len("mulps xmm3, xmm5") :]
        self.play(
            loop[:29].animate.set_opacity(0.5),
            loop[30:].animate.set_opacity(0.5),
            mulps_inst.animate.set_opacity(1),
        )
        self.wait(1)
        mul = Tex(r"$\times$")[0].move_to(xmm3.get_edge_center(RIGHT) + 0.5 * RIGHT)
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
                Square(0.5, fill_color=GREEN, fill_opacity=0.4, color=GREEN).shift(
                    4 * RIGHT + 0.5 * DOWN * x + 2 * UP
                )
                for x in range(4)
            ]
        )
        self.play(
            Transform(xmm3, xmm3_),
            Transform(xmm3_label, xmm5_label),
            Transform(xmm5, xmm3_),
            FadeOut(mul),
        )
        self.wait(1)
        self.play(Transform(mulps, mulps_copy))
        self.wait(1)
