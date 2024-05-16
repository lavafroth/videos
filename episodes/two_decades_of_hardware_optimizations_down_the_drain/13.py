#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        poly = Text("Polymorphism").shift(3 * LEFT)
        self.add(poly)
        arr = Arrow(0.7 * LEFT, 2.5 * RIGHT)
        enums = Text("Enums").shift(3.5 * RIGHT)
        self.play(Create(arr), Write(enums))
        self.wait(6)
        code = Code("m01_snippet.rs", font_size=28)[2]
        self.play(
            (x.animate.shift(5 * UP).set_opacity(0) for x in (poly, arr, enums)),
            FadeIn(code),
        )
        self.wait(2)
        _code = Code("m02_snippet_min.rs", font_size=28).shift(0.4 * LEFT)[2]
        self.play(Transform(code, _code))
        self.wait(2)
        filename = Text('lib.rs').shift(UP)
        icon = octicon('package-24', fill_color=WHITE).scale(.5)
        self.play(Transform(code, filename), Write(icon))
        self.wait(2)
        lbr = SVGMobject('left_branch', fill_color=WHITE).scale(.25).shift(0.7 * DL)
        rbr = SVGMobject('right_branch', fill_color=WHITE).scale(.25).shift(0.7 * DR)
        down = octicon('arrow-down-24', fill_color=WHITE).scale(.25).shift(DOWN)
        lbr_ = lbr.copy().shift(.2 * UP).set_opacity(0)
        rbr_ = rbr.copy().shift(.2 * UP).set_opacity(0)
        down_ = down.copy().shift(.2 * UP).set_opacity(0)
        self.play(Transform(lbr_, lbr), Transform(rbr_, rbr), Transform(down_, down))
        licon = octicon('package-24', fill_color=WHITE).scale(.5).shift(1.4 * DL)
        ricon = octicon('package-24', fill_color=WHITE).scale(.5).shift(1.4 * DR)
        dicon = octicon('package-24', fill_color=WHITE).scale(.5).shift(2 * DOWN)
        self.play(FadeIn(x) for x in (licon,ricon,dicon))
        grp = Group(code, icon, lbr_, rbr_, down_, licon, ricon, dicon)
        notrait = Code('notrait.rs', font_size=28)[2].shift(2 * RIGHT)
        self.play(grp.animate.shift(3 * LEFT), Write(notrait))
        x_scale = 0.7
        x = [
            Line(start=x_scale * UR, end=x_scale * DL, stroke_width=5, color=RED).shift(2.5 * RIGHT + .2 * UP),
            Line(start=x_scale * UL, end=x_scale * DR, stroke_width=5, color=RED).shift(2.5 * RIGHT + .2 * UP)
        ]
        for line in x:
            self.play(Create(line), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(y) for y in (*x, grp, notrait))

