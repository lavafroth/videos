#!/usr/bin/env python
# coding: utf-8

from manim import *
class MyScene(Scene):
    def construct(self):
        text = (
            Text("Filesystems in the Userspace")
            .to_edge(UP)
        )
        self.wait(4)
        user = SVGMobject("user", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        disk = SVGMobject("disk", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6).scale(0.3).shift(0.5 * DOWN)
        self.play(AnimationGroup(
            Write(text),
            Write(user),
            Write(disk)
        ))
        self.wait()
        _text = Text("FUSE", font_size=50)
        self.play(AnimationGroup(
            Transform(text, _text),
            FadeOut(user),
            FadeOut(disk),
        ))
        self.wait(4)
        podman = SVGMobject("podman", fill_opacity=0.6).shift(4 * LEFT)
        _text = Text("fuse-overlayfs", font="monospace").shift(2.8 * RIGHT)
        arrow = Arrow(start=podman.get_center() + RIGHT, end=_text.get_center() + 2.6 * LEFT)
        self.play(AnimationGroup(
            FadeIn(podman),
            Transform(text, _text),
            Create(arrow)
        ))
        self.wait(4)
        self.play(AnimationGroup(
            FadeOut(podman),
            FadeOut(arrow),
            text.animate.shift(2.8 * LEFT),
        ))
        self.wait(6)
        self.play(
            FadeOut(text),
        )
