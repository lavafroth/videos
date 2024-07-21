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
        MonoText.set_default(font=codefont, font_size=32)

        raw = """      0 BUILD_LIST               0
      2 LOAD_FAST                0 (.0)
>>    4 FOR_ITER                12 (to 18)
      6 STORE_FAST               1 (char)
      8 LOAD_GLOBAL              0 (ord)
     10 LOAD_FAST                1 (char)
     12 CALL_FUNCTION            1
     14 LIST_APPEND              2
     16 JUMP_ABSOLUTE            4
>>   18 RETURN_VALUE"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        phantom_0 = stackvar(BLUE).next_to(stack, UP)
        phantom_1 = stackvar(BLUE).next_to(phantom_0, UP)

        red = "#ff3046"
        me = stackvar(red, 0).set_z_index(-1).next_to(phantom_1, UP)
        self.add(me)

        x_scale = 0.5
        x = VGroup(
            Line(start=x_scale * UR, end=x_scale * DL, stroke_width=5, color=red),
            Line(start=x_scale * UL, end=x_scale * DR, stroke_width=5, color=red),
        ).shift(UP * 0.5 + 1.2 * RIGHT)
        self.play(Transform(me, x))
        self.wait(1)
