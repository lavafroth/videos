#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        _ord_call = Text("ord(   )", font=codefont, font_size=32, color=PURPLE)
        c = Circle(radius=0.2, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5).shift(
            0.32 * RIGHT
        )
        g = VGroup(_ord_call, c)
        g.scale(2).shift(UP)
        ch = Text("ü", font=codefont, font_size=40).shift(2 * LEFT)
        chn = Text("252", font=codefont, font_size=40).shift(2 * RIGHT)
        end = chn.get_edge_center(LEFT)
        start = ch.get_edge_center(RIGHT)
        disp = (end - start) * RIGHT
        end = start + disp
        a = Arrow(start, end)
        # self.add(a, chn, ch)
        sq = RoundedRectangle(
            width=0.8, height=0.8, color=TEAL, fill_color=TEAL, fill_opacity=0.5, corner_radius=.05
        ).shift(DOWN + 2 * RIGHT)
        sq_ = sq.copy().rotate(-PI/4).set_opacity(0)
        c.shift(2 * DOWN + 2 * LEFT)
        end = sq.get_edge_center(LEFT)
        start = c.get_edge_center(RIGHT)
        disp = (end - start) * RIGHT
        end = start + disp
        a = Arrow(start, end)
        self.add(c)
        self.play(Create(a))
        self.play(Transform(sq_, sq))
        self.wait(1)
