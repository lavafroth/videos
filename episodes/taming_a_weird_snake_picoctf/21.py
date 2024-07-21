#!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont)

        lc = MonoText('LOAD_CONST', font_size=50, color=GREEN)
        self.add(lc)
        file = octicon('file-24', fill_color=WHITE).scale(0.7).shift(DOWN)
        const = Rectangle(width=.25, height=.15, color=WHITE, fill_color=TEAL, fill_opacity=.4)
        consts = [const.copy() for _ in range(4)]
        consts = VGroup(*consts).arrange(buff=0).shift(DOWN)
        self.play(lc.animate.shift(UP), Write(file), Write(consts))
        arrow = CurvedArrow(lc.get_edge_center(DOWN) + 0.1 * DOWN, consts[0].get_edge_center(UP) + 0.1 * UP, angle=PI/4, tip_length=.2)
        self.play(Create(arrow))
        for i, const in enumerate(consts[:-1]):
            arrow_ = CurvedArrow(lc.get_edge_center(DOWN) + 0.1 * DOWN, const.get_edge_center(UP) + 0.1 * UP, angle=i/4 + PI/4, tip_length=.2)
            self.play(Transform(arrow, arrow_))

        ccopy= RoundedRectangle(width=.25, height=.15, color=TEAL, fill_color=TEAL, fill_opacity=.4, corner_radius=0.02).scale(3).move_to(ORIGIN + 3.5 * RIGHT+ UP)
        arrow_ = Arrow(lc.get_edge_center(RIGHT), ccopy.get_edge_center(LEFT), tip_length=.2)
        self.play(ReplacementTransform(consts[2], ccopy), Transform(arrow, arrow_))
        self.play(Group(file, lc, arrow, consts, ccopy).animate.shift(3.5 * LEFT))
        stack_var = stackvar(BLUE)
        stack = (stack_var.copy().fade(x/n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(DOWN + 3.5 * RIGHT)
        self.play(AnimationGroup((Create(x) for x in stack), lag_ratio=1/n), ccopy.animate.shift(2 * UP), FadeOut(arrow))
        sv = stackvar(TEAL).next_to(stack, UP)
        self.play(Transform(ccopy, sv))
        self.wait(2)
        self.play(VGroup(stack, ccopy).animate.shift(6 * RIGHT))
        self.play(FadeOut(lc, file), consts.animate.shift(UP + 3.5 * RIGHT))
        sv = RoundedRectangle(grid_xstep = 6/4, width=6, height=1, color=TEAL, fill_color=TEAL, fill_opacity=0.5, corner_radius=0.05)
        t = MonoText('co_consts', font=codefont).next_to(sv, DOWN)
        self.play(ReplacementTransform(VGroup(consts[0:2], consts[3]), sv), Write(t))
        self.wait(2)
        code = """  1           0 LOAD_CONST               0 (4)
              2 LOAD_CONST               1 (54)
              4 LOAD_CONST               2 (41)
              6 LOAD_CONST               3 (0)
              8 LOAD_CONST               4 (112)
             10 LOAD_CONST               5 (32)
             12 LOAD_CONST               6 (25)
             14 LOAD_CONST               7 (49)
             16 LOAD_CONST               8 (33)
             18 LOAD_CONST               9 (3)
             20 LOAD_CONST               3 (0)
             22 LOAD_CONST               3 (0)
             24 LOAD_CONST              10 (57)
             26 LOAD_CONST               5 (32)
             28 LOAD_CONST              11 (108)
             30 LOAD_CONST              12 (23)
             32 LOAD_CONST              13 (48)
             34 LOAD_CONST               0 (4)
             36 LOAD_CONST              14 (9)
             38 LOAD_CONST              15 (70)
             40 LOAD_CONST              16 (7)
             42 LOAD_CONST              17 (110)
             44 LOAD_CONST              18 (36)
             46 LOAD_CONST              19 (8)
             48 LOAD_CONST              11 (108)
             50 LOAD_CONST              16 (7)
             52 LOAD_CONST               7 (49)
             54 LOAD_CONST              20 (10)"""
        code = MonoParagraph(code).to_edge(UL)
        self.play(Group(sv, t).animate.shift(12 * RIGHT), FadeIn(code, shift=12 * RIGHT))
