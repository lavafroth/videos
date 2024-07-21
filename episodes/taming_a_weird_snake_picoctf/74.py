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

        raw = """>>  134 LOAD_NAME                3 (   )
    136 LOAD_NAME                2 (key_list)
    138 CALL_FUNCTION            1
    140 LOAD_NAME                3 (len)
    142 LOAD_NAME                0 (input_list)
    144 CALL_FUNCTION            1
    146 COMPARE_OP               0 (<)
    148 POP_JUMP_IF_FALSE      162"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        code[0].set_opacity(1)
        self.add(code, stack)
        self.play(code[1].animate.set_opacity(1), code[0].animate.set_opacity(.5))
        phantom = stackvar(BLUE).next_to(stack, UP)
        key_str_box =stackvar(WHITE).next_to(phantom, UP).set_z_index(-1)
        key_str_txt = code[1][-9:-1]

        self.play(
            code.animate.shift(LEFT)
        )
        key_str_txt_copy = key_str_txt.copy()
        self.play(
            key_str_txt_copy.animate.move_to(key_str_box),
            ReplacementTransform(key_str_txt, key_str_box),
        )
        tete = MonoText('len(key_list)').shift(.5 * DOWN)
        self.play(Transform(VGroup(key_str_box, key_str_txt_copy), tete[-9:-1]), code[1][:-9].animate.set_opacity(0.5),code[1][-1].animate.set_opacity(0.5), code[2].animate.set_opacity(1))
        self.wait(3)
