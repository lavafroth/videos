#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        bench = Code("benchmark_init_02.rs", font_size=28)[2].shift(0.5 * LEFT)
        self.add(bench)
        offt = len("fn init(count: usize) -> ")
        size = len("Vec<Shape>")
        end = offt + size
        start = offt
        focus = bench[0][start:end]
        _focus = Code(code="Vec<Shape>", font_size=40, language="rust")[2][0]
        rest = Group(bench[1:], bench[0][:start], bench[0][end:])
        self.play(Transform(focus, _focus), FadeOut(rest))
        l, shape, r = focus[:4], focus[4:-1], focus[-1:]
        shape_copy = shape.copy()
        l_copy = l.copy()
        r_copy = r.copy()

        ferris = SVGMobject('rustacean-flat-gesture').scale(.6).shift(4.5 * RIGHT)
        ferris_old = ferris.copy().shift(RIGHT).set_opacity(0)
        self.play(Transform(ferris_old, ferris))
        boxes = Rectangle(
            width=4,
            height=1,
            grid_xstep=1,
            fill_opacity=0.8,
            fill_color=BLUE,
            color=BLUE,
        )
        ferris_down = SVGMobject('rustacean-flat-gesture-down').scale(.6).shift(4.5 * RIGHT)
        self.play(
            Transform(shape, boxes),
            Transform(ferris_old, ferris_down),
            l.animate.move_to(boxes.get_edge_center(LEFT) + LEFT),
            r.animate.move_to(boxes.get_edge_center(RIGHT) + 0.5 * RIGHT),
        )

        size_hint = Text('4 bytes', font_size=24).shift(1.5 * DOWN)
        brace = Brace(shape, sharpness=0.7)
        self.play(Write(size_hint), Write(brace))
        self.wait(4)
        ferris_old_copy = ferris.copy().shift(RIGHT).set_opacity(0)
        self.play(
            Transform(ferris_old, ferris),
            Transform(shape, shape_copy), Transform(l, l_copy), Transform(r, r_copy),
            FadeOut(size_hint), FadeOut(brace),

        )
        self.play(
            FadeOut(focus),
            Transform(ferris_old, ferris_old_copy)
        )
