#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        codefont="Terminess Nerd Font Propo"
        Code.set_default(font=codefont, style="monokai")
        text = Text(
            "key_list.extend(key_list)",
            font=codefont,
            font_size=32,
            t2c={"extend": PURPLE},
        )
        self.play(text.animate.scale(1.1), run_time=.5, rate_func=rate_functions.ease_in_quad)
        self.play(text.animate.scale(1/1.1), run_time=.5, rate_func=rate_functions.ease_out_quad)
