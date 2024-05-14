#!/usr/bin/env python
# coding: utf-8

from manim import *

class Sc(Scene):
    def construct(self):
        t_0 = Text('anyhow', font='monospace', font_size=40)
        self.play(Write(t_0))
        self.wait(4)
        t_1 = Code(code='use anyhow::Result;', language='rust', font_size=40)[2][0]
        l, o, r = t_1[:4], t_1[4:10], t_1[10:]
        self.play(Transform(t_0, o), Write(l), Write(r))
        self.wait(4)
