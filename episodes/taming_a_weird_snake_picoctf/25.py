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

        raw = """  3          88 LOAD_CONST              31 ('_')
             90 LOAD_NAME                1 (key_str)
             92 BINARY_ADD
             94 STORE_NAME               1 (key_str)
"""
        code = MonoParagraph(raw).to_edge(UL)

        stack_var = RoundedRectangle(width=4, height=1, color=BLUE, fill_color=BLUE, fill_opacity=0.5, corner_radius=0.05)
        n = 3
        stack = (stack_var.copy().fade(x/n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        jbox = RoundedRectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-2)
        j = MonoText("'_'").move_to(jbox)
        off = (4 + SMALL_BUFF) * LEFT
        jgrp = VGroup(j, jbox).next_to(stack, UP).shift(off)

        self.play(FadeIn(code, shift=2*UP))
        self.play(code[1:].animate.set_opacity(.5))
        self.wait(1)
        self.play(Create(jbox), ReplacementTransform(code[0][-4:-1], j))
        self.play(jgrp.animate.shift(-off))
        self.wait(1)
        code[0] = VGroup(code[0][-1], code[0][:-4])
        self.play(code[1].animate.set_opacity(1), code[0].animate.set_opacity(.5))
        key_str = code[1][-7-1:-1]
        self.play(ripple(key_str))
        self.wait(1)
        jjbox = RoundedRectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-2)
        jj = MonoText("'J'").move_to(jjbox)
        jjgrp = VGroup(jj, jjbox).next_to(jgrp, UP).shift(off)
        self.play(ReplacementTransform(key_str, jjgrp))
        self.play(jjgrp.animate.shift(-off))
        self.play(FadeOut(code[0], code[1][:-8], code[1][-1]))
        code = code[2:]
        self.play(code.animate.to_edge(UL))
        self.play(code[0].animate.set_opacity(1))

        brace = Brace(VGroup(jjbox, jbox), LEFT)

        p1 = code[0][-1].get_edge_center(RIGHT) + 0.1 * RIGHT
        p1b = p1 + [1, 0, 0]
        l1 = Line(p1, p1b)
        p2 = brace.get_edge_center(LEFT) + 0.1 * LEFT
        p2b = p2 - [1, 0, 0]
        l2 = Line(p2b, p2)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.play(Create(l1), rate_func=rate_functions.ease_in_quad, run_time=.5)
        self.play(Create(bezier), rate_func=rate_functions.linear, run_time=.5)
        self.play(Create(l2), rate_func=rate_functions.ease_out_quad, run_time=.5)
        self.play(Write(brace))
        self.wait(2)
        dupe0 = RoundedRectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.8, corner_radius=0.05).set_z_index(-2).move_to(jbox.get_center())
        dupe1 = dupe0.copy().move_to(jjbox.get_center())

        clone0 = jbox.copy()
        clone1 = jjbox.copy()
        self.play(Transform(jbox, dupe0))
        self.wait(1)
        self.play(Transform(jbox, clone0), Transform(jjbox, dupe1))
        self.wait(1)
        self.play(Transform(jjbox, clone1))
        self.play(FadeOut(jjgrp, jgrp, bezier, l1, l2, brace, code[0][-10:]))
        self.wait(3)
