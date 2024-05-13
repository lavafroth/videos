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
        hide = [loop[:26], loop[27:]]

        for chunk in hide:
            chunk.set_opacity(0.5)

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

        self.add(loop, xmm3, xmm3_label)

        show = [loop[20:24], loop[27:29]]
        anims = [loop[26].animate.set_opacity(0.5)]
        anims.extend(map(lambda x: x.animate.set_opacity(1), show))
        self.play(anims)

        self.wait(1)
        shapes = [
            Rectangle(
                width=1, height=0.5, color=PURPLE, fill_color=PURPLE, fill_opacity=0.6
            ),
            Square(0.5, color=BLUE, fill_color=BLUE, fill_opacity=0.6),
            Circle(radius=0.25, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.6),
            Triangle(radius=0.25, color=GREEN, fill_color=GREEN, fill_opacity=0.6),
        ]

        group_offt = 5 * RIGHT

        for i, shape in enumerate(shapes):
            if i == 0:
                offt = 0.95 * LEFT
            else:
                offt = 0.7 * LEFT

            shape.shift(i * 1 * DOWN + offt + group_offt + 2 * UP)

        t = [
            Text(".height", font="Terminess Nerd Font Propo", font_size=22).shift(
                1 * DOWN * i + 0.2 * RIGHT + group_offt + 2 * UP
            )
            for i in range(4)
        ]

        self.play(map(Create, shapes))
        self.play(map(Write, t))

        xmm5 = [
            Square(0.5, fill_color=YELLOW, fill_opacity=0.5, color=YELLOW).shift(
                4 * RIGHT + 0.5 * DOWN * x + 2 * UP
            )
            for x in range(4)
        ]
        xmm5_label = Text("xmm5", font="Terminess Nerd Font Propo", font_size=22).move_to(xmm5[3].get_edge_center(DOWN) + 0.5 * DOWN)


        anims = []
        for mul, shape, xmm5l in zip(t, shapes, xmm5):
            anims.append(Transform(Group(shape, mul), xmm5l))

        self.play(anims)
        self.play(Write(xmm5_label))
        self.wait(2)
