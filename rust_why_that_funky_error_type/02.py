#!/usr/bin/env python
# coding: utf-8
from manim import *

class EnumBlock(Scene):
    def construct(self):
        enum = Text("enum", font_size=50, font='monospace')
        result = Code(code="Result<T, E>", language='rust')[2][0].shift(3 * UP).scale(1.5)
        self.add(enum)
        self.add(result)
        enum_def = Code(code="""enum Result<T, E> {
   Ok(T),
   Err(E),
}""", language='rust', font_size=40)[2]
        _enum = enum_def[0][:4]
        _result = enum_def[0][5:17]
        _remaining = VGroup(enum_def[0][18:], enum_def[1:])
        self.play(Transform(enum, _enum))
        self.play(Transform(result, _result))
        self.play(Write(_remaining))
        self.wait(2)
