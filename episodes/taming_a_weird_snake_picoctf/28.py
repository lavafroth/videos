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

        raw = """ 96 LOAD_NAME                1 (key_str)
 98 LOAD_CONST              32 ('o')
100 BINARY_ADD
102 STORE_NAME               1 (key_str)"""
        
        code = MonoParagraph(raw).to_edge(UL)
        code[3].set_opacity(0.5)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        badd = code[2][-10:]
        self.add(badd)

        jbox = stackvar(ORANGE).set_z_index(-2)
        j = MonoText("'_J'").move_to(jbox.get_center())
        off = (4 + SMALL_BUFF) * LEFT
        jgrp = VGroup(j, jbox).next_to(stack, UP)
        self.add(jgrp)

        jjbox = RoundedRectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-2)
        jj = MonoText("'o'").move_to(jjbox.get_center()).set_z_index(2)
        jjgrp = VGroup(jj, jjbox).next_to(jgrp, UP)
        self.add(jjgrp)
        brace = Brace(VGroup(jjbox, jbox), LEFT)

        p = MonoText('+', font_size=40)
        jb = RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(1)
        ub = RoundedRectangle(width=1.5, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-1)
        vg = VGroup(ub, p, jb).arrange()
        self.play(
            ReplacementTransform(jbox, ub),
            ReplacementTransform(jjbox, jb),
            Transform(badd, p),
            j.animate.move_to(ub.get_center()),
            jj.animate.move_to(jb.get_center()),
        )
        jg = VGroup(jj, jb)
        ug = VGroup(j, ub)
        a = MonoText("= '_Jo'", font_size=40).next_to(jg)
        alessa = a[-5:]
        self.play(Write(a))
        self.wait(1)
        re = RoundedRectangle(width=2, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-1)
        self.play(ReplacementTransform(VGroup(ub, jb), re), FadeOut(jj, j, a[:-5], badd), alessa.animate.move_to(ORIGIN))
        self.wait(1)
