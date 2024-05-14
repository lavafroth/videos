#!/usr/bin/env python
# coding: utf-8

from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from custom import octicon

class ErrorSizes(Scene):
    def construct(self):
        box = Code(code=' Box<dyn std::error::Error>', language='rust', font_size=40)[2][0]
        self.play(FadeIn(box))
        self.wait(2)
        dyn_error = box[len(' Box<'):-1]
        pos = box[len(' Box<')].get_center()
        closing = box[-1]
        rect = Rectangle(width=7, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.8).move_to(pos + 3.5 * RIGHT)
        self.play(Transform(dyn_error, rect))
        rect = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.8).move_to(pos + 2 * RIGHT)
        self.play(AnimationGroup(
            Transform(dyn_error, rect),
            closing.animate.shift(3 * LEFT),
        ))
        rect = Rectangle(width=1, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.8).move_to(pos + 0.5 * RIGHT)
        self.play(AnimationGroup(
            Transform(dyn_error, rect),
            closing.animate.shift(3 * LEFT),
        ))
        rect = Rectangle(width=7, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.8).move_to(pos + 3.5 * RIGHT)
        self.play(AnimationGroup(
            Transform(dyn_error, rect),
            closing.animate.shift(6 * RIGHT),
        ))
        ferris = SVGMobject('rustacean-flat-gesture').rotate(0.8 * PI).to_edge(UR).shift(0.5 * (UP + RIGHT))
        self.play(FadeIn(ferris))
        self.wait(2)
        rect = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.8).shift(2 * (DL))
        self.play(Transform(dyn_error, rect))
        not_equals = Tex(r"$\neq$", font_size=40).shift(2 * DOWN + 0.75 * RIGHT)
        struct = Code(code="struct", language='rust', font_size=40)[2][0].shift( 2* DOWN + 2 * RIGHT)
        self.play(AnimationGroup(
            Write(not_equals),
            Write(struct),
        ))
        self.wait(2)
        self.play(FadeOut(Group(not_equals, struct)))
        link = octicon('link-24', fill_color=TEAL_D, color=TEAL_D, fill_opacity=0.8).rotate(-0.25*PI).scale(0.75).shift(.75 * RIGHT)
        self.play(Transform(dyn_error, link))
        self.wait(4)
        box = Code(code=' Box<dyn std::error::Error>', language='rust', font_size=40)[2][0]
        _dyn_error = box[len(' Box<'):-1]
        self.play(
            Transform(dyn_error, _dyn_error),
            FadeOut(ferris),
        )
        self.wait(4)
