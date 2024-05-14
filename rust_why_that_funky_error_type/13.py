#!/usr/bin/env python
# coding: utf-8
from manim import *

class Sc(Scene):
    def construct(self):
        code = "Result<T, Box<dyn std::error::Error>>"
        code = Code(code=code, language='rust', font_size=40)[2][0].shift(0.25 * LEFT)
        self.play(Write(code))
        self.wait(6)
        # let's recap!
        result, rest = code[:len('Result')], code[len('Result'):]
        self.play(x.animate.set_opacity(0.5) for x in rest)
        self.wait(2)
        ok = Text('Ok(  )', font_size=40, font='monospace').move_to(rest[1].get_center() + 2 * DOWN + 0.35 * LEFT)
        green = Circle(radius=0.4, color=GREEN, fill_color=GREEN, fill_opacity=0.8).move_to(ok.get_center() + 0.39 * RIGHT)
        arrow = Arrow(start=green.get_center() + 0.25 * DOWN, end=rest[1].get_center())
        old_res = result.copy()
        rest_one = rest[1]
        rest_one_copy = rest_one.copy()
        rest_one_ = rest[1].copy().shift(0.1 * UP).set_opacity(1)
        self.play(Transform(result, ok), FadeIn(green), Create(arrow), Transform(rest_one, rest_one_))
        self.wait(2)
        rest_two = rest[len('<T, '):-1]
        rest_two_copy = rest_two.copy()
        rest_two_ = rest_two.copy().shift(0.1 * UP).set_opacity(1)
        ok = Text('Err(  )', font_size=40, font='monospace').move_to(rest_two.get_center() + 2 * DOWN + 0.3 * LEFT)
        red = Circle(radius=0.4, color=RED, fill_color=RED, fill_opacity=0.8).move_to(ok.get_center() + 0.57 * RIGHT)
        _arrow = Arrow(start=red.get_center() + 0.25 * DOWN + 0.08 * LEFT, end=rest_two.get_center())
        self.play(
            Transform(result, ok),
            Transform(green, red),
            Transform(arrow, _arrow),
            Transform(rest_one, rest_one_copy),
            Transform(rest_two, rest_two_),
        )
        self.wait(2)
        self.play(Transform(rest_two, rest_two_copy), FadeOut(green), FadeOut(arrow), Transform(result, old_res))
        self.play(x.animate.set_opacity(1) for x in rest)
        self.wait(2)
        _nucode = "Box<dyn std::error::Error>"
        _nucode = Code(code=_nucode, language='rust', font_size=40)[2][0]
        nucode = code[len('Result<T, '):-1]
        self.play(
            code[:len('Result<T, ')].animate.shift(20 * LEFT),
            code[-1].animate.shift(20 * RIGHT),
            Transform(nucode, _nucode)
        )
        self.wait(2)
