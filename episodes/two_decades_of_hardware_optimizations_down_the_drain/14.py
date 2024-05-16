#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        nsiter = Text("54,956 ns/iter", font="Terminess Nerd Font Propo")
        self.wait(1)
        self.play(Write(nsiter))
        arr = Arrow(0.75 * UP, 0.75 * DOWN)
        _nsiter = Text("17,141 ns/iter", font="Terminess Nerd Font Propo").shift(DOWN)
        self.play(
            nsiter.animate.shift(UP).set_opacity(0.5), Create(arr), Write(_nsiter)
        )
        self.wait(1)
        line = Line(2.5 * LEFT, 2.5 * RIGHT)
        self.play(
            Transform(arr, line),
            nsiter.animate.shift(0.5 * DOWN).set_opacity(1),
            _nsiter.animate.shift(0.5 * UP),
        )
        grp = Group(arr, nsiter, _nsiter)
        appr = Tex(r"$\approx$").shift(1.3 * RIGHT)
        siz = Text("3.2", font="Terminess Nerd Font Propo").shift(2.5 * RIGHT)
        self.play(grp.animate.shift(2 * LEFT), Write(appr))
        self.play(Write(siz))
        grp = Group(grp, siz, appr)
        self.wait(4)
        accum = Text("accum", font="Terminess Nerd Font Propo").shift(3 * DOWN)
        self.play(
            Write(accum),
            arr.animate.shift(2.5 * UP).set_opacity(0.5),
            nsiter.animate.shift(2.5 * UP).set_opacity(0.5),
            _nsiter.animate.shift(2.5 * UP).set_opacity(0.5),
            appr.animate.shift(2.5 * UP).set_opacity(0.5),
            siz.animate.shift(2.5 * UP).set_opacity(0.5),
        )
        self.wait(1)
        drstrange = [
            Text("accum", font="Terminess Nerd Font Propo").shift(UP + x * DOWN)
            for x in range(1, 5)
        ]
        accums = [
            Text("accum{}".format(x), font="Terminess Nerd Font Propo").shift(
                UP + x * DOWN
            )
            for x in range(1, 5)
        ]

        old_accums = [accum.copy(), accum.copy(), accum.copy(), accum]
        self.play(
            (Transform(old, accum_) for old, accum_ in zip(old_accums, drstrange))
        )

        self.play((Transform(old, accum_) for old, accum_ in zip(old_accums, accums)))
        accums = Group(*old_accums)
        self.wait(1)
        self.play(
            accums.animate.shift(5 * DOWN).fade(1),
            arr.animate.shift(2.5 * DOWN),
            nsiter.animate.shift(2.5 * DOWN),
            _nsiter.animate.shift(2.5 * DOWN).set_opacity(1),
            appr.animate.shift(2.5 * DOWN),
            siz.animate.shift(2.5 * DOWN),
        )

        _siz = Text("8.5", font="Terminess Nerd Font Propo").shift(2.5 * RIGHT)
        __nsiter = Text("6,434 ns/iter", font="Terminess Nerd Font Propo").move_to(_nsiter.get_center())
        self.play(
            nsiter.animate.set_opacity(1),
            appr.animate.set_opacity(1),
            arr.animate.set_opacity(1),
            Transform(siz, _siz),
            Transform(_nsiter, __nsiter),
        )

        self.wait(2)
        self.play(FadeOut(siz, _nsiter, arr, appr, nsiter))
