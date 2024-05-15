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

        loop = Code("pdf_loop.c", font_size=22)[2].to_edge(LEFT).shift(UP)
        self.add(loop)
        self.wait(2)
        sse = Text("SSE").shift(3.5 * RIGHT)
        self.play(Write(sse))
        sse_ = Paragraph("""Streaming
SIMD
Extensions""").shift(3.5 * RIGHT)
        self.play(Transform(sse, sse_))
        self.wait(4)
        self.play(FadeOut(x) for x in (sse[0], sse[2]))
        self.wait(2)
        simd_ = Paragraph("""Single
Instruction
Multiple
Data""").shift(3.5 * RIGHT)
        simd = sse[1]
        self.play(Transform(simd, simd_))
        self.wait(2)

        for symbol in ("+", "-", r"$\times$", "/", "+"):
            sq_0 = Square(0.5, fill_color=BLUE, color=BLUE, fill_opacity=0.8).shift(
                0.5 * LEFT
            )
            sq_1 = Square(0.5, fill_color=BLUE, color=BLUE, fill_opacity=0.8).shift(
                0.5 * RIGHT
            )
            sym = Tex(symbol)[0]
            gr = VGroup(sq_1, sym, sq_0)
            gr.shift(3.5 * RIGHT)
            self.play(Transform(simd, gr), run_time=0.5)
            self.wait(0.5)
        self.wait(1)
        oldgr = simd

        # the naming is absolutely ridiculous!
        grgr = [oldgr]
        for x in range(3):
            gr_ = oldgr.copy().set_opacity(0)
            gr__ = oldgr.copy().shift(.7 * DOWN)
            self.play(Transform(gr_, gr__), run_time=.25)
            oldgr = gr_
            grgr.append(gr_)
        self.play(FadeOut(x) for x in grgr)
