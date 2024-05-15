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
        self.add(loop)

        hide = [loop[:11], loop[20:24], loop[26:]]
        anims = map(lambda x: x.animate.set_opacity(0.5), hide)
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
            Text(".multiplier", font="Terminess Nerd Font Propo", font_size=22).shift(
                1 * DOWN * i + 0.5 * RIGHT + group_offt + 2 * UP
            )
            for i in range(4)
        ]

        self.play(map(Create, shapes))
        self.play(map(Write, t))

        xmm3 = [
            Square(0.5, fill_color=BLUE, fill_opacity=0.5, color=BLUE).shift(
                2.5 * RIGHT + 0.5 * DOWN * x + 2 * UP
            )
            for x in range(4)
        ]
        xmm3_label = Text("xmm3", font="Terminess Nerd Font Propo", font_size=22).move_to(xmm3[3].get_edge_center(DOWN) + 0.5 * DOWN)

        fadeins = []
        anims = []
        for mul, shape, xmm3l in zip(t, shapes, xmm3):
            interim = shape.copy()
            fadeins.append(FadeIn(interim))
            anims.append(Transform(Group(interim, mul), xmm3l))

        self.play(fadeins)
        self.play(anims)
        self.play(Write(xmm3_label))

        t = [
            Text(".width", font="Terminess Nerd Font Propo", font_size=22).shift(
                DOWN * i + 0.2 * RIGHT + group_offt + 2 * UP
            )
            for i in range(4)
        ]

        xmm4 = [
            Square(0.5, fill_color=GREEN, fill_opacity=0.5, color=GREEN).shift(
                4 * RIGHT + 0.5 * DOWN * x + 2 * UP
            )
            for x in range(4)
        ]
        xmm4_label = Text("xmm4", font="Terminess Nerd Font Propo", font_size=22).move_to(xmm4[3].get_edge_center(DOWN) + 0.5 * DOWN)


        anims = []
        for mul, shape, xmm4l in zip(t, shapes, xmm4):
            anims.append(Transform(Group(shape, mul), xmm4l))

        self.play(map(Write, t))
        self.wait(1)
        self.play(anims)
        self.play(Write(xmm4_label))
        brace = Brace(VGroup(*xmm4), RIGHT, sharpness=.7)
        brace_ = Brace(xmm3[0], LEFT, sharpness=.7)
        brace_text = Text('128\nbits', font="Terminess Nerd Font Propo", font_size=24).move_to(brace.get_center() + .5 * RIGHT + .25 * UP)
        brace_text_ = Text('32\nbits', font="Terminess Nerd Font Propo", font_size=24).move_to(brace_.get_center() + .5 * LEFT)
        self.play(
            Write(brace),
            FadeIn(brace_text),
            Write(brace_),
            FadeIn(brace_text_),
        )
        self.wait(6)
        self.play(FadeOut(brace, brace_text, brace_, brace_text_))
