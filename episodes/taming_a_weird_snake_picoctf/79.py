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

        raw = """150 LOAD_NAME                2 (key_list)
152 LOAD_METHOD              4 (extend)
154 LOAD_NAME                2 (key_list)
156 CALL_METHOD              1
158 POP_TOP
160 JUMP_ABSOLUTE          134"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack.shift((3.5 + MED_SMALL_BUFF) * DOWN + 4 * RIGHT)
        code[-1].set_opacity(1)
        glob = RoundedRectangle(
            width=2,
            height=1,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=.5,
            corner_radius=0.05,
        )
        bob = RoundedRectangle(
            width=2,
            height=1,
            color=PURPLE,
            fill_color=PURPLE,
            fill_opacity=.5,
            corner_radius=0.05,
        )
        vg = VGroup(glob, bob).arrange(buff=MED_LARGE_BUFF).shift(3.5 * LEFT + 2 * DOWN)
        self.play(FadeIn(glob))
        self.wait(1)
        glob.set_opacity(0)
        self.play(FadeIn(bob))
        self.wait(1)
        bob.set_opacity(0)
        x = VGroup(
            Line(start=bob.get_corner(UR) + .5 * UR, end=glob.get_corner(DL) + .5 * DL, stroke_width=5, color=RED),
            Line(start=glob.get_corner(UL) + .5 * UL, end=bob.get_corner(DR) + .5 * DR, stroke_width=5, color=RED)
        ).move_to(vg)
        self.play(Create(x))
        self.wait(1)
