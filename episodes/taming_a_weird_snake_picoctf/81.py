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

        raw = """150 LOAD_NAME                2 (        )
152 LOAD_METHOD              4 (      )
154 LOAD_NAME                2 (key_list)
156 CALL_METHOD              1
158 POP_TOP
160 JUMP_ABSOLUTE          134"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack.shift((3.5 + MED_SMALL_BUFF) * DOWN + 4 * RIGHT)
        code[1].set_opacity(1)
        key_list_0_box = stackvar(WHITE).next_to(stack, UP).set_z_index(-1)
        key_list_0 = MonoText("key_list").move_to(key_list_0_box)
        extend_box = stackvar(PURPLE).next_to(key_list_0_box, UP).set_z_index(-1)
        extend = MonoText("extend").move_to(extend_box)
        self.add(code, key_list_0, key_list_0_box, extend, extend_box, stack)

        self.play(code[1].animate.set_opacity(0.5), code[2].animate.set_opacity(1))
        key_list_1_box = stackvar(WHITE).next_to(extend_box, UP).set_z_index(-1)
        key_list = code[2][-9:-1]
        self.play(
            key_list.animate.move_to(key_list_1_box),
            ReplacementTransform(key_list.copy(), key_list_1_box),
        )
        key_list = VGroup(key_list, key_list_1_box)
        extend = VGroup(extend, extend_box)
        key_list_0 = VGroup(key_list_0, key_list_0_box)
        self.wait(1)
        text = MonoText(
            "key_list.extend(key_list)",
            t2c={"extend": PURPLE},
        )
        self.play(
            ReplacementTransform(extend, text[9:15]),
            ReplacementTransform(key_list_0, text[:9]),
            ReplacementTransform(key_list, text[15:]),
        )
        self.wait(1)
        self.play(
            code[2][:-9].animate.set_opacity(0.5),
            code[2][-1].animate.set_opacity(0.5),
            code[3].animate.set_opacity(1),
        )
        text.set_opacity(0)
        self.wait(1)
        text.set_opacity(1)
        nonebox = stackvar(GRAY).next_to(stack, UP).set_z_index(-1)
        none = MonoText("None").move_to(nonebox)
        none = VGroup(none, nonebox)
        self.play(
            ReplacementTransform(text, none)
        )
        self.wait(1)
        self.play(code[3].animate.set_opacity(0.5), code[4].animate.set_opacity(1), FadeOut(none, shift=4 * RIGHT))
        self.wait(1)
