#!/usr/bin/env python
# coding: utf-8

from manim import *

class ExternalStorage(Scene):
    def construct(self):
        directory = SVGMobject("file-directory-fill.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        group = [directory]

        package = SVGMobject("package.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        package.scale(0.25)
        package.set_opacity(1)
        package.shift(0.5 * DOWN + 0.4 * LEFT)
        group.append(package)
        
        file = SVGMobject("file.svg", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        file.shift(0.5 * DOWN + 0.4 * LEFT)
        file.scale(0.3)
        file.set_opacity(1)
        
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
        group += files

        vmob = VMobject()
        for thing in group:
            for inner in thing:
                vmob.add(inner)
        self.play(FadeIn(vmob))
        self.wait(2)
        
        vmob_ = vmob.copy()
        vmob_.scale(0.25)
        vmob_.shift(0.5 * UP + 1.45 * RIGHT)
        
        server = SVGMobject("server", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        server.scale(2)
        
        self.play(AnimationGroup(
            Transform(vmob, vmob_),
            Write(server)
        ))

        self.wait(2)

        server_ = server.copy()
        server_.scale(0.5)
        server_.shift(2 * LEFT)

        self.play(FadeOut(vmob))
        self.play(
            Transform(server, server_)
        )

        bgrect = Rectangle(width=6.0, height=9.0, stroke_color=BLUE).to_edge(UR)
        bgrect.shift(UP + RIGHT)

        self.play(Create(bgrect))

        selector = RoundedRectangle(width=6.0, height=1.2, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.6, corner_radius=0.25).to_edge(UR)
        selector.shift(0.24 * UP+ 1.25 * RIGHT)

        saves = Text(
"""Save 1
2022 06 04 18:32:55

Save 2
2022 10 11 20:29:01

Save 3
2024 03 31 09:22:18

         .
         .
         .
""", font_size=28, font="monospace").to_edge(UR)
        saves.shift(0.2 * RIGHT)

        self.add_foreground_mobject(saves)
        self.play(Write(saves))
        self.play(FadeIn(selector))

        self.play(selector.animate.shift(1.15 * DOWN))
        self.play(selector.animate.shift(1.15 * DOWN))
        self.wait(2)
        self.play(selector.animate.shift(1.15 * UP))
        self.wait(5)
