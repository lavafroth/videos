#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont)

        t = MonoText("python-xasm", font_size=50)
        self.play(Write(t))
        self.wait(2)
        metadata = octicon('checklist-24', fill_color=WHITE).scale(0.7)
        meta_text = Text('metadata', font=codefont, font_size=32)
        VGroup(metadata, meta_text).arrange(DOWN, buff=0.2)
        self.play(t.animate.to_edge(UP), Write(metadata), Write(meta_text))
        req = """
# pydisasm version 4.0.0
# Python bytecode 3.11  (3379)
# Disassembled from Python 3.11.9  (default, Jul 11 2024, 17:51:08)
# [GCC 4.2.1 Compatible Linux LLVM 9.1.0 (clang-902.0.39.2)]
# Source code size mod 2**32: 23 bytes
# Method Name:       <module>
# Filename:         exec
# Argument count:    0
# Kw-only arguments: 0
# Number of locals:  0
# Stack size:        3
# Flags:             0x00000040 (NOFREE)
# First Line:        1
# Constants:
#    0: 1
#    1: 2
#    2: None
# Names:
#    0: a
#    1: b
#    2: print"""

        req_wtf = """# Argument count:    ???
# Kw-only arguments: ???
# Number of locals:  ???
# Stack size:        ???
# Flags:             ???
# First Line:        ???
# Constants:         ???"""
        req_t = req
        req_wtf_t = req_wtf
        req = MonoParagraph(req, color=GRAY).shift(2 * DOWN).to_edge(LEFT)
        req_wtf = MonoParagraph(req_wtf, color=GRAY).shift(1.03 * UP).to_edge(LEFT)
        surr = SurroundingRectangle(req[11], color=BLUE, corner_radius=0.1)
        self.play(ReplacementTransform(metadata, req), FadeOut(meta_text))
        self.play(Create(surr))
        cut = 8
        self.play(
            AnimationGroup(
                FadeOut(req[:cut]),
                AnimationGroup(
                    req[cut:].animate.shift(3 * UP), surr.animate.shift(3 * UP)
                ),
                lag_ratio=0.5,
            )
        )
        surr_ = SurroundingRectangle(req[-8:], color=BLUE, corner_radius=0.1)
        self.play(Transform(surr, surr_))
        self.wait(3)
        anims = []
        for i, (a, b) in enumerate(zip(req_wtf, req[cut:-7])):
            # anims.append(Transform(b, a))
            end = -18 if i == 4 else -1
            anims.append(Transform(b[end:], a[-3:]))
        self.play(FadeOut(surr, req[-7:]), AnimationGroup(*anims))
        self.wait(1)
