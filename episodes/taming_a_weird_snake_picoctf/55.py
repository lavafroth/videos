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
        com = octicon("gear-24", fill_color=WHITE).scale(0.3)
        com1 = (
            octicon("gear-16", fill_color=WHITE).scale(0.3 * 16 / 24).shift(0.35 * DR)
        )
        cogs = Group(com, com1).next_to(me, UP).scale(1.5)
        self.play(FadeIn(cogs, shift=UP))
        self.play(
            Rotate(com, angle=0.5 * PI, about_point=com.get_center()),
            Rotate(com1, angle=1.5 * PI, about_point=com1.get_center()),
        )
        self.wait(1)
        self.play(FadeOut(cogs, shift=DOWN))
