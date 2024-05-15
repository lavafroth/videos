#!/usr/bin/env python
# coding: utf-8

from manim import *

class OverlayFS(Scene):
    def construct(self):
        podman = SVGMobject("podman").scale(1.5)
        docker = SVGMobject("docker", fill_color='#1D63ED', stroke_color=BLUE, fill_opacity=0.6)
        container =  SVGMobject("container", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6).shift(2*RIGHT)
        daemon =  SVGMobject("daemon", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6).shift(5*RIGHT).scale(0.5)
        x =  SVGMobject("x", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6).shift(5*RIGHT).scale(0.6)
        self.play(FadeIn(docker))

        self.wait(3)
        self.play(Transform(docker, podman))
        self.wait()
        self.play(docker.animate.shift(3 * LEFT))
        self.play(AnimationGroup(FadeIn(container), FadeIn(daemon)))
        self.play(Write(x))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(daemon), FadeOut(x)))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(container), FadeOut(docker)))
