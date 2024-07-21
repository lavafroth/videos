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
        dz = Text('.0', font=codefont, font_size=32)
        dz.move_to(phantom_2)
        self.add(dz)
        a = CurvedArrow(dz.get_edge_center(RIGHT) + .1 * RIGHT, phantom_0.get_edge_center(RIGHT) + .1 * RIGHT, angle=-PI)
        self.play(Create(a))

        self.wait(1)
        self.play(FadeOut(a, dz))
