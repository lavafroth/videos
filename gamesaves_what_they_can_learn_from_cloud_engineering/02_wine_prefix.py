#!/usr/bin/env python
# coding: utf-8

from manim import *

class WinePrefix(Scene):
    def construct(self):
        wine = SVGMobject("wine-glass.svg", fill_opacity=0.8)
        self.play(Write(wine))
        self.wait(3)
        self.play(FadeOut(wine))
        directory = SVGMobject("file-directory-fill.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        self.play(Write(directory))

        package = SVGMobject("package.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        package.scale(0.25)
        package.set_opacity(0)
        package.shift(0.4 * LEFT)
        
        file = SVGMobject("file.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        file.scale(0.3)
        file.shift(0.4 * LEFT)
        file.set_opacity(0)
        
        files = [file]
        file = file.copy()
        file.shift(0.75 * RIGHT)
        files.append(file)
        file = file.copy()
        file.shift(0.75 * UP)
        files.append(file)
        file = files[0].copy()
        file.shift(0.75 * UP)
        files.append(file)

        files[0] = package

        for file in files:
            file_ = file.copy()
            file_.shift(0.5 * DOWN)
            file_.set_opacity(1)
            self.play(Transform(file, file_), run_time=0.5)

        text = Text("WINE prefix")
        text.shift(2 * DOWN)
        self.play(Write(text))

        self.wait(2)
        self.play(FadeOut(text))
        
        self.wait(2)
        self.play(files[2].animate.shift(0.025 * LEFT), run_time=0.1)
        for x in range(4):
            direction = RIGHT if x % 2 == 0 else LEFT
            self.play(files[2].animate.shift(0.05 * direction), run_time=0.1)
        self.play(files[2].animate.shift(0.025 * RIGHT), run_time=0.1)
        
        self.play(files[2].animate.set_fill(RED))
        self.wait(4)
