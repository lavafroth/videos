#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """
132 STORE_NAME               2 (key_list)
        """.strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack_var = RoundedRectangle(
            width=4,
            height=1,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.5,
            corner_radius=0.05,
        )
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        code[0].set_opacity(1)
        self.add(code, stack)
        raw = """>>  134 LOAD_NAME                3 (len)
    136 LOAD_NAME                2 (key_list)
    138 CALL_FUNCTION            1
    140 LOAD_NAME                3 (len)
    142 LOAD_NAME                0 (input_list)
    144 CALL_FUNCTION            1
    146 COMPARE_OP               0 (<)
    148 POP_JUMP_IF_FALSE      162"""
        next_s = (
            MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        )
        self.play(code.animate.shift(2 * UP), FadeIn(next_s, shift=2 * UP))
        self.wait(3)
