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
         "tree -L 1",
        """.
├── bin
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
    
18 directories, 0 files"""
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
        self.play(AnimationGroup(unwrites))
        self.play(drawables[1].animate.shift(0.5 * UP))
        touch = "touch foobar"

        self.play(Write(Text(touch, font_size="28", font="monospace").to_edge(UL).shift(RIGHT)))
        prompt = drawables[1].copy().shift(0.5 * DOWN)

        ls = "ls -l foobar"
        self.play(Write(prompt))
        self.play(Write(Text(ls, font_size="28", font="monospace").to_edge(UL).shift(RIGHT+0.5*DOWN)))
        ls_out = '-rw-r--r--    1 root  root  0 Apr  1 12:33 foobar'
        self.play(Write(Text(ls_out, font_size="28", font="monospace").to_edge(UL).shift(DOWN)))
        prompt = prompt.copy().shift(DOWN)
        self.play(Write(prompt))
        self.wait(2)

        exit = "exit"
        self.play(Write(Text(exit, font_size="28", font="monospace").to_edge(UL).shift(RIGHT+1.5*DOWN)))
        self.wait(4)
