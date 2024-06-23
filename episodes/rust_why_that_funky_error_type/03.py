#!/usr/bin/env python
# coding: utf-8

from manim import *

class EnumBlock(Scene):
    def construct(self):
        enum_def = Code(code="""enum Result<T, E> {
   Ok(T),
   Err(E),
}""", language='rust', font_size=40)[2]
        self.add(enum_def)
        self.play(enum_def.animate.set_opacity(0.5))
        self.play(enum_def[1].animate.set_opacity(1))
        self.wait(2)
        self.play(
            enum_def[1].animate.set_opacity(0.5),
            enum_def[2].animate.set_opacity(1)
        )
        self.play(enum_def[2].animate.set_opacity(0.5))
        self.wait(2)
        self.play(enum_def.animate.set_opacity(1))
        self.play(enum_def.animate.shift(3*LEFT).scale(0.75))
        _function = Tex("$f$", font_size=100).shift(3*RIGHT + 2 * UP)
        function = _function.copy().shift(0.5 * DOWN).set_opacity(0)
        self.play(Transform(function, _function))
        arrow = Arrow(start=function.get_center() + 0.5 * DOWN, end=function.get_center() + 3.5 * DOWN) 
        self.play(Create(arrow))
        success = Circle(color=GREEN, fill_color=TEAL_A, fill_opacity=0.8, radius=.5).shift(function.get_center() + 4 * DOWN)
        self.play(Create(success))
       
        ok = enum_def[1][:-3].copy()
        _ok = ok.copy().scale(2).move_to(success.get_center()+2 * RIGHT + 0.2 * UP)
        ok_brace = enum_def[1][7].copy()
        _ok_brace = ok_brace.copy().scale(2).move_to(success.get_center() + 0.75 * RIGHT)
        self.play(
            Transform(ok, _ok),
            Transform(ok_brace, _ok_brace),
        )
        self.wait(2)
        self.play(AnimationGroup(FadeOut(ok), FadeOut(ok_brace)))
        success_overlay = success.copy().move_to(enum_def[1][-3].get_center()).scale(0.5).set_opacity(0)
        T = enum_def[1][-3].copy().set_fill(GREEN)
        T2 = enum_def[0][-7].copy().set_fill(GREEN)
        self.play(AnimationGroup(
            Transform(success, success_overlay),
            Transform(enum_def[1][-3], T),
            Transform(enum_def[0][-7], T2)
        ), lag_ratio=0.3)
        self.wait(2)

        failure = Circle(color=RED, fill_color=RED, fill_opacity=0.8, radius=.5).shift(function.get_center() + 4 * DOWN)
        self.play(Create(failure))
        
        ok = enum_def[2][:-3].copy()
        _ok = ok.copy().scale(2).move_to(failure.get_center() + 1.1 * LEFT + 0.1 * UP)
        ok_brace = enum_def[2][8].copy()
        _ok_brace = ok_brace.copy().scale(2).move_to(failure.get_center() + 0.75 * RIGHT)
        self.play(
            Transform(ok, _ok),
            Transform(ok_brace, _ok_brace)
        )
        self.wait(2)
        self.play(FadeOut(ok), FadeOut(ok_brace))
        success_overlay = failure.copy().move_to(enum_def[2][-3].get_center()).scale(0.5).set_opacity(0)
        T = enum_def[2][-3].copy().set_fill(RED)
        T2 = enum_def[0][-4].copy().set_fill(RED)
        self.play(AnimationGroup(
            Transform(failure, success_overlay),
            Transform(enum_def[2][-3], T),
            Transform(enum_def[0][-4], T2)
        ), lag_ratio=0.3)
        self.wait(2)
        self.play(FadeOut(Group(function, arrow)))
        self.wait(4)
        ferris = SVGMobject('../assets/rustacean-flat-gesture').shift(3 * RIGHT)
        self.play(FadeIn(ferris))

        highlight = []
        for t_or_e in (enum_def[2][-3], enum_def[0][-4], enum_def[0][-7], enum_def[1][-3]):
            curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]).move_to(t_or_e.get_center() + 0.05 * UP)
            highlight.append(MoveAlongPath(t_or_e, curve))

        self.play(highlight)
        self.wait(2)
        self.play(
            FadeOut(ferris),
            FadeOut(enum_def[0][:5]),
            FadeOut(enum_def[0][-2:]),
            FadeOut(enum_def[1:]),
        )
        result = enum_def[0][5:-2]
        _result = Code(code="Result<T, Box<dyn std::error::Error>>", language='rust', font_size=40)[2][0].shift(0.2 * LEFT)
        self.play(
            Transform(result[0:len('Result<T, ')], _result[0:len('Result<T, ')]),
            Transform(result[-1], _result[-1]),
            Transform(result[-2], _result[len('Result<T, '):len('Result<T, Box<dyn std::error::Error>')])
        )
        self.wait(2)
