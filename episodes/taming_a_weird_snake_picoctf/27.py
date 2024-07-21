#!/usr/bin/env manim
from manim import *
from manim import Transfrom as T
from hackermanim import *
from stack import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """ 96 LOAD_NAME                1 (key_str)
 98 LOAD_CONST              32 ('o')
100 BINARY_ADD
102 STORE_NAME               1 (key_str)"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        jbox = RoundedRectangle(width=1.5, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_index(-1)
        underj = MonoText("'_J'", font_size=40).move_to(jbox).set_z_index(1)

        jgrp = VGroup(underj, jbox)
        self.add(jgrp)

        self.play(FadeIn(code, shift=2*UP))
        self.play(code[0].animate.set_opacity(1))

        jbox_ = stackvar(ORANGE).set_index(-1).next_to(stack, UP)
        underj_ = MonoText("'_J'").move_to(jbox_).set_z_index(1)
        self.play(T(jbox, jbox_), T(underj, underj_))
        self.play(code[1].animate.set_opacity(1), code[0].animate.set_opacity(.5))

        obox = stack(ORANGE).set_z_index(-2)
        o = MonoText("'o'").move_to(obox).set_z_index(2)
        ogrp = VGroup(o, obox).next_to(jbox, UP)

        self.play(ReplacementTransform(code[1][-4:-1], ogrp))
        code1rem = VGroup(code[1][:-4], code[1][-1])
        self.play(code[2].animate.set_opacity(1), code1rem.animate.set_opacity(.5))
        self.wait(1)
        self.play(FadeOut(code[2:], code1rem, code[0], ogrp, jgrp))
