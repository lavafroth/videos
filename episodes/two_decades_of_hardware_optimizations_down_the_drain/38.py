#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        box = octicon('device-desktop-24', fill_color=WHITE).scale(0.6)
        tw = Text('Since 1999').shift(DOWN)
        self.add(box, tw)
        self.wait(6)
        
        sse = Text('SSE', font="Terminess Nerd Font Propo")
        tw_ = Text('1999').shift(DOWN)
        self.play(Transform(box, sse), Transform(tw, tw_))
        grp = Group(box, tw)
        avx_full = Paragraph('Advaced\nVector\neXtensions').shift(.5 * UP)
        avx = Text('AVX', font="Terminess Nerd Font Propo")
        tw = Text('2011').shift(DOWN)
        grp1 = Group(avx_full, tw)
        self.play(grp.animate.shift(3 * LEFT), FadeIn(grp1))
        self.wait(3)
        self.play(Transform(avx_full, avx))
        avx = Text('AVX-512', font="Terminess Nerd Font Propo")
        tw = Text('2017').shift(DOWN)
        grp2 = Group(avx, tw)
        grp2.shift(3 * RIGHT)
        self.play(FadeIn(grp2))
        self.wait(3)
        file = octicon('file-binary-24', fill_color=WHITE).scale(0.5).set_opacity(0)
        arr = Arrow(.3 * UP, 2.5 * UP)
        com = octicon('gear-24', fill_color=WHITE).scale(0.3)
        com1 = octicon('gear-16', fill_color=WHITE).scale(0.3 * 16/ 24).shift(0.35 * DR)
        compiler = Group(com, com1)
        comp = Text('compiles', font_size=24).shift(1.5 * UP + RIGHT)
        compiler.shift(0.9 * UP + RIGHT)
        self.play(
            file.animate.set_opacity(1).shift(3 * UP),
            Create(arr),
            FadeIn(comp),
            FadeIn(compiler)
        )
        self.wait(2)
        run = octicon('rel-file-path-24',fill_color=WHITE).scale(0.4).shift(4 * LEFT + UP)
        self.play(
            file.animate.shift(3 * LEFT + 2 * DOWN),
            FadeIn(run),
            FadeOut(arr),
            FadeOut(comp),
            FadeOut(compiler)
        )
        curve = ParametricFunction(lambda t: np.array([0.1 * np.sin(PI * t), 0, 0]), t_range=[0, 4]).move_to(file.get_center())
        self.play(AnimationGroup(file.animate.set(fill_color=RED)), MoveAlongPath(file, curve))
        self.wait(3)
        self.play(FadeOut(file, run))
        self.play(FadeOut(grp, grp1, grp2))
