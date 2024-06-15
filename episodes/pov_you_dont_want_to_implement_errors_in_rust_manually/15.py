#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"

def boxattr(attr: str):
    d = Text(attr, font=codefont, font_size=32).set_z_index(1)
    box = RoundedRectangle(width=d.width + .5, height=d.height + .5, corner_radius=.2, color=BLUE, fill_color=BLUE, fill_opacity=.2).move_to(d).set_z_index(0)
    return Group(d, box)

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        w = Text('active').to_edge(DOWN)
        self.add(w)
        self.play(w.animate.to_edge(UP).shift(3 * RIGHT))
        d = Text('#[derive(thiserror::Error)]', font=codefont, font_size=32).next_to(w, direction=DOWN, buff=2).set_z_index(1)
        d_box = RoundedRectangle(width=d.width + 1, height=d.height + 1, corner_radius=.2, color=TEAL_D, fill_color=TEAL_D, fill_opacity=.2).move_to(d).set_z_index(0)
        self.play((Create(d_box), Write(d)))
        l = Text('inert').to_edge(UP).shift(3 * LEFT)
        boxes = [boxattr(attr).next_to(l, direction=DOWN, buff=1).shift(i * DOWN + .5 * UP).fade(1) for i, attr in enumerate(('#[source]', '#[from]', '#[error]', '#[backtrace]'))]
        boxes_ = [boxattr(attr).next_to(l, direction=DOWN, buff=1).shift(i * DOWN) for i, attr in enumerate(('#[source]', '#[from]', '#[error]', '#[backtrace]'))]
        self.play(FadeIn(l))
        self.play(
            AnimationGroup(
                (Transform(a,b) for a,b in zip(boxes, boxes_)),
                lag_ratio=.5
            ),
        )
        self.wait(1)
