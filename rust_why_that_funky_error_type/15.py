#!/usr/bin/env python
# coding: utf-8

from manim import *

class Sc(Scene):
    def construct(self):
        try_op = Text('?', font_size=60, font='monospace', color=BLUE_D)
        self.play(Write(try_op))
        self.wait(2)
        let = Code(code='let handle = std::fs::File::open("file.txt")?;', language='rust', font_size=32)[2][0]
        let, q, sem = let[:-2], let[-2], let[-1]
        self.play(Transform(try_op, q), Write(let), Write(sem))
        self.wait(2)
        gro = Group(try_op, let, sem)
        match = Code(code='let handle = match std::fs::File::open("file.txt") {\n\tOk(handle) => handle,\n\tErr(e) => {\n\t\treturn Err(e.into());\n\t},\n};', language='rust', font_size=32)[2]
        self.play(Transform(gro, match))
        self.wait(8)
