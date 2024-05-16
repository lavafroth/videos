#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        workflow = octicon('workflow-24', fill_color=WHITE).scale(0.5)
        self.play(Write(workflow))
        log = octicon('log-24', fill_color=WHITE).scale(0.5).shift(0.5 * RIGHT)
        self.play(
            workflow.animate.shift(1 * LEFT),
            FadeIn(log)
        )
        self.play(
            workflow.animate.to_edge(UL).shift(2 * DOWN + 2 * RIGHT),
            log.animate.to_edge(DL).shift(2 * UP + 2 * RIGHT),
        )

        code = Code('m01_snippet.rs', font_size=20).shift(2 * RIGHT)[2]
        self.play(FadeIn(code))
        self.wait(2)
        self.play(Transform(code, Code('m02_snippet.rs', font_size=20).shift(1.5 * RIGHT)[2]))
        self.wait(2)
        self.play(Transform(code, Code('m03_snippet.rs', font_size=20).shift(2 * RIGHT)[2]))
        self.wait(4)
        self.play(FadeOut(x) for x in (log, workflow, code))
