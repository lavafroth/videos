#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font='Poppins')
        Code.set_default(font=codefont, style="monokai")

        py = SVGMobject('python-outlined', stroke_color=WHITE, stroke_width=5)
        c = Text('C', font_size=320).shift(.1 * LEFT)
        self.add(py)
        self.play(Write(c))
        cpy =VGroup(c, py)
        self.play(cpy.animate.shift(3.5 * LEFT))
        script = octicon('log-24', fill_color=WHITE).scale(.5).shift(3.5 * RIGHT + 3 * UP)
        self.play(FadeIn(script, shift=0.2 * DOWN))
        com = octicon("gear-24", fill_color=WHITE).scale(0.3)
        com1 = (
            octicon("gear-16", fill_color=WHITE).scale(0.3 * 16 / 24).shift(0.35 * DR)
        )
        cogs = Group(com, com1).shift(3.5 * RIGHT).scale(1.5)
        start = script.get_edge_center(DOWN)
        end = cogs.get_edge_center(UP)
        arrow = Arrow(start, (end - start) * UP + start)
        self.play(Create(arrow), FadeIn(cogs, shift=0.2 * DOWN))
        self.play(
            Rotate(com, angle=0.5 * PI, about_point=com.get_center()),
            Rotate(com1, angle=1.5 * PI, about_point=com1.get_center()),
        )
        fb = octicon('file-binary-24', fill_color=WHITE).scale(0.5).shift(3.5 * RIGHT + 3 * DOWN)
        start = cogs.get_edge_center(DOWN)
        end = fb.get_edge_center(UP)
        arrow_1 = Arrow(start, (end - start) * UP + start)
        self.play(Create(arrow_1), FadeIn(fb, shift=0.2 * DOWN))

        fb_ = octicon('file-binary-24', fill_color=WHITE)
        self.play(Transform(fb, fb_), FadeOut(cpy, cogs, arrow, arrow_1, script))

        self.wait(1)
