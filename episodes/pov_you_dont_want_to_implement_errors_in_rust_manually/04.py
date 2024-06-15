#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        f = Text('#[from]', font=codefont, font_size=40, color=GREEN_D)
        self.add(f)
        bounds = lambda f: (f[:2], f[2:-1], f[-1])
        a, b, c = bounds(f)

        for attr in ('#[source]', '#[backtrace]', '#[error]'):
            _a, _b, _c = bounds(Text(attr, font=codefont, font_size=40, color=GREEN_D))
            self.play(Transform(x, _x) for (x, _x) in (
                (a, _a),
                (b, _b),
                (c, _c)
            ))
            self.wait(1)
        self.wait(3)
