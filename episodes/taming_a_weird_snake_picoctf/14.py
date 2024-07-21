#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font='Poppins')
        Code.set_default(font=codefont, style="monokai")

        vm = SVGMobject('server-24').set_z_index(1).scale(0.7)
        self.play(FadeIn(vm))
        self.play(vm.animate.shift(3.5 * LEFT))
        neq = Tex(r'$\neq$').scale(2)
        self.play(Write(neq))
        self.wait(3)
        self.play(FadeOut(neq), vm.animate.move_to(ORIGIN))
