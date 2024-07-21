#!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import *


def roundedrect(n):
    sv = []
    for x in range(n):
        if x == 0 or x == n - 1:
            if x == 0:
                cr = [0.05, 0.05, 0, 0]
            if x == n - 1:
                cr = [0, 0, 0.05, 0.05]
            box = RoundedRectangle(
                width=1.5,
                height=1,
                color=TEAL,
                fill_color=TEAL,
                fill_opacity=0.5,
                corner_radius=cr,
            )
        else:
            box = Rectangle(
                width=1.5,
                height=1,
                color=TEAL,
                fill_color=TEAL,
                fill_opacity=0.5,
            )
        sv.append(box)
    return VGroup(*sv).arrange(buff=0)


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """  1           0 LOAD_CONST               0 (4)
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
             54 LOAD_CONST              20 (10)
             56 LOAD_CONST               0 (4)
             58 LOAD_CONST              21 (86)
             60 LOAD_CONST              22 (43)
             62 LOAD_CONST              23 (102)
             64 LOAD_CONST              24 (126)
             66 LOAD_CONST              25 (92)
             68 LOAD_CONST               3 (0)
             70 LOAD_CONST              26 (16)
             72 LOAD_CONST              27 (58)
             74 LOAD_CONST               2 (41)
             76 LOAD_CONST              28 (89)
             78 LOAD_CONST              29 (78)
             80 BUILD_LIST              40
             82 STORE_NAME               0 (input_list)"""
        code = MonoParagraph(raw).to_edge(DL)
        self.play(FadeIn(code, shift=10 * UP))
        self.play(VGroup(code[:-2], code[-1]).animate.set_opacity(0.5))
        self.play(code.animate.shift(2.5 * LEFT))
        stack.shift(2.5 * DOWN + 4 * RIGHT)
        self.play(AnimationGroup((Create(x) for x in stack), lag_ratio=1 / n))

        liste = stackvar(TEAL)
        lis = (
            VGroup(
                liste,
                liste.copy(),
                Text("...").rotate(PI / 2),
                liste.copy(),
            )
            .arrange(UP)
            .next_to(stack, UP)
        )
        self.play(AnimationGroup((Create(x) for x in lis), lag_ratio=1 / 4))
        wrapper = SurroundingRectangle(
            lis, color=WHITE, fill_color=WHITE, fill_opacity=0.4, corner_radius=0.05
        )
        self.wait(3)
        self.play(Create(wrapper))
        self.wait(1)
        wrapper = VGroup(wrapper, lis)
        sml = RoundedRectangle(
            width=4,
            height=1,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0.5,
            corner_radius=0.05,
        ).next_to(stack, UP)
        self.play(Transform(wrapper, sml))
        self.wait(1)
        off = 6 * UP
        self.play(
            code[-2].animate.shift(off).set_opacity(0.5),
            code[-1].animate.shift(off).set_opacity(1),
            code[:-2].animate.shift(off),
        )
        self.wait(3)
        input_list = code[-1][-11:-1]
        self.play(ripple(input_list))
        t = MonoText("input_list", font_size=34).next_to(code, DOWN)
        self.play(Transform(input_list, t))
        self.wait(3)
        off = (t.get_center() - wrapper.get_center()) * RIGHT
        l = (
            octicon("link-24", fill_color=WHITE)
            .scale(0.4)
            .rotate(PI / 4)
            .next_to(t, DOWN)
        )
        self.play(wrapper.animate.shift(off))
        self.play(Write(l))
        self.play(FadeOut(l, shift=UP), Transform(wrapper, t))
        self.play(FadeOut(code[-4:]), FadeOut(wrapper))
        self.wait(3)
