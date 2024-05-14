#!/usr/bin/env python
# coding: utf-8

from manim import *

class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=0.6)
        layer = square.copy()
        layer.rotate(PI / 4)
        layer.shift(4 * LEFT + 2 * DOWN)
        layer.apply_function(lambda p: np.array([
            p[0],
            p[1] * 0.5,
            0
        ]))
        problem_def = Text("Read-only layer of the assets", font_size=32)
        problem_def.shift(DOWN + 2 * RIGHT)
        self.play(Create(square))
        self.play(Transform(square, layer))
        self.play(Write(problem_def))
        
        upper_layer = square.copy()
        self.play(Create(upper_layer))
        self.play(upper_layer.animate.shift(UP))
        upper_layer_text = Text("writable layer to capture\nchanges during runtime", font_size=32)
        upper_layer_text.shift(0.25 * UP + 2*RIGHT)
        self.play(Write(upper_layer_text))
        self.wait(5)
