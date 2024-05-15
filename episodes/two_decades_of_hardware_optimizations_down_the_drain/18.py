#!/usr/bin/env manim
from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from custom import CodeTransformer, octicon


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        t = Text('Lookup Table').shift(3 * UP)
        self.play(Write(t))
        t0 = MobjectTable(
            [[Text("Shape", font_size=28), Text("Multiplier", font_size=28)],
            [Text("Circle", font_size=28), Tex(r"$\pi$")],
            [Text("Square", font_size=28), Tex(r"$1$")],
            [Text("Rectangle", font_size=28), Tex(r"$1$")],
            [Text("Triangle", font_size=28), Tex(r"$0.5$")]],
        ).shift(0.5 * DOWN)
        self.play(Write(t0))
        gr = Group(t, t0)
        self.wait(1)
        self.play(gr.animate.shift(3 * LEFT).scale(0.6))

        struct = Code(code='''struct Shape {
    multiplier: f32,
    width: f32,
    height: f32,
}''', language='rust', font_size=34)[2].shift(3 * RIGHT)
        self.play(Write(struct))
        self.wait(2)
        start = len('struct ')
        end = start + len('Shape')
        line = struct[0]
        l, shapetype, r = line[:start], line[start:end], line[end:]
        rest = Group(l, r, struct[1:])
        self.play(FadeOut(rest), FadeOut(t0), FadeOut(t))
        enum = Code(code='''enum ShapeType {
    Square,
    Rectangle,
    Triangle,
    Circle,
}''', language='rust', font_size=34)[2]
        l, shapetype_, r = enum[0][:5], enum[0][5:14], enum[0][14:]
        rest = Group(enum[1:], l, r)
        self.play(Transform(shapetype, shapetype_), FadeIn(rest))
        self.wait(3)

