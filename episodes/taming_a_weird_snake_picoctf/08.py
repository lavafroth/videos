#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        with open('assets/codes/snake.c') as f:
            contents = f.read().splitlines()[66:86]

        t = MonoParagraph('\n'.join(contents)).to_edge(UL)
        t_ = t.copy().shift(8 * DOWN).set_opacity(0)
        self.play(ReplacementTransform(t_, t))
        eye = SVGMobject('eyes').scale(0.5).shift(5 * RIGHT)
        self.play(FadeIn(eye))
        eye_up = SVGMobject('eyes_up').scale(0.5).shift(3.5 * RIGHT)
        tete = Paragraph('contextual\ncues', font_size=32, alignment='center').next_to(eye_up, DOWN)
        self.play(t.animate.shift(8 * LEFT), Transform(eye, eye_up), Write(tete))
        self.wait(3)
        not_sec_9 = t[7:]
        self.play(not_sec_9.animate.set_opacity(0.4))
        start = 3-21
        end = start+len('snake.py')+2
        codo = t[0][start:end]
        self.play(ripple(codo))
        self.wait(1)
        py = SVGMobject('python').scale(1.2)
        self.play(Transform(codo, py), FadeOut(t[1:], t[0][:start], t[0][end:], eye, tete))
        self.wait(3)

