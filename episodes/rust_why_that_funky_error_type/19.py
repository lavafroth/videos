#!/usr/bin/env python
# coding: utf-8

from manim import *

class Sc(Scene):
    def construct(self):
        t_2 = Code(code='Result<T>', language='rust', font_size=40)[2][0]
        self.add(t_2)
        t_3 = Code(
code='''let content = fs::read(path)
              .with_context(|| format!(
                 "Failed to config from {}",
                 path.display()
              ))?;''',
                language='rust', font_size=34)[2].shift(0.3 * LEFT)
        self.play(Transform(t_2, t_3[0]))
        self.play(Write(t_3[1:]))
        self.wait(4)
        self.play(FadeOut(t_3), FadeOut(t_2))
