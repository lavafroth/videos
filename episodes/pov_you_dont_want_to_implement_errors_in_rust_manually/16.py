#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


def boxattr(attr: str):
    d = Text(attr, font=codefont, font_size=32).set_z_index(1)
    box = (
        RoundedRectangle(
            width=d.width + 0.5,
            height=d.height + 0.5,
            corner_radius=0.2,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.2,
        )
        .move_to(d)
        .set_z_index(0)
    )
    return Group(d, box)


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        active = Text("active").to_edge(UP).shift(3 * RIGHT)
        self.add(active)
        d = (
            Text("#[derive(thiserror::Error)]", font=codefont, font_size=32)
            .next_to(active, direction=DOWN, buff=2)
            .set_z_index(1)
        )
        d_box = (
            RoundedRectangle(
                width=d.width + 1,
                height=d.height + 1,
                corner_radius=0.2,
                color=TEAL_D,
                fill_color=TEAL_D,
                fill_opacity=0.2,
            )
            .move_to(d)
            .set_z_index(0)
        )
        self.add(d_box, d)
        inert = Text("inert").to_edge(UP).shift(3 * LEFT)
        boxes = [
            boxattr(attr).next_to(inert, direction=DOWN, buff=1).shift(i * DOWN)
            for i, attr in enumerate(
                ("#[source]", "#[from]", "#[error]", "#[backtrace]")
            )
        ]
        self.add(inert, *boxes)
        dots = [
            Dot(radius=0.1)
            .move_to(d_box.get_edge_center(LEFT) + 0.35 * UP + x * 0.25 * DOWN)
            .set_z_index(1)
            for x in range(4)
        ]
        dots_ = [
            Dot(radius=0.1).move_to(d_box.get_edge_center(RIGHT)).set_z_index(1)
            for d_box in boxes
        ]
        self.play(Create(dot) for dot in dots)
        self.play(Create(dot) for dot in dots_)
        lines = []
        for a, b in zip(dots, dots_):
            lines.append(Line(a, b))
        self.play(AnimationGroup((Create(line) for line in lines), lag_ratio=0.4))
        anims = []
        for box, dot, line in zip(boxes, dots_, lines):
            dir = line.start - line.end
            dot_ = dot.copy().shift(dir / 4).set_opacity(0)
            line_ = Line(line.start, line.end + dir / 4).set_opacity(0)
            anims.append(Transform(dot, dot_))
            anims.append(Transform(line, line_))
        ends = [d.get_center() + DOWN * (i + 1) for i in range(4)]
        arcs = [
            ArcBetweenPoints(box.get_center(), e, angle=-PI / 4)
            for box, e in zip(boxes, ends)
        ]
        derive_macro_helper = Text("derive macro helper attributes").to_edge(UP)
        self.play(
            AnimationGroup(
                AnimationGroup(anims, lag_ratio=.1, run_time=.5),
                AnimationGroup(
                    (MoveAlongPath(box, arc) for box, arc in zip(boxes, arcs)),
                    lag_ratio=0.1,
                ),
                AnimationGroup(
                    Transform(
                        d_box,
                        RoundedRectangle(
                            width=d.width + 1,
                            height=d.height + 5,
                            corner_radius=0.2,
                            color=TEAL_D,
                            fill_color=TEAL_D,
                            fill_opacity=0.2,
                        )
                        .move_to(d.get_center() + 2 * DOWN)
                        .set_z_index(0),
                    ),
                    *(FadeOut(dot) for dot in dots),
                    ReplacementTransform(Group(active, inert), derive_macro_helper),
                ),
            )
        )
        grp = Group(d_box, d, *boxes)
        self.play(grp.animate.move_to(ORIGIN + DOWN * .5))
        self.wait(2)
        a, b, c = d[:len('#[derive(')], d[len('#[derive('):-2], d[-2:]
        self.play(FadeOut(d_box, *boxes, derive_macro_helper, a, c), b.animate.move_to(ORIGIN).scale(2))
