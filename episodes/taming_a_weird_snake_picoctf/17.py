#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont)

        dis = MonoText("dis", font_size=60)
        self.play(Write(dis))
        self.wait(1)
        code = (
            Code(code="import dis\n" "dis.dis(  )", language="python")
            .shift(3.5 * LEFT)[2]
            .scale(2)
        )
        self.play(FadeIn(code[1], code[0][:7]), Transform(dis, code[0][7:]))
        where = code[1][-2].get_center() + code[1][-1].get_center()
        where /= 2
        script = octicon("log-24", fill_color=WHITE).scale(0.2).move_to(where)
        delta = 4.2 * LEFT + 2 * DOWN
        delta_fb = 2.5 * LEFT + 2 * DOWN
        self.play(FadeIn(script, shift=-delta))
        fb = octicon("file-binary-24", fill_color=WHITE).scale(0.2).move_to(where)
        texts = (
            VGroup(
                MonoText("source"),
                MonoText("bytecode"),
            )
            .arrange(buff=0.4)
            .move_to((delta + delta_fb) / 2 + DOWN)
        )
        self.wait(1)
        self.play(script.animate.move_to(delta).scale(1.5), FadeIn(fb, shift=-delta_fb))
        self.play(Write(texts[0]))
        self.play(fb.animate.move_to(delta_fb).scale(1.5))
        self.play(Write(texts[1]))

        self.play(
            Create(
                Circle(
                    radius=0.2, color=BLUE, fill_color=BLUE, fill_opacity=0.4
                ).move_to(where)
            )
        )
        dummy = MonoParagraph(
            """0 RESUME      0
2 LOAD_CONST  1 (0)
...
4 RETURN_VALUE
"""
        ).shift(2 * RIGHT)
        arrow = Arrow(
            code.get_edge_center(RIGHT), dummy.get_edge_center(LEFT), stroke_width=3
        )
        self.play(AnimationGroup(Create(arrow), FadeIn(dummy, shift=0.2 * RIGHT)))
        human = (
            octicon("people-24", fill_color=WHITE)
            .scale(0.8)
            .move_to(3.75 * RIGHT + 2 * DOWN)
        )
        self.play(FadeIn(human, shift=0.2 * UP))
        buffer = 0.2
        arr = CurvedArrow(
            dummy.get_edge_center(DOWN) + buffer * DOWN,
            fb.get_edge_center(RIGHT) + buffer * RIGHT,
            angle=-PI / 4,
        )
        self.play(Create(arr))
        x_scale = 0.5
        x = VGroup(
            Line(start=x_scale * UR, end=x_scale * DL, stroke_width=5, color=RED),
            Line(start=x_scale * UL, end=x_scale * DR, stroke_width=5, color=RED),
        ).shift(2 * DOWN + 0.05 * UP)
        for line in x:
            self.play(Create(line), run_time=0.5)

        self.wait(3)
