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

        stack.shift(4.5 * DOWN + 4 * RIGHT)
        g3 = VGroup(
            stackvar(WHITE).set_z_index(-1),
            MonoText("<listcomp>"),
        ).next_to(stack, UP)

        raw = """      0 BUILD_LIST               0
      2 LOAD_FAST                0 (.0)
>>    4 FOR_ITER                16 (to 22)
      6 UNPACK_SEQUENCE          2
      8 STORE_FAST               1 (a)
     10 STORE_FAST               2 (b)
     12 LOAD_FAST                1 (a)
     14 LOAD_FAST                2 (b)
     16 BINARY_XOR
     18 LIST_APPEND              2
     20 JUMP_ABSOLUTE            4
>>   22 RETURN_VALUE"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        self.play(Transform(g3, code))
        self.wait(1)
