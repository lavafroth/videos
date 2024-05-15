#!/usr/bin/env python
# coding: utf-8

from manim import *

class MyScene(Scene):
    def construct(self):
        text = (
            Paragraph("If podman can run rootless containers,\nhow does it mount an overlay?", alignment="center")
            .to_edge(UP)
        )
        self.play(Write(text))

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

        lowerdir_path = ArcBetweenPoints(lowerdir.get_center(), workdir.get_center(), angle=PI, stroke_width=8)
        workdir_path = ArcBetweenPoints(workdir.get_center(), upperdir.get_center(), angle=-PI, stroke_width=8)
        upperdir_path = ArcBetweenPoints(upperdir.get_center(), lowerdir.get_center(), angle=PI, stroke_width=8)
        self.play(AnimationGroup(
            MoveAlongPath(lowerdir, lowerdir_path),
            MoveAlongPath(upperdir, upperdir_path),
            MoveAlongPath(workdir, workdir_path),

            lag_ratio=0.5
         ))
        q_l = Text('?').move_to(lowerdir.get_center())
        q_u = Text('?').move_to(upperdir.get_center())
        q_w = Text('?').move_to(workdir.get_center())
        self.play(AnimationGroup(
            Transform(lowerdir, q_l),
            Transform(upperdir, q_u),
            Transform(workdir,  q_w)
        ))
        self.play(AnimationGroup(
            Transform(lowerdir, workdir),
            Transform(upperdir, workdir)
        ))
        self.play(AnimationGroup(FadeOut(lowerdir),FadeOut(upperdir), FadeOut(workdir)))
        self.wait(3)
        self.play(FadeOut(text))
