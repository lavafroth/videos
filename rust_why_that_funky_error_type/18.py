#!/usr/bin/env python
# coding: utf-8

from manim import *

class Sc(Scene):
    def construct(self):
        t_1 = Code(code='use anyhow::Result;', language='rust', font_size=40)[2][0]
        t_2 = Code(code='Result<T>', language='rust', font_size=40)[2][0]
        self.add(t_1)
        l, o, r = t_1[:12], t_1[12:-1], t_1[-1]
        self.play(FadeOut(l), Transform(o, t_2[:7]), Transform(r, t_2[7:]))
        self.wait(4)
