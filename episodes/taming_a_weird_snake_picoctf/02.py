#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        script = octicon('log-24', fill_color=WHITE).to_edge(UL).scale(0.5)
        rocket = octicon('rocket-24', fill_color=WHITE).to_edge(UR).scale(0.5)
        arrow = CurvedArrow(ORIGIN, script.get_center(), angle=PI/1.4)
        arrow1 = CurvedArrow(ORIGIN, rocket.get_center(), angle=-PI/1.4)
        line = Line(6 * DOWN, ORIGIN)

        script.shift(DOWN)
        rocket.shift(DOWN)

        self.play(Create(line), run_time=0.5, rate_func=rate_functions.ease_in_quad)
        self.play(Create(arrow), FadeIn(script), Create(arrow1), FadeIn(rocket), rate_func=rate_functions.ease_out_quad)
        text = Text('Continue with\nthis script', font_size=36).next_to(script, DOWN).shift(RIGHT)
        text1 = Text('Course correct', font_size=36).next_to(rocket, DOWN).shift(LEFT)
        self.play(Write(text), Write(text1))
        self.wait(1)
        stg = VGroup(script.copy().scale(1.25), text.copy()).arrange(DOWN)
        self.play(Transform(VGroup(script, text), stg), map(FadeOut, (rocket, arrow, arrow1, line, text1)))
        self.wait(2)
