#!/usr/bin/env manim
from manim import *

class CodeBlock(Scene):
    def construct(self):
        sudo = Text("sudo", font="monospace", font_size=40)
        self.play(Write(sudo))
        self.wait(8)
        self.play(FadeOut(sudo))
