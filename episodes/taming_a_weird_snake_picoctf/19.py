#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        t = Text("python-xasm", font=codefont, font_size=50).to_edge(UP)
        self.add(t)

        req_wtf = """# Argument count:    ???
# Kw-only arguments: ???
# Number of locals:  ???
# Stack size:        ???
# Flags:             ???
# First Line:        ???
# Constants:         ???"""
        req_wtf = (
            Paragraph(req_wtf, font=codefont, font_size=32, color=GRAY)
            .shift(1.03 * UP)
            .to_edge(LEFT)
        )
        self.add(req_wtf)
        self.play(req_wtf.animate.next_to(t, DOWN))
        p = octicon("person-24", fill_color=WHITE).scale(0.7)
        q = (
            octicon("search-24", fill_color=WHITE)
            .scale(0.4)
            .shift(0.5 * DR)
            .rotate(PI, UP)
        )
        person_search = VGroup(p, q)
        com = octicon("gear-24", fill_color=WHITE).scale(0.3)
        com1 = octicon("gear-16", fill_color=WHITE).scale(0.3 * 16 / 24).shift(0.4 * DR)
        cogs = Group(com, com1).shift(3.5 * RIGHT).scale(1.5)

        fb = octicon("file-binary-24", fill_color=WHITE).scale(0.7)
        bottom_row = Group(person_search, cogs, fb).arrange(buff=2).shift(2 * DOWN)
        cogs.shift(RIGHT)
        self.play(
            AnimationGroup(
                (FadeIn(x, shift=0.2 * RIGHT) for x in bottom_row), lag_ratio=0.5
            )
        )
        line = Line(.2 * DL, .6 * UR).shift(2.4 * DOWN + RIGHT).set_opacity(0)
        script = octicon("log-24", fill_color=WHITE).scale(0.5).shift(2 * DOWN + 1 * LEFT)
        t = octicon('triangle-left-24', fill_color=WHITE).shift(3.2 * DOWN + RIGHT).scale(0.2)
        t1 = t.copy().shift(.2 * RIGHT)
        self.play(Transform(fb, line), 
            Rotate(com, angle=-0.5/2 * PI, about_point=com.get_center()),
            Rotate(com1, angle=-1.5/2 * PI, about_point=com1.get_center()), 
            FadeIn(t, shift=.2 * LEFT),
            rate_func=rate_functions.ease_in_quad,
            run_time=.5)
        self.play(
            Transform(fb, script),
            Rotate(com, angle=-0.5/2 * PI, about_point=com.get_center()),
            Rotate(com1, angle=-1.5/2 * PI, about_point=com1.get_center()),
            FadeIn(t1, shift=.2 * LEFT),
            run_time=.5,
            rate_func=rate_functions.ease_out_quad,
        )
        a = Group(person_search.copy(), fb.copy()).arrange(buff=3).shift(2 * DOWN)
        self.play(FadeOut(cogs, t, t1), Transform(person_search, a[0]), Transform(fb, a[1]))
        self.wait(4)
