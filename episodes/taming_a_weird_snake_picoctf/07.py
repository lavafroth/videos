#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        with open('assets/codes/snake.smol') as f:
            contents = f.read()

        t = Text(contents, font=codefont, font_size=32).to_edge(UL)
        self.add(t)
        line = Line(5 * UP, 5 * DOWN)
        t_backup = t.copy()
        t_ = t.copy().scale(0.8).to_edge(UL).shift(1.25 * LEFT + DOWN)
        vg = VGroup(
            Text('File contents', font_size=34),
            Text('x86_64 assembly', font_size=34)
        ).arrange(buff=3.5).to_edge(UP).shift(.5 * RIGHT)
        self.play(Transform(t, t_), Create(line), Write(vg[0]))
        with open('assets/codes/llvm_dis.S') as f:
            contents = f.read()
        
        dis = Text(contents, font=codefont, font_size=32).scale(0.8).to_edge(UP).shift(5.5 * RIGHT + DOWN)
        self.play(FadeIn(dis), Write(vg[1]))
        self.wait(2)

        eq = Text('=')
        n = Line(.15 * UR, .15 * DL)
        self.play(Write(eq), ReplacementTransform(line, n))
        neq = VGroup(n, eq)
        self.play(neq.animate.set(color=RED))
        curve = ParametricFunction(lambda t: np.array([0.1 * np.sin(PI * t), 0, 0]), t_range=[0, 4]).move_to(neq.get_center())
        self.play(
            MoveAlongPath(neq, curve)
        )
        self.wait(3)
        self.play(FadeOut(neq, dis, vg), Transform(t, t_backup))
