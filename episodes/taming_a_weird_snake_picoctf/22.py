#!/usr/bin/env manim
from manim import *
from hackermanim import *


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
             54 LOAD_CONST              20 (10)"""
        code = MonoParagraph(raw).to_edge(UL)
        self.add(code)
        colorem = []
        parens = []
        for line, line_of_code in zip(raw.splitlines(), code):
            index = -line[::-1].find("(")
            colorem.append(line_of_code[index:-1])
            parens.append(line_of_code[index - 1].copy())
            parens.append(line_of_code[-1].copy())

        colorem = VGroup(*colorem)
        self.play(colorem.animate.set(color=TEAL))
        parens = VGroup(*parens)
        self.play(Write(parens))
        sv = roundedrect(4).shift(DOWN)
        el = Text("...").move_to(sv[-2].get_center())

        self.play(
            code[0].animate.move_to(UP),
            FadeOut(code[1:], parens),
            FadeIn(sv, shift=12 * LEFT),
            FadeIn(el, shift=12 * LEFT),
        )

        self.wait(2)
        arr = CurvedArrow(code[0][-4].get_edge_center(LEFT) + .2 * LEFT, sv[0].get_edge_center(UP) + .2 * UP, angle=PI/6)
        self.play(Create(arr))
        sv_ = roundedrect(3).shift(DOWN)
        self.wait(2)

        self.play(
            FadeOut(arr),
            Transform(sv[0], colorem[0]),
            Transform(sv[1:], sv_),
            el.animate.move_to(sv_[-2].get_center()),
        )
        self.wait(3)
