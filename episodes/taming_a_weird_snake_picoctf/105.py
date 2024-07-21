#!/usr/bin/env manim
from manim import *
from manim import Transform as T, ReplacementTransform as RT
from hackermanim import *
codefont = "Terminess Nerd Font Propo"

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        code = Code('solve.py', font_size=30)[2]
        lis = code[:3]
        l = lis.copy().move_to(ORIGIN).scale(1.2)
        self.play(Write(l))
        self.wait(1)
        self.play(RT(l, lis))

        self.wait(2)
        j = code[4]
        j_ = j.copy().move_to(ORIGIN).scale(1.2)
        self.play(Write(j_))
        self.play(RT(j_, j))
        self.wait(2)
        self.play(Write(code[5]))
        self.play(Write(code[6]))
        self.play(Write(code[7]))
        self.play(Write(code[8]))
        self.wait(1)
        self.play(Write(code[9]))
        lc = code[10]
        self.play(Write(lc[:12]), Write(lc[-1]))
        self.play(Write(lc[-20:-1]))
        self.play(RT(lc[-16:-12].copy(), lc[16:20]), Write(lc[12:16]), Write(lc[20]))

        self.play(Write(code[11]))
        l = code[12]
        self.play(
            Write(l[:9]),
            Write(l[18:26]),
            T(lc[:8].copy(), l[9:18]),
            T(code[0][:10].copy(), l[26:36]),
            Write(l[-2:]),
        )

        l = code[13]
        self.play(Write(l))
        self.play(Write(code[14]))
        self.wait(2)
        l = code[15]
        self.play(
            Write(l[28:53])
        )
        self.play(
            Write(l[-1]),
            Write(l[9]),
        )
        self.play(
            Write(l[16:28]),
        )
        self.play(
            Write(l[10:16]),
            Write(l[:9])
        )
        self.wait(2)

        res = l[:6].copy()
        l = code[16]
        self.play(
            Write(l[15:24]),
            Write(l[30]),
            T(res, l[24:30])
        )
        self.wait(1)
        self.play(
            Write(l[7:15]),
            Write(l[-1]),
        )
        self.play(
            Write(l[:7]),
        )
        self.wait(4)
        self.play(
            Write(code[-1]),
        )
        self.wait(5)
