#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        dump = Code('pdf_cont_min.c', font_size=22)[2]
        dump.scale(0.6)
        dump.shift(.16 * LEFT + .0265 * DOWN)
        self.add(dump)
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

        self.play(x.animate.set_opacity(0.5) for x in loop_rest)
        self.wait(8)
        cmp = loop[-2][-len('cmp rcx, 0x2803'):]
        jmp = loop[-1][-len('jne 0x88e0'):]
        grp = Group(cmp, jmp)
        self.play(dump.animate.shift(3.5 * LEFT))
        self.play(grp.animate.move_to(ORIGIN + 3.5 * RIGHT).scale(2))
        self.wait(8)
