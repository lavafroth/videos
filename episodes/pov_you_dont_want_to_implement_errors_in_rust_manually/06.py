#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        f = Text('#[error]', font=codefont, font_size=40, color=GREEN_D)
        self.add(f)
        bounds = lambda f: (f[:2], f[2:-1], f[-1])
        a, b, c = bounds(f)
        self.play(FadeOut(b), a.animate.scale(3), c.animate.scale(3))
        grp = Group(a, c)
        self.play(grp.animate.shift(4 * LEFT))
        at = Text('attributes', font=codefont, font_size=40, color=GREEN_D).scale(3).shift(.5  * RIGHT)
        self.play(Write(at), c.animate.next_to(at))
        grp = Group(a, at, c)
        self.wait(2)
        self.play(grp.animate.to_edge(UP).scale(0.5))
        ac = Text('active\nattributes').shift(3* LEFT)
        aa = Arrow(start=grp.get_center() + DL/2, end=ac)
        ia = Text('inert\nattributes').shift(3*RIGHT)
        ai = Arrow(start=grp.get_center() + DR/2, end=ia)
        self.play(Write(ac), Create(aa))
        self.play(Write(ia), Create(ai))
        self.play(x.animate.set_opacity(0.5) for x in (grp, ia, aa, ai))
        surr = Rectangle(color=BLUE, width=ac.get_width() + .5, height=ac.get_height() + .5).move_to(ac.get_center())
        self.play(Create(surr))
        self.play(FadeOut(surr))
        grp = Group(grp, ac, ia, aa, ai)
        self.play(grp.animate.shift(7 * UP))
        self.wait(3)
