#!/usr/bin/env manim
from manim import *

def str_to_text_mobject(i: int, s: Text):
    shift = i * 0.5 * DOWN
    return s.to_edge(UL).shift(shift)

class CodeBlock(Scene):
    def construct(self):
        drawables = [
            Text("fuse-overlayfs \\", font_size="28", font="monospace"),
            Text("-o lowerdir=lowerdir,upperdir=upperdir,work=work game", t2c={"upperdir": TEAL, "work":YELLOW, "lowerdir": BLUE}, font_size="28", font="monospace"),
        ]
        drawables = [
            str_to_text_mobject(i, s)
            for i, s in enumerate(drawables)
        ]
        for i, drawable in enumerate(drawables):
            self.play(Write(drawable))
        self.wait(2)
        
        horizontal_line = DashedLine(start=np.array([-8, 2.25, 0]), end=np.array([8, 2.25, 0]), color=GRAY)
        self.play(Create(horizontal_line))

        lowerdir = Square(color=BLUE, fill_opacity=0.6).shift(3 * DOWN).rotate(PI / 4)
        lowerdir.apply_function(lambda p: np.array([
            p[0],
            p[1] * 0.5,
            0
        ]))
        upperdir = lowerdir.copy().set_fill(TEAL).set_stroke(TEAL).shift(UP)
        workdir = upperdir.copy().set_fill(YELLOW).set_stroke(YELLOW).shift(UP)

        self.play(AnimationGroup(
            Create(lowerdir),
            Create(upperdir),
            Create(workdir),
        ))

        mergeddir = upperdir.copy().set_fill(WHITE).set_stroke(WHITE)

        self.play(
            AnimationGroup(
                Transform(lowerdir, mergeddir),
                Transform(upperdir, mergeddir),
                Transform(workdir, mergeddir),
            )
        )

        self.wait(4)
