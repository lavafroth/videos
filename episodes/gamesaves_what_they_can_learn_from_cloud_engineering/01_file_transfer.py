#!/usr/bin/env python
# coding: utf-8

from manim import *

class FileTransfer(Scene):
    def construct(self):
        directory = SVGMobject("file-directory-fill.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        directory.shift(4*LEFT)

        codespace = SVGMobject("codespaces.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        codespace.scale(0.5)
        codespace.shift(4.5 * RIGHT + 0.25 * DOWN)

        dir_codespace_group = AnimationGroup(Write(directory), Write(codespace))
        self.play(dir_codespace_group)
        
        file_icon = SVGMobject("file.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        file_icon.scale(0.3)
        file_icon.shift(4.5*LEFT + 0.25 * UP)

        files = [file_icon]
        file_icon = file_icon.copy()
        file_icon.shift(RIGHT)
        files.append(file_icon)
        file_icon = file_icon.copy()
        file_icon.shift(0.75 * DOWN)
        files.append(file_icon)
        file_icon = files[0].copy()
        file_icon.shift(0.75 * DOWN)
        files.append(file_icon)

        file_group = AnimationGroup((Write(file) for file in files))
        self.play(file_group)

        target = codespace.get_center() + 1.5 * LEFT + 0.2 * DOWN
        for i, file in enumerate(files):
            self.play(
                file.animate.move_to(target + i/8 * (RIGHT + UP))
            )

        run_icon = SVGMobject("rel-file-path.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        run_icon.scale(0.4)
        run_icon.shift(0.5 * LEFT + 0.25 * DOWN)

        run_action = []
        for i, file in enumerate(files):
            run_action.append(
                file.animate.shift(2.75 * LEFT)
            )
        run_action = AnimationGroup(
            *run_action,
            FadeOut(directory),
            Transform(codespace, run_icon)
        )

        self.play(run_action)

        self.wait(4)
