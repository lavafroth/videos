#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        
        c0 = '''This type/pattern is a quick fix but
shouldn't generally be used in library code.'''
        c1 = '''
It should be mentioned that if you're
writing code that anyone else is supposed
to use ... make an error enum, use thiserror
instead of anyhow.'''.strip()
        p0 = Paragraph(c0, font_size=22).to_edge(LEFT).shift(UP)
        surr_0 = SurroundingRectangle(p0, corner_radius=.2, color=TEAL, fill_color=TEAL, fill_opacity=.3)
        g_0 = Group(p0, surr_0)
        g_old_0 = g_0.copy().shift(5 * LEFT).fade(1)
        
        p1 = Paragraph(c1, font_size=22).to_edge(DR)
        surr = SurroundingRectangle(p1, corner_radius=.2, color=BLUE, fill_color=BLUE, fill_opacity=.3)
        g = Group(p1, surr)
        g_old = g.copy().shift(8 * RIGHT).fade(1)
        self.play(Transform(g_old, g),Transform(g_old_0, g_0))
        self.wait(3)
        self.play(FadeOut(g_old, g_old_0))
