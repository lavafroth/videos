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
        stack = (
            VGroup(*stack)
            .arrange(DOWN)
            .shift(2.5 * DOWN + 4 * RIGHT)
        )
        tim = stackvar(PURPLE).next_to(stack, UP).set_z_index(-1)
        text = Text(
            "0x7f04f6bdedf0",
            font=codefont,
            font_size=32,
        ).move_to(tim)
        g1 = VGroup(tim, text)
        self.add(g1)
        g2 = VGroup(
            stackvar(ORANGE).set_z_index(-1),
            Text(
                        "'<listcomp>'",
                        font=codefont,
                        font_size=32,
                    )
        ).next_to(tim, UP)
        self.add(g2)
        g3 = VGroup(
            stackvar(WHITE).set_z_index(-1),
            Text(
                        "<listcomp>",
                        font=codefont,
                        font_size=32,
                    )
        ).move_to((g1.get_center() + g2.get_center())/ 2)
        self.play(ReplacementTransform(VGroup(g1, g2), g3))
        self.play(g3.animate.next_to(stack, UP))
        self.wait(2)
        self.play(g3.animate.shift(2 * DOWN))
        self.wait(2)
