#!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)

        raw = """128 GET_ITER
130 CALL_FUNCTION            1
132 STORE_NAME               2 (key_list)"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        code[0].set_opacity(1)
        self.add(code)

        phantom = stackvar(WHITE).next_to(stack, UP)

        co_box = (
            stackvar(YELLOW_B)
            .set_z_index(-1)
            .next_to(phantom, UP)
        )
        
        self.play(FadeOut(code[0], shift=2 * UP), code[1:].animate.to_edge(UL))
        self.play(code[1].animate.set_opacity(1))
        self.wait(1)
