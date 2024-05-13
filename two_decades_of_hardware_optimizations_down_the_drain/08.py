#!/usr/bin/env manim
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        line = Line(10 * LEFT, 10 * RIGHT)
        self.add(line)
        cmd = Text('cargo bench', font="Terminess Nerd Font Propo").shift(.5 * UP + 10 * RIGHT)
        self.play(cmd.animate.shift(10 * LEFT), run_time=0.5)
        self.wait(1)
        self.play(cmd.animate.shift(10 * LEFT), run_time=0.5)
