#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        lines = []
        for char in 'wtf?':
            codepoint = ord(char)
            binary_repr = '{0:08b}'.format(codepoint)
            textobj = Text(binary_repr, t2c={'1':GRAY, '0': GRAY_D}, font=codefont)
            lines.append(textobj)

        lines =VGroup(*lines).arrange(DOWN, buff=.1)
        self.play(Write(lines))
        tfmrs = []
        for real, line in zip(lines, lines.copy().scale(0.5)):
            literal_line = Line(line.get_edge_center(LEFT), line.get_edge_center(RIGHT), buff=0.2, stroke_width=5)
            tfmrs.append(Transform(real, literal_line))

        fil = SVGMobject('file-thin', stroke_color=WHITE, stroke_width=5).shift(UP * 0.2)
        self.play(AnimationGroup(*tfmrs), Write(fil))

        fils = VGroup(fil, lines)
        py = SVGMobject('python-outlined', stroke_color=WHITE, stroke_width=5).shift(5 * DOWN + 3 * RIGHT).rotate(PI/8)

        zero_grav = AnimationGroup(
            fils.animate.shift(LEFT + UP).rotate(PI/6), py.animate.shift(2 * LEFT + 4 * UP).rotate(-PI/6), run_time=6
        )

        ques = Text('?', font=codefont, font_size=70).shift(LEFT + DOWN).rotate(-PI/6)
        zero_grav_write_q = AnimationGroup(
            zero_grav,
            Write(ques),
            lag_ratio=0.4
        )

        self.play(zero_grav_write_q)
        py_ = SVGMobject('python-outlined', stroke_color=WHITE, stroke_width=5)
        self.play(Transform(py, py_), FadeOut(fils, ques))
