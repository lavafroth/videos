#!/usr/bin/env manim

# Yes, the title is a 3b1b reference
from manim import *
class CodeBlock(Scene):
    def construct(self):
        text = Text("???", font_size=60)
        after = Text("...", font_size=60)
        self.play(Write(text))
        self.play(Transform(text, after))
        self.wait(3)
        after = Text((" "*100).join((".",".",".")), font_size=60).shift(6*DOWN)
        self.play(Transform(text, after))
