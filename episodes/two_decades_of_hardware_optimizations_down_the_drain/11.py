#!/usr/bin/env manim
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from custom import CodeTransformer, octicon

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        bench = Code('benchmark_init.rs')[2]
        self.play(FadeIn(bench))
        ferris = SVGMobject('rustacean-flat-gesture').scale(.8).shift(4 * RIGHT)
        ferris_old = ferris.copy().shift(RIGHT).set_opacity(0)
        self.play(Transform(ferris_old, ferris))
        ferris = ferris_old
        start = len('    let mut shapes: ')
        end = len('Vec<Box<dyn Shape>>')+start
        box_dyn = bench[1][start:end]
        box_dyn_ = box_dyn.copy().scale(1.5).move_to(ORIGIN)
        group = Group(bench[1][:start], bench[1][end:], bench[0], bench[2:])
        ferris_down = SVGMobject('rustacean-flat-gesture-down').scale(.8).shift(4 * RIGHT)
        self.play(FadeOut(group), Transform(ferris, ferris_down), Transform(box_dyn, box_dyn_))
        self.wait(6)
        self.play(box_dyn.animate.to_edge(UP))
        self.wait(2)
        box_dyn_ = Code(code='Vec<Box<dyn Shape>>', language='rust', font_size=34).shift(3 * LEFT)[2][0]
        self.play(
            Transform(box_dyn, box_dyn_),
            FadeOut(ferris)
        )
