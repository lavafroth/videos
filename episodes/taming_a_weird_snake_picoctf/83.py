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
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont)

        raw = """150 LOAD_NAME                2 (        )
152 LOAD_METHOD              4 (      )
154 LOAD_NAME                2 (        )
156 CALL_METHOD              1
158 POP_TOP
160 JUMP_ABSOLUTE          134"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[-2].set_opacity(1)

        raw_2 = """134 LOAD_NAME                3 (   )
136 LOAD_NAME                2 (        )
138 CALL_FUNCTION            1
140 LOAD_NAME                3 (   )
142 LOAD_NAME                0 (          )
144 CALL_FUNCTION            1
146 COMPARE_OP               0 ( )
148 POP_JUMP_IF_FALSE      162"""
        code_2 = MonoParagraph(raw_2).to_edge(UL).set_opacity(0.5)

        stack_var = stackvar(BLUE)
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = (
            VGroup(*stack)
            .arrange(DOWN)
            .shift((3.5 + MED_SMALL_BUFF) * DOWN + 4 * RIGHT)
        )
        self.add(stack, code)
        self.play(code[-2].animate.set_opacity(0.5), code[-1].animate.set_opacity(1))
        self.play(code.animate.next_to(code_2, DOWN, buff=SMALL_BUFF).shift(.2 * LEFT), FadeIn(code_2, shift=4 * DOWN))
        arr = CurvedArrow(code[-1][-3:].get_edge_center(LEFT) + .2 * LEFT, code_2[0][:3].get_edge_center(DOWN) + .2 * DOWN, angle=-PI/2)
        self.play(Create(arr), code_2[0][:3].animate.set_opacity(1))
        self.wait(1)
        off = 2 * RIGHT
        arr_ = CurvedArrow(code[-1].get_edge_center(LEFT) + .2 * LEFT + off, code_2[0].get_edge_center(LEFT) + .2 * LEFT + off, angle=-PI/2)
        self.play(stack.animate.shift(4 * DOWN), VGroup(code, code_2).animate.shift(2 * RIGHT), Transform(arr, arr_))
        self.wait(4)
