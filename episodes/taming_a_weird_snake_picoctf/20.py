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

        code = MonoParagraph(code).to_edge(UL)
        self.play(FadeIn(code, shift=2 * UP))
        self.wait(2)
        lc = code[0][2:12]
        lc_ = MonoText('LOAD_CONST', font_size=50, color=GREEN)
        self.play(Transform(lc, lc_), FadeOut(code[0][:2], code[0][12:], code[1:]))
