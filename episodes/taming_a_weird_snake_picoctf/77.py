#!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
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

        stack.shift((3.5 + MED_SMALL_BUFF) * DOWN + 4 * RIGHT)
        code[-2].set_opacity(1)
        self.add(code, stack)
        self.wait(1)
        self.play(code[-1].animate.set_opacity(1), code[-2].animate.set_opacity(.5))
        r = SurroundingRectangle(code[-1][-3:], color=BLUE, corner_radius=.05)
        self.play(Create(r))
        self.play(FadeOut(r))
        self.play(ripple(code[-1][3:-3]), run_time=1.5)
        self.wait(1)
