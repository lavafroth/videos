#!/usr/bin/env manim
# coding: utf-8
from manim import *
class Sc(Scene):
    def construct(self):
        with register_font("Poppins-Light.ttf"):
            Text.set_default(font="Poppins")
        dom = Text("chrs.dev")
        slash = Text('/')
        complete = Text('chrs.dev/blog/clean-code-rust')
        self.play(Write(dom))
        self.wait(2)
        self.play(AnimationGroup(
            Transform(dom[:], complete[:len(dom)]), FadeIn(complete[len(dom):]),
            lag_ratio=0.3
        )) 
        self.wait(3)
        onscreen = Group(dom, complete[len(dom):])
        circle = Circle(radius=0.25, color=WHITE, fill_color=WHITE, fill_opacity=1)
        self.play(Transform(onscreen, circle))





