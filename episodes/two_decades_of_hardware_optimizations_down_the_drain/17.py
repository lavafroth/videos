#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
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
        self.wait(1)
        self.play(grp.animate.fade(0.5))
        x_scale = 2
        x = [
            Line(start=x_scale * UR, end=x_scale * DL, stroke_width=5, color=RED),
            Line(start=x_scale * UL, end=x_scale * DR, stroke_width=5, color=RED)
        ]
        for line in x:
            self.play(Create(line), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(y) for y in (*x, grp))
