#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        file_scale = 0.7
        contents = SVGMobject('contents', fill_color=WHITE).scale(0.35).shift(0.2 * DOWN).scale(file_scale)
        file = octicon('file-24', fill_color=WHITE).scale(file_scale)
        grp = (contents, file)
        for fi in grp:
            fi.shift(5 * LEFT).set_opacity(0)
        self.play((fi.animate.shift(RIGHT).set_opacity(1) for fi in grp), run_time=0.7)
        com = octicon('gear-24', fill_color=WHITE).scale(0.3)
        com1 = octicon('gear-16', fill_color=WHITE).scale(0.3 * 16/ 24).shift(0.35 * DR)
        cogs = Group(com, com1)
        cogs.scale(1.5)
        arrow_0 = Arrow(start=file.get_edge_center(RIGHT), end=cogs.get_edge_center(LEFT)+0.1 * UP)
        self.play(FadeIn(cogs), ReplacementTransform(contents, arrow_0))
        self.play(
            Rotate(com, angle=.5*PI, about_point=com.get_center()),
            Rotate(com1, angle=1.5*PI, about_point=com1.get_center()),
        )
        start = cogs.get_edge_center(RIGHT) + UP *.1
        a = Arrow(start=start, end=start+20*RIGHT)
        self.play(Create(a))
        everything = Group(file, arrow_0, cogs, a)
        self.play(everything.animate.shift(8.5*LEFT))
