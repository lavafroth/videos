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
        phantom = stack
        for x in range(3):
            phantom = stack_var.next_to(phantom, UP)

        phantom.shift(3 * DOWN)
        me = RoundedRectangle(width=4, height=1, color=WHITE, fill_color=WHITE, fill_opacity=.5, corner_radius=0.05).set_z_index(-1).next_to(phantom, UP)
        t = Text("'t'", font=codefont, font_size=32).move_to(me)
        self.add(t)
        self.play(FadeOut(t, shift=4 * RIGHT))
