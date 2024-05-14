#!/usr/bin/env manim

from manim import *

def str_to_text_mobject(i: int, s: str):
    if i == 2:
        shift = 0.5 * DOWN + RIGHT
    elif i > 2:
        shift = (i - 1) * 0.5 * DOWN
    else:
        shift = i * 0.5 * DOWN
    return Text(s, font_size="28", font="monospace").to_edge(UL).shift(shift)

class CodeBlock(Scene):
    def construct(self):
        drawables = [
            "docker run --rm -it alpine:latest sh",
            "/ # ",
            "ls -l foobar",
            "ls: foobar: No such file or directory"
        ]
        drawables = [
            str_to_text_mobject(i, s)
            for i, s in enumerate(drawables)
        ]
        for drawable in drawables:
            self.play(Write(drawable))

        unwrites = []
        for i, drawable in enumerate(drawables):
            if i == 1:
                continue
            unwrites.append(Unwrite(drawable))

        self.wait(4)
