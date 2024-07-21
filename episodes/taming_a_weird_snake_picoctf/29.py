#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=40)

        raw = """104 LOAD_NAME                1 (key_str)
106 LOAD_CONST              33 ('3')
108 BINARY_ADD
110 STORE_NAME               1 (key_str)
"""
        
        code = MonoParagraph(raw).to_edge(UL)
        code[1:].set_opacity(0.5)

        badd = code[2][-10:]

        jb = RoundedRectangle(width=2, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-2)
        j = MonoText("'_Jo'").move_to(jb)
        jg = VGroup(jb, j)
        self.add(jg)
        self.play(FadeIn(code, shift=2 * UP))
        self.play(code[0].animate.set_opacity(.5), code[1].animate.set_opacity(1))

        ub = RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-3)
        u = MonoText("'3'").move_to(ub)
        ug = VGroup(u, ub)

        p = MonoText('+')
        jgrp_copy = jg.copy()

        three = code[1][-4:-1].copy()

        VGroup(ug, p, jgrp_copy).arrange()
        self.play(jg.animate.move_to(jgrp_copy), ReplacementTransform(three, ug))
        self.play(code[1].animate.set_opacity(.5), code[2].animate.set_opacity(1))

        self.play(ReplacementTransform(badd, p))
        a = MonoText("= '_Jo3'").next_to(jg)
        alessa = a[1:]
        self.play(Write(a))
        self.wait(1)
        re = RoundedRectangle(width=2, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-1)
        self.play(ReplacementTransform(VGroup(ub, jb), re), FadeOut(u, j, a[:1], p), alessa.animate.move_to(ORIGIN))
        self.wait(1)
