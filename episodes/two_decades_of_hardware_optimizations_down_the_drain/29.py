#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        dump = (
            Code('pdf_cont.c', font_size=22)[2]
            .to_edge(UL)
            .scale(0.6)
            .shift(8.5 * UP)
        )

        loop_rest = [dump[:31], dump[66:]]
        loop = dump[31:66]

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

        dump.shift(3.5 * LEFT)
        self.add(dump)

        self.play(FadeOut(dump))
