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
130 CALL_FUNCTION            1
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
        self.play(FadeIn(stack, code, shift=8 * UP))

        self.wait(1)
        self.play(FadeOut(code[0], shift=2 * UP), code[1:].animate.to_edge(UL))
        self.play(code[1].animate.set_opacity(1))
        me = RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05, fill_color=WHITE, fill_opacity=1).next_to(stack, UP)
        key_list = code[1][-9:-1]
        self.play(Transform(me, key_list))
        self.wait(1)
