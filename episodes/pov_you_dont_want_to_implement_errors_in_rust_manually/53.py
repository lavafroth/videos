#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        ty = Text('Thank you!')
        shoutout = Text("check out dtolnay's other works", font_size=32).next_to(ty, DOWN)
        self.add(ty, shoutout)
