#!/usr/bin/env manim
from manim import *

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

        cmp = loop[-2][-len('cmp rcx, 0x2803'):]
        jmp = loop[-1][-len('jne 0x88e0'):]
        grp = Group(cmp, jmp)
        grp_ = grp.copy()
        grp.move_to(ORIGIN + 3.5 * RIGHT).scale(2)

        self.add(dump)

        # this was all exposition
        hex = cmp[-len('0x2803'):]
        hex_ = hex.copy()
        color = hex[0].color
        dec = Text('10243', font_size=22 * 0.6 * 2, font="Terminess Nerd Font Propo", color=color).move_to(hex)
        self.play(Transform(hex, dec))
        self.wait(7)
        self.play(Transform(hex, hex_))
        self.play(Transform(grp, grp_))
