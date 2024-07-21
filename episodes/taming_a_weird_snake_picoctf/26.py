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

        raw = """             92 BINARY_ADD
             94 STORE_NAME               1 (key_str)
"""
        code = MonoParagraph(raw).to_edge(UL)
        code[1].set_opacity(0.5)

        stack_var = Rectangle(width=4, height=1, color=BLUE, fill_color=BLUE, fill_opacity=0.5)
        n = 3
        stack = (stack_var.copy().fade(x/n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        badd = code[0][-10:]
        self.add(badd)

        jbox = RoundedRectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-2)
        j = MonoText("'_'").move_to(jbox.get_center())
        off = (4 + SMALL_BUFF) * LEFT
        jgrp = VGroup(j, jbox).next_to(stack, UP)
        self.add(jgrp)

        jjbox = RoundedRectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-2)
        jj = MonoText("'J'").move_to(jjbox.get_center()).set_z_index(2)
        jjgrp = VGroup(jj, jjbox).next_to(jgrp, UP)
        self.add(jjgrp)
        brace = Brace(VGroup(jjbox, jbox), LEFT)
        self.add(brace)

        p1 = code[0][-1].get_edge_center(RIGHT) + 0.1 * RIGHT
        p1b = p1 + [1, 0, 0]
        l1 = Line(p1, p1b)
        p2 = brace.get_edge_center(LEFT) + 0.1 * LEFT
        p2b = p2 - [1, 0, 0]
        l2 = Line(p2b, p2)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.add(bezier, l1, l2)
        self.play(Unwrite(brace), Uncreate(l2), rate_func=rate_functions.ease_out_quad, run_time=.5)
        self.play(Uncreate(bezier), rate_func=rate_functions.linear, run_time=.5)
        self.play(Uncreate(l1), rate_func=rate_functions.ease_in_quad, run_time=.5)
        p = MonoText('+', font_size=40)
        jb = RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(1)
        ub = RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-1)
        vg = VGroup(ub, p, jb).arrange()
        self.play(
            ReplacementTransform(jbox, ub),
            ReplacementTransform(jjbox, jb),
            Transform(badd, p),
            j.animate.move_to(ub.get_center()),
            jj.animate.move_to(jb.get_center()),
        )
        jg = VGroup(jj, jb)
        ug = VGroup(j, ub)
        self.play(ug.animate.move_to(jg), jg.animate.move_to(ug))
        self.play(ug.animate.move_to(jg), jg.animate.move_to(ug))
        self.wait(1)
        a = MonoText("= '_J'", font_size=40).next_to(jg)
        alessa = a.copy()[-4:]
        acopy = alessa[1:-1]
        b = MonoText("= 'J_'", font_size=40).next_to(jg)
        self.play(Write(a))
        self.wait(2)
        self.play(ug.animate.move_to(jg), jg.animate.move_to(ug), AnimationGroup(Unwrite(a[-3:-1]), Write(b[-3:-1]), lag_ratio=1))
        self.play(ug.animate.move_to(jg), jg.animate.move_to(ug), AnimationGroup(Unwrite(b[-3:-1]), Write(acopy), lag_ratio=1))
        self.wait(1)
        re = RoundedRectangle(width=1.5, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-1)
        self.play(ReplacementTransform(VGroup(ub, jb), re), FadeOut(jj, j, a, badd), alessa.animate.move_to(ORIGIN))
        self.wait(1)
