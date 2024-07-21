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

        raw = """128 GET_ITER
130 CALL_FUNCTION            1
132 STORE_NAME               2 (key_list)"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        stack.shift(2.5 * DOWN + 4 * RIGHT)
        code[0].set_opacity(1)

        phantom = stack_var.next_to(stack, UP)

        co_box = stackvar(YELLOW_B).set_z_index(-1).next_to(phantom, UP)
        co_txt = SVGMobject("iter-rot", fill_color=WHITE).move_to(co_box).scale(0.3)
        co = VGroup(co_txt, co_box)
        self.add(co)

        self.play(
            co_txt.animate.move_to(ORIGIN),
            co_box.animate.move_to(phantom),
        )
        self.wait(2)
        self.play(
            co_txt.animate.move_to(phantom),
        )
        self.wait(1)
