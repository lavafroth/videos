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
        bench_init_01 = Code('benchmark_init.rs', font_size=28)[2].shift(.5 * LEFT)
        bench_init_02 = Code('benchmark_init_02.rs', font_size=28)[2].shift(.5 * LEFT)
        self.play(FadeIn(bench_init_01))
        self.wait(1)
        self.play(Transform(bench_init_01, bench_init_02))
        self.wait(2)
