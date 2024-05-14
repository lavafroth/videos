#!/usr/bin/env python
# coding: utf-8

from manim import *

class Sc(Scene):
    def construct(self):
        match = Code(code='let handle = match std::fs::File::open("file.txt") {\n\tOk(handle) => handle,\n\tErr(e) => {\n\t\treturn Err(e.into());\n\t},\n};', language='rust', font_size=32)[2]
        self.add(match)
        self.play(FadeOut(match[:2]), FadeOut(match[-1]))
        e, r, b = match[2:5]
        _e = Circle(radius=0.2, color=WHITE, fill_color=WHITE, fill_opacity=0.6).move_to(e.get_center()+LEFT)
        _r = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=0.5).move_to(r.get_center()+LEFT)
        _b = Circle(radius=0.1, color=WHITE, fill_color=WHITE, fill_opacity=0.8).move_to(b.get_center()+LEFT)
        self.play(
            Transform(e, _e),
            Transform(b, _b),
            Transform(r, _r),
        )
        self.play(
            r.animate.shift(8 * UP),
            e.animate.shift(10 * UP),
            b.animate.shift(12 * UP),
            run_time=2
        )        
