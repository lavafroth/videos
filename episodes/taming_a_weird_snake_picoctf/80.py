#!/usr/bin/env manim
from manim import *
from hackermanim import *

def stackvar(color, opacity=0.5):
    return RoundedRectangle(
        width=4,
        height=1,
        color=color,
        fill_color=color,
        fill_opacity=opacity,
        corner_radius=0.05,
    )

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        stack_var = stackvar(BLUE)
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift((3.5 + MED_SMALL_BUFF) * DOWN + 4 * RIGHT)
        a = stackvar(WHITE).next_to(stack, UP)
        b = stackvar(WHITE).next_to(a, UP)
        arc = ArcBetweenPoints(a.get_edge_center(LEFT), b.get_edge_center(LEFT), angle=-PI/2)
        self.play(Create(arc))
        self.wait(1)
        self.play(FadeOut(arc))
