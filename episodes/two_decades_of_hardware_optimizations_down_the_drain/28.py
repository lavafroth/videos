#!/usr/bin/env manim
from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from custom import CodeTransformer, octicon


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        dump = Code('pdf_cont_min.c', font_size=22)[2]
        dump.scale(0.6)
        dump.shift((3.5 + .16) * LEFT + .0265 * DOWN)

        start = 9
        end = 44
        loop_rest = [dump[:start], dump[end:]]
        loop = dump[start:end]

        for i, line in enumerate(loop):
            if i == 0 or i == len(loop) - 1:
                loop_rest.append(line[:7])
                continue
            if i in (2, 5, 8, 10):
                loop_rest.append(line[:12])
                continue
            loop_rest.append(line[:7])
            loop_rest.append(line[8:12])

        for x in loop_rest:
            x.set_opacity(0.5)

        self.add(dump)

        rcx = dump[31-22-5][12:]
        self.play(rcx.animate.set_opacity(1))
        instr = rcx[-10:]
        instr_ = instr.copy()
        self.play(instr.animate.shift(ORIGIN + 3.5 * RIGHT).scale(2))
        self.wait(2)
        self.play(Transform(instr, instr_))
        self.wait(2)
        self.play(rcx.animate.set_opacity(.5))
