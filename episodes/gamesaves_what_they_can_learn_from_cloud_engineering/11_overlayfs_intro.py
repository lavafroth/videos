#!/usr/bin/env python
# coding: utf-8

from manim import *

class OverlayFS(Scene):
    def construct(self):
        docker = SVGMobject("docker", fill_color='#1D63ED', stroke_color=BLUE, fill_opacity=0.6)
        self.play(Write(docker))
        self.play(docker.animate.shift(2 * LEFT))

        overlayfs = Text("Overlay Filesystem", font_size=28).shift(2*RIGHT)
        self.play(Write(overlayfs))
        
        self.wait(3)
        _overlayfs = Text("overlayfs", font_size=36, font="monospace").shift(3*UP)
        self.play(AnimationGroup(
            FadeOut(docker),
            Transform(overlayfs, _overlayfs),
            lag_ratio=0.6
        ))


        lowerdir = Square(color=BLUE, fill_opacity=0.6).shift(3 * DOWN + 3 * LEFT).rotate(PI / 4)
        lowerdir.apply_function(lambda p: np.array([
            p[0],
            p[1] * 0.5,
            0
        ]))

        pos = 1.5 * DOWN + 2 * RIGHT

        lowerdir_desc = Text("Read-only lower directory", font_size=28).shift(pos)
        self.play(AnimationGroup(
            Write(lowerdir_desc),
            Create(lowerdir)
        ))

        pos += UP
        upperdir = lowerdir.copy().set_fill(TEAL).set_stroke(TEAL)

        upperdir_desc = Text("Writable upper directory", font_size=28).shift(pos)
        self.play(Create(upperdir))
        self.play(AnimationGroup(
            Write(upperdir_desc),
            upperdir.animate.shift(UP)
        ))

        pos += UP
        workdir_desc = Text("Scratch work directory", font_size=28).shift(pos)
        workdir = upperdir.copy().set_fill(YELLOW).set_stroke(YELLOW)

        self.play(Create(workdir))
        self.play(AnimationGroup(
            Write(workdir_desc),
            workdir.animate.shift(UP)
        ))

        stage = Group(lowerdir, lowerdir_desc, upperdir, upperdir_desc, workdir, workdir_desc, overlayfs)
        _stage = stage.copy().scale(0.5).shift(1.5 * UP)
        self.wait(4)
        self.play(Transform(stage, _stage))
        
        square = (
            Square(color=BLUE, fill_opacity=0.6)
            .rotate(PI / 4)
            .shift(4 * LEFT + 2 * DOWN)
            .apply_function(lambda p: np.array([
                p[0],
                p[1] * 0.5,
                0
            ]))
        )
        problem_def = Text("Read-only layer of the assets", font_size=32).shift(DOWN + 2 * RIGHT)
        
        upper_layer = square.copy().shift(UP)
        upper_layer_text = Text("writable layer to capture\nchanges during runtime", font_size=32).shift(0.25 * UP + 2*RIGHT)

        title = Text("Problem definition", font_size=36, font="monospace").shift(3*UP)
        def_stage = Group(title, square, problem_def, upper_layer, upper_layer_text).scale(0.5).shift(3*DOWN)
        self.play(FadeIn(def_stage))
        self.wait(4)
        self.play(AnimationGroup(FadeOut(stage), FadeOut(def_stage)))
