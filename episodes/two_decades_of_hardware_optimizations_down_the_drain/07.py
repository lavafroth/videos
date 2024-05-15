#!/usr/bin/env manim
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')

        code = Code('benchmark_snippet.rs',  font_size=34)[2]
        self.play(code.animate.scale(0.75).to_edge(LEFT))
        shape_dot_area = code[7][-13:-1]
        shape_dot_area_copy = shape_dot_area.copy()
        self.play(shape_dot_area.animate.scale(1/.75).shift(4.5 * RIGHT + .5 * UP))
        shape = shape_dot_area[:5]
        dot_area = shape_dot_area[5:]

        shapes = [
            Rectangle(width=2, height=1,color=PURPLE, fill_color=PURPLE, fill_opacity=0.6),
            Square(1, color=BLUE, fill_color=BLUE, fill_opacity=0.6),
            Circle(radius=0.5, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.6),
            Triangle(radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=0.6),
        ]
        
        working_shape = shape
        shape_copy = shape.copy()
        for i, next_shape in enumerate(shapes):
            if i == 0:
                offt = 1.2 * LEFT
            else:
                offt = .7 * LEFT
            next_shape.move_to(dot_area.get_edge_center(LEFT) + offt)
            _next_shape = next_shape.copy().shift(5 * UP).set_opacity(0)
            self.play(
                working_shape.animate.shift(5 * DOWN).set_opacity(0),
                Transform(_next_shape, next_shape)
            )
            working_shape = _next_shape

        _next_shape = shape_copy.copy().shift(5 * UP).set_opacity(0)
        self.play(
            working_shape.animate.shift(5 * DOWN).set_opacity(0),
            Transform(_next_shape, shape_copy)
        )
        self.wait(1)
        accum = code[7][3 * 4: 3 * 4 + 5]

        curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1])
        anims = []
        for char in accum:
            curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))

        group = Group(_next_shape, dot_area)
        self.play(Transform(group, shape_dot_area_copy), AnimationGroup(anims, lag_ratio=0.1), run_time=1)
        line = Line(LEFT, 20 * RIGHT)
        self.play(Create(line))
        group = Group(group, code)
        _group = group.copy().shift(8 * LEFT)
        self.play(
            Transform(group, _group),
            line.animate.shift(8 * LEFT),
        )
