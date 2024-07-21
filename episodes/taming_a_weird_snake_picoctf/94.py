#!/usr/bin/env manim

from manim import *
from manim import VGroup as V
from hackermanim import *


def stackvar(color, opacity=0.5):
    return RoundedRectangle(
        width=4,
        height=1,
        color=color,
        fill_color=color,
        fill_opacity=opacity,
        corner_radius=0.05,
    ).set_z_index(-1)


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont)

        raw = """
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[2].set_opacity(1)
        stack_var = stackvar(BLUE)
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(4.5 * DOWN + 4 * RIGHT)
        self.play(FadeIn(code, shift=4 * DOWN),FadeIn(stack, shift=4 * UP) )
        self.wait(1)
        me = stackvar(WHITE)
        self.play(me.animate.next_to(stack, UP))
        self.play(code[3].animate.set_opacity(1), code[2].animate.set_opacity(0.5))
        self.wait(1)
        res = code[3][-7:-1]
        self.play(Transform(me, res))
        self.wait(2)
        raw_2 = """
182 LOAD_CONST              38 ('')
184 LOAD_METHOD              7 (join)
186 LOAD_NAME                8 (map)
188 LOAD_NAME                9 (chr)
190 LOAD_NAME                6 (result)
192 CALL_FUNCTION            2
194 CALL_METHOD              1
196 STORE_NAME              10 (result_text)
198 LOAD_CONST              39 (None)
200 RETURN_VALUE
        """.strip()
        code_2 = MonoParagraph(raw_2).to_edge(UL).set_opacity(0.5).shift(.3 * LEFT)
        self.play(FadeOut(code, me, shift=4 * UP), FadeIn(code_2, shift=4 * UP))
        self.wait(1)
