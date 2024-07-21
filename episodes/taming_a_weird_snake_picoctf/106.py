#!/usr/bin/env manim
from manim import *
from manim import Transform as T, ReplacementTransform as RT, VGroup as V
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=40)
        MonoText.set_default(font=codefont, font_size=32)
        raw = """h at cafe in ~/Documents/picoctf
(python-3.11)   python assets/codes/solve.py 
picoCTF{N0t_sO_coNfus1ng_sn@ke_9433dec6}"""
        t = MonoParagraph(
            raw,
            t2c={
                "h ": ORANGE,
                "cafe": PURPLE,
                "~/Documents/picoctf": GREEN,
                "-3.11": BLUE,
                "python": BLUE,
            },
        )
        self.play(FadeIn(V(t[0], t[1][:14]), shift=2 * UP))
        self.wait(1)
        self.play(Write(t[1][14:]))
        self.play(Write(t[2]))
        self.wait(5)
