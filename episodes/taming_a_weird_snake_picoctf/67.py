#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        stack_var = Rectangle(width=4, height=1)
        n = 3
        stack = (stack_var.copy().fade(x/n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        phantom_0 = stack_var.copy().next_to(stack, UP)
        phantom_1 = stack_var.copy().next_to(phantom_0, UP)
        phantom_2 = stack_var.copy().next_to(phantom_1, UP)
        phantom_2.shift(3 * DOWN)
        phantom_1.shift(3 * DOWN)
        sq = RoundedRectangle(
            width=0.8, height=0.8, color=TEAL, fill_color=TEAL, fill_opacity=0.5, corner_radius=.05
        ).shift(DOWN + 2 * RIGHT)
        self.add(sq)
        self.wait(.5)
        rect = RoundedRectangle(
            width=4, height=1, color=TEAL, fill_color=TEAL, fill_opacity=0.5, corner_radius=.05
        ).next_to(phantom_2, UP)
        self.play(Transform(sq, rect))
        rect = RoundedRectangle(
            width=4, height=1, color=WHITE, fill_color=WHITE, fill_opacity=0.5, corner_radius=.05
        ).move_to(phantom_1)
        self.play(sq.animate.move_to(phantom_1).scale(.8), rate_func=rate_functions.ease_in_quad, run_time=.5)
        self.play(Transform(sq, rect), rate_func=rate_functions.ease_out_quad, run_time=.5)
