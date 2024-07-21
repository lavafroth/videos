#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        raw = """>>  134 LOAD_NAME                3 (len)
    136 LOAD_NAME                2 (key_list)
    138 CALL_FUNCTION            1
    140 LOAD_NAME                3 (len)
    142 LOAD_NAME                0 (input_list)
    144 CALL_FUNCTION            1
    146 COMPARE_OP               0 (<)
    148 POP_JUMP_IF_FALSE      162"""

        stack_var = RoundedRectangle(
            width=4,
            height=1,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.5,
            corner_radius=0.05,
        )
        n = 3
        code = (
            Paragraph(raw, font=codefont, font_size=32).to_edge(UL).set_opacity(0.5)
        )
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        len_ = code[0][-4:-1].set_opacity(1)
        res = RoundedRectangle(
            width=4,
            height=1,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0.5,
            corner_radius=0.05,
        ).next_to(stack, UP).set_z_index(-1)
        len_copy = len_.copy()
        self.play(ReplacementTransform(len_, res), len_copy.animate.move_to(res))
        tete = Text('len(        )', font=codefont, font_size=32).shift(.5 * DOWN)
        self.wait(3)
        self.play(Transform(res, tete[-2:]), Transform(len_copy, tete[:-2]))
        self.wait(1)

