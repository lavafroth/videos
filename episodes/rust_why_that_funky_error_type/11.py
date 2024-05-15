#!/usr/bin/env python
# coding: utf-8

from manim import *

class Sc(Scene):
    def construct(self):
        c = Circle(radius=1.5, color=WHITE, fill_color=WHITE, fill_opacity=.5)
        circle = Circle(radius=0.3, color=WHITE).shift(0.3 * UL)
        num_points = 20
        angles = [n * (360 / num_points) for n in range(num_points)]
        points = [circle.point_at_angle(n*DEGREES) for n in angles]
        dots = [Circle(radius=0.01, color=WHITE, fill_opacity=1).move_to(p) for p in points]
        self.add(c)
        for dot in dots:
            self.add(dot)
        access = Code(code='let field = trait_object.field;', language='rust', font_size=20)[2].to_edge(DL).shift(2 * UP)
        error = """error[E0609]: no field `field` on type `Box<dyn std::error::Error>`
  --> src/main.rs:15:30
   |
15 |     let field = trait_object.field;
   |                              ^^^^^ unknown field

For more information about this error, try `rustc --explain E0609`."""
        error = Text(error, font_size=20, font='monospace',
                     t2c={
                         '[172:191]': RED,
                         '[0:12]': RED,
                     }
                    ).to_edge(DL).shift(0.2 * DOWN)
        self.play(Write(access))
        curved_arrow = CurvedArrow(start_point=access.get_center() + 0.25 * UP, end_point=circle.get_center(), angle=-PI/2)
        self.play(Create(curved_arrow))
        self.wait(2)
        _c = Circle(radius=1.5, color=WHITE, fill_color=WHITE, fill_opacity=1)
        curve = ParametricFunction(lambda t: np.array([0.1 * np.sin(PI * t), 0, 0]), t_range=[0, 4]).move_to(_c.get_center())
        self.play(Transform(c, _c), FadeOut(curved_arrow))
        self.play(Write(error), MoveAlongPath(c, curve))
        self.wait(4)
        self.play(FadeOut(access), FadeOut(error))
        self.wait(2)
