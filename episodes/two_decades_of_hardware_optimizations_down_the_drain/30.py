#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        self.wait(3)
        normal_ins = Paragraph("""movss
addps
mulps""", font="Terminess Nerd Font Propo")
        for line in normal_ins:
            self.play(Write(line[:-2]))
        self.wait(2)
        self.play(Write(line[-2:]) for line in normal_ins)
        self.wait(4)
        loop = Code("pdf_loop.c", font_size=22)[2].to_edge(LEFT).shift(LEFT + UP).set_opacity(0)
        self.play(loop.animate.shift(RIGHT).set_opacity(1), normal_ins.animate.shift(3.5 * RIGHT))
        self.wait(1)
        movss = normal_ins[0]
        start = len('f30f1058c4     ')
        end = start + len('movss')
        movss_ = loop[11][start:end]

        addps = normal_ins[1]
        addps_ = loop[30][start:end]

        mulps = normal_ins[2]
        mulps_ = loop[29][start:end]

        self.play(Transform(movss, movss_))
        self.play(Transform(addps, addps_))
        self.play(Transform(mulps, mulps_))
        self.wait(2)
