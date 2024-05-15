#!/usr/bin/env manim
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from custom import octicon
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        circle = Circle(radius=0.25, color=WHITE, fill_color=WHITE, fill_opacity=1)
        self.add(circle)
        self.play(circle.animate.shift(UP))
        self.wait(1)
        text = Text('Clean code').shift(2 * UP)
        self.play(Write(text))
        book = octicon('book-24', fill_color=WHITE).scale(0.5).to_edge(DL).shift(UR)
        self.play(Write(book))
        mortar_board = octicon('mortar-board-24', fill_color=WHITE).scale(0.5).to_edge(DR).shift(UL)
        self.play(Write(mortar_board))
        start_handle = book.get_center() + 4 * LEFT + .5 * DOWN
        end_handle = book.get_center() + 4 * RIGHT
        ckpts = [mortar_board.get_center() + 2.5 * x * LEFT for x in range(1, 4)]
        arcpoly = CubicBezier(circle.get_center(), start_handle, end_handle, ckpts[0])
        ckpt_circles = [
            Circle(radius=.25, fill_color=WHITE, color=WHITE, fill_opacity=1).move_to(pos)
            for pos in ckpts[1:]
        ]
        line = Line(start=book.get_center() + RIGHT, end=mortar_board.get_center() + LEFT)
        self.play(
            MoveAlongPath(circle, arcpoly),
            AnimationGroup(
            Create(line),
            FadeIn(ckpt_circles[1]),
            FadeIn(ckpt_circles[0]),
            lag_ratio=0.2
            )
        )
        self.wait(2)
        self.play(FadeOut(Group(line, circle, ckpt_circles[1], ckpt_circles[0], book, mortar_board)))
        self.play(text.animate.to_edge(UP).shift(3.5 * RIGHT))
