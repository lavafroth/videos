#!/usr/bin/env manim
from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from custom import CodeTransformer, octicon


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        nsiter = Text("54,956 ns/iter", font="Terminess Nerd Font Propo").shift(.5 * UP)
        _nsiter = Text("17,141 ns/iter", font="Terminess Nerd Font Propo").shift(.5 * DOWN)
        line = Line(2.5 * LEFT, 2.5 * RIGHT)
        grp = Group(line, nsiter, _nsiter)
        grp.shift(2 * LEFT)
        appr = Tex(r"$\approx$").shift(1.3 * RIGHT)
        siz = Text("3.2", font="Terminess Nerd Font Propo").shift(2.5 * RIGHT)
        self.play(FadeIn(x) for x in (grp, appr, siz))
        self.wait(3)
        grp = Group(grp, siz, appr)
        __nsiter = Text("8,560 ns/iter", font="Terminess Nerd Font Propo").move_to(_nsiter.get_center())
        _siz = Text("6.4", font="Terminess Nerd Font Propo").shift(2.5 * RIGHT)
        self.play(Transform(_nsiter, __nsiter), Transform(siz, _siz))
        self.wait(2)

        accum = Text("accum", font="Terminess Nerd Font Propo").shift(3 * DOWN)
        self.play(
            Write(accum),
            line.animate.shift(2.5 * UP).set_opacity(0.5),
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
            line.animate.shift(2.5 * DOWN),
            nsiter.animate.shift(2.5 * DOWN),
            _nsiter.animate.shift(2.5 * DOWN).set_opacity(1),
            appr.animate.shift(2.5 * DOWN),
            siz.animate.shift(2.5 * DOWN),
        )

        _siz = Text("11.0", font="Terminess Nerd Font Propo").shift(2.5 * RIGHT)
        __nsiter = Text("5,002 ns/iter", font="Terminess Nerd Font Propo").move_to(_nsiter.get_center())
        self.play(
            nsiter.animate.set_opacity(1),
            appr.animate.set_opacity(1),
            line.animate.set_opacity(1),
            Transform(siz, _siz),
            Transform(_nsiter, __nsiter),
        )

        
        accums = [
            Text("accum{}".format(x), font="Terminess Nerd Font Propo").shift(
                5 * DOWN + x * DOWN
            )
            for x in range(1, 5)
        ]
        accums = Group(*accums)

        self.wait(2)
        self.play(FadeOut(siz, _nsiter, line, appr, nsiter))
        self.play(accums.animate.move_to(ORIGIN))
        self.wait(6)
        file = octicon('file-24', fill_color=WHITE).scale(0.6).shift(1.5 * UP)
        self.play(Transform(accums, file))
        arr = Arrow(UP, DOWN)
        bins = SVGMobject('binary-code-algorithm-svgrepo-com.svg', fill_color=WHITE).scale(0.6).shift(1.5 * DOWN)
        self.play(Write(bins), Create(arr))
        self.wait(6)
        grp = Group(accums, arr, bins)
        r2 = Text('radare2',  font="Terminess Nerd Font Propo")
        self.play(Transform(grp, r2))
        self.wait(8)

