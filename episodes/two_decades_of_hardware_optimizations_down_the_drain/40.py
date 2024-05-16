#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        text = Text('Clean code?')
        self.play(FadeIn(text))
        self.wait(2)
        self.play(text.animate.shift(3 * UP))

        table = Rectangle(
            width=2,
            height=3 / 2,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.3,
            grid_ystep=3 / 8,
        ).shift(2 * DR)
        trait_object = Rectangle(
            width=1,
            height=3 / 4,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.3,
            grid_ystep=3 / 8,
        )
        a1 = Arrow(0.2 * UP, 0.2 * UP + 2 * RIGHT)
        a2 = Arrow(0.2 * DOWN, 1.4 * DOWN + 2 * RIGHT)
        a3 = Arrow(2.6 * DOWN + 1.5 * RIGHT, 2.6 * DOWN + 0.1 * LEFT)
        data = Rectangle(
            width=1.5, height=0.5, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3
        ).shift(2 * RIGHT + .2 * UP)
        mc = Text("machine\ncode", font="Terminess Nerd Font Propo", font_size=22).shift(2.6 * DOWN + 0.5 * LEFT)
        grp = Group(
            trait_object,
            table,
            a1,
            a2,
            a3,
            data,
            mc,
        )

        grp.shift(UP + LEFT)
        self.play(
            Create(trait_object),
            Create(table),
            Create(a1),
            Create(a2),
            Create(a3),
            Create(data),
            Create(mc),
        )

        self.wait(10)
        a = Group(trait_object, table)
        b = Group(data, mc)
        a_ = octicon('package-24', fill_color=WHITE).scale(.5).shift(LEFT)
        b_ = octicon('package-24', fill_color=WHITE).scale(.5).shift(RIGHT)
        self.play(FadeOut(a1, a2, a3), Transform(a, a_), Transform(b, b_))
        separate = Text('Separate crates', font_size=24).shift(DOWN)
        self.play(Write(separate), FadeOut(text))
        self.wait(8)
        self.play(FadeOut(a, b, separate))
