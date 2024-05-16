#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        bench = Code('benchmark_snippet.rs')[2]
        bench_refactor = Code('benchmark_sum4.rs')[2]
        self.play(Write(bench))
        self.wait(2)
        iter_body = bench[5:11]
        end = bench[11:]
        start = bench[:5]
        self.play(Unwrite(iter_body))
        self.play(
            Transform(end, bench_refactor[-2:]),
            Transform(start, bench_refactor[:5])
        )

        body = bench_refactor[6:18]
        self.play(Write(body))
        self.wait(2)
        nsiter = Text('54,956 ns/iter', font='Terminess Nerd Font Propo')
        _nsiter = nsiter.copy().shift(8 * UP).set_opacity(0)
        group = Group(start, body, end)
        _group = group.copy().shift(8 * DOWN).set(opacity=0)
        self.play(Transform(group, _group), Transform(_nsiter, nsiter))
        self.wait(4)
        nsiter = Text('17,725 ns/iter', font='Terminess Nerd Font Propo')
        self.play(Transform(_nsiter, nsiter))
        self.wait(8)
        cpu = octicon('cpu-24', fill_color=WHITE)
        self.play(Transform(_nsiter, cpu))
        cpu_l = cpu.copy()
        cpu_r = cpu.copy()
        cpu_el = cpu.copy()
        cpu_er = cpu.copy()
        self.play(
            cpu_l.animate.scale(0.8).shift(2.2 * LEFT).set_opacity(0.8),
            cpu_r.animate.scale(0.8).shift(2.2 * RIGHT).set_opacity(0.8),
            cpu_el.animate.scale(0.6).shift(4 * LEFT).set_opacity(0.6),
            cpu_er.animate.scale(0.6).shift(4 * RIGHT).set_opacity(0.6),
        )
        self.wait(4)
        self.play(FadeOut(x) for x in (cpu_l, cpu_r,cpu_el, cpu_er, _nsiter))
