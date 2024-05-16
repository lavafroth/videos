#!/usr/bin/env python
# coding: utf-8
from manim import *
from hackermanim import *

def whitespace_indices(s: str) -> List[int]:
    return [i for i, c in enumerate(s) if c.isspace()]

class OpeningScene(Scene):
    def construct(self):
        t_0 = "Result<T, Box<dyn std::error::Error>>"
        t_1 = "Result<(), Box<dyn std::error::Error>>"
        t_2 = "Result<i64, Box<dyn std::error::Error>>"
        t_3 = "Result<f64, Box<dyn std::error::Error>>"
        t_4 = " Box<dyn std::error::Error>"
        t_0_splits = [len('Result<'), len('Result<T'), len('Result<T, Box<dyn std::error::Error>')] + whitespace_indices(t_0)
        t_1_splits = [len('Result<'), len('Result<()'), len('Result<(), Box<dyn std::error::Error>')] + whitespace_indices(t_1)
        t_2_splits = [len('Result<'), len('Result<i64'), len('Result<i64, Box<dyn std::error::Error>')] + whitespace_indices(t_2)
        t_3_splits = [len('Result<'), len('Result<i64'), len('Result<i64, Box<dyn std::error::Error>')] + whitespace_indices(t_3)
        t_4_splits = whitespace_indices(t_4)
        tfmr = CodeTransformer(t_0, t_0_splits, language='rust', font_size=40)
        tfmr.ingest(t_1, t_1_splits,  language='rust', font_size=40)
        for thing in tfmr.writables():
            self.add(thing)
        self.play(tfmr.unwrites())
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        tfmr.ingest(t_2, t_2_splits, language='rust',  font_size=40)
        self.play(tfmr.unwrites())
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        
        tfmr.ingest(t_3, t_3_splits, language='rust',  font_size=40)
        self.play(tfmr.unwrites())
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        
        tfmr.ingest(t_0, t_0_splits, language='rust',  font_size=40)
        self.play(tfmr.unwrites())
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        self.wait(2)
        
        T = tfmr.post.chunks[1].chunk
        def parametric_curve(t, scale=0.1):
            return np.array([0, scale * np.sin(PI * t), 0])
        curve = ParametricFunction(parametric_curve, t_range=[0, 1]).move_to(T.get_center() + 0.05 * UP)
        self.play(MoveAlongPath(T, curve))
        self.wait(2)

        tfmr.ingest(t_4, t_4_splits, language='rust', font_size=40)
        self.play(tfmr.unwrites())
        self.play(tfmr.transforms())
        self.wait(4)
        self.play(
            chunk.chunk.animate.shift(5 * UP) for chunk in tfmr.post.chunks
        )
