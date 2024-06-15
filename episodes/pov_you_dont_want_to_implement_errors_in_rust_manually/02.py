#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        t = Text('thiserror', font=codefont, font_size=40).shift(LEFT)
        e = Text('::Error', font=codefont, t2c={'Error': GREEN}, font_size=40).next_to(t, buff=0.15)
        tegr = Group(t, e)
        self.add(tegr)
        self.play(tegr.animate.shift(1.5 * RIGHT))
        d = (
            Text('#[derive(', font_size=40, font=codefont).next_to(t, direction=LEFT, buff=0.15),
            Text(')]', font_size=40, font=codefont).next_to(e, buff=0.15),
        )
        self.play(map(Write,d))
        self.wait(1)
        code = Code('deriverror.rs', font_size=32)[2]
        objs = [*list(d[0]), *list(t), *list(e), *list(d[1])]
        to = code[0]
        self.play(Transform(a, b) for a, b in zip(objs, code[0]))
        self.play(Write(code[1:]))
        self.wait(1)
