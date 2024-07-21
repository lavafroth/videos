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

        raw = """>>  134 LOAD_NAME                3 (   )
    136 LOAD_NAME                2 (        )
    138 CALL_FUNCTION            1
    140 LOAD_NAME                3 (   )
    142 LOAD_NAME                0 (          )
    144 CALL_FUNCTION            1
    146 COMPARE_OP               0 ( )
    148 POP_JUMP_IF_FALSE      162"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5).shift(LEFT)
        raw_2 = """150 LOAD_NAME                2 (key_list)
152 LOAD_METHOD              4 (extend)
154 LOAD_NAME                2 (key_list)
156 CALL_METHOD              1
158 POP_TOP
160 JUMP_ABSOLUTE          134"""
        code_2 = MonoParagraph(raw_2).to_edge(UL).set_opacity(0.5)

        stack.shift((3.5 + MED_SMALL_BUFF) * DOWN + 4 * RIGHT)
        code[-1].set_opacity(1)
        self.add(code, stack)
        self.wait(1)
        self.play(FadeOut(code, shift=4 * UP), FadeIn(code_2, shift=4 * UP))
        self.wait(1)
        self.play(code_2[0].animate.set_opacity(1))
        key_list = code_2[0][-9:-1]
        lbox = stackvar(WHITE).next_to(stack, UP).set_z_index(-1)
        self.play(Transform(key_list.copy(), lbox), key_list.animate.move_to(lbox))
        self.wait(1)
        self.play(code_2[0][:-9].animate.set_opacity(.5), code_2[0][-1].animate.set_opacity(.5), code_2[1].animate.set_opacity(1))
        self.wait(5)
        extend = code_2[1][-7:-1]
        lbox = stackvar(PURPLE).next_to(lbox, UP).set_z_index(-1)
        self.play(Transform(extend.copy(), lbox), extend.animate.move_to(lbox))
        self.wait(1)
