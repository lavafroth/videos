#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        _ord_call = Text('ord(   )', font=codefont, font_size=32, color=PURPLE)
        c = Circle(radius=.2, color=ORANGE, fill_color=ORANGE, fill_opacity=.5).shift(.32 * RIGHT)
        g = VGroup(_ord_call, c)
        self.play(g.animate.scale(2).shift(UP))
        ch = Text('ü', font=codefont, font_size=40).shift(2 * LEFT)
        self.play(Write(ch))
        chn = Text('252', font=codefont, font_size=40).shift(2 * RIGHT)
        end  =chn.get_edge_center(LEFT)
        start =ch.get_edge_center(RIGHT)
        disp = (end - start) * RIGHT
        end = start + disp
        a = Arrow(start, end)
        self.play(Create(a))
        self.play(Write(chn))
        self.play(c.animate.shift(2 * DOWN + 2 * LEFT))
        self.wait(1)
        c.set_opacity(0)
        self.wait(2)
