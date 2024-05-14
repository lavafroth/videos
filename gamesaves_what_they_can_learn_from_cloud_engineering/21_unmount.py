#!/usr/bin/env manim
from manim import *

class CodeBlock(Scene):
    def construct(self):
        umount = Text("fusermount -u game", font_size="28", font="monospace").to_edge(UL)
        self.play(Write(umount))
        self.wait(2)
        
        horizontal_line = DashedLine(start=np.array([-8, 2.75, 0]), end=np.array([8, 2.75, 0]), color=GRAY)
        self.play(Create(horizontal_line))

        lowerdir = Square(color=BLUE, fill_opacity=0.6).shift(3 * DOWN).rotate(PI / 4).apply_function(lambda p: np.array([
            p[0],
            p[1] * 0.5,
            0
        ]))
        upperdir = lowerdir.copy().set_fill(TEAL).set_stroke(TEAL).shift(UP)
        workdir = upperdir.copy().set_fill(YELLOW).set_stroke(YELLOW).shift(UP)

        mergeddir_0 = upperdir.copy().set_fill(WHITE).set_stroke(WHITE)
        mergeddir_1 = mergeddir_0.copy()
        mergeddir_2 = mergeddir_0.copy()

        self.play(AnimationGroup(
            Create(mergeddir_0),Create(mergeddir_1),Create(mergeddir_2)
        ))

        self.play(
            AnimationGroup(
                Transform(mergeddir_0, lowerdir),
                Transform(mergeddir_1, upperdir),
                Transform(mergeddir_2, workdir),
            )
        )

        self.wait(2)
        self.play(
            AnimationGroup(
                FadeOut(mergeddir_0),
                FadeOut(mergeddir_1),
                FadeOut(mergeddir_2),
                FadeOut(umount),
                FadeOut(horizontal_line)
            )
         )
