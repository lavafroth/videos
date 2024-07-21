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

        raw = """  2          84 LOAD_CONST              30 ('J')
             86 STORE_NAME               1 (key_str)"""
        code = MonoParagraph(raw).to_edge(UL)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        jbox = stackvar(ORANGE).set_z_index(-2)
        j = MonoText("'J'").move_to(jbox.get_center())
        off = (4 + SMALL_BUFF) * LEFT
        jgrp = VGroup(j, jbox).next_to(stack, UP).shift(off)

        self.play(FadeIn(code, shift=2*UP))
        self.play(code[1].animate.set_opacity(.5))
        self.wait(1)
        self.play(Create(jbox), ReplacementTransform(code[0][-4:-1], j))
        self.play(jgrp.animate.shift(-off))
        self.wait(1)
        code[0] = VGroup(code[0][-1], code[0][:-4])
        self.play(code[1].animate.set_opacity(1), code[0].animate.set_opacity(.5))
        key_str = code[1][-7-1:-1]
        self.play(ripple(key_str))
        self.wait(1)
        self.play(Transform(jgrp, key_str))
        self.play(FadeOut(code[0], code[1], jgrp))
        self.wait(3)
