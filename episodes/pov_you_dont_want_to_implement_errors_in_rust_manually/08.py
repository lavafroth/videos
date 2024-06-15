#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


def node(text):
    file = Circle(color=WHITE, radius=0.5)
    lab = Text(text, font=codefont, font_size=22)
    return Group(file, lab)


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        com = octicon("gear-24", fill_color=WHITE).scale(0.3)
        com1 = (
            octicon("gear-16", fill_color=WHITE).scale(0.3 * 16 / 24).shift(0.35 * DR)
        )
        cogs = Group(com, com1)
        cogs.scale(1.5)
        start = cogs.get_edge_center(RIGHT) + UP * 0.1 + 10 * LEFT
        a = Arrow(start=start, end=start + 20 * RIGHT)
        self.add(a)
        self.play(a.animate.shift(16 * LEFT))
        n = node("file").shift(3 * UP)
        self.play(Create(n[0]), Write(n[1]))
        n1 = (
            Group(node("Item"), node("Item"), node("Item"))
            .arrange(buff=1.0)
            .shift(1.5 * UP)
        )
        n2 = Group(node("Fn"), node("Fn")).arrange(buff=1.0).shift(3 * LEFT)
        n3 = Group(node("Struct")).arrange(buff=1.0)
        n4 = Group(node("Fn"), node("Enum")).arrange(buff=1.0).shift(3 * RIGHT)
        self.play(AnimationGroup(Create(n[0]), Write(n[1])) for n in n1)
        self.play(
            AnimationGroup(Create(n[0]), Write(n[1]))
            for n in list(n2) + list(n3) + list(n4)
        )
        lines = []
        for nz in n1:
            direction = 0 * LEFT
            lines.append(
                Line(
                    start=n.get_edge_center(DOWN) - direction,
                    end=nz.get_edge_center(UP) + direction,
                )
            )
        for nz in n2:
            direction = 0 * LEFT
            lines.append(
                Line(
                    start=n1[0].get_edge_center(DOWN) - direction,
                    end=nz.get_edge_center(UP) + direction,
                )
            )
        for nz in n3:
            direction = 0 * LEFT
            lines.append(
                Line(
                    start=n1[1].get_edge_center(DOWN) - direction,
                    end=nz.get_edge_center(UP) + direction,
                )
            )
        for nz in n4:
            direction = 0 * LEFT
            lines.append(
                Line(
                    start=n1[2].get_edge_center(DOWN) - direction,
                    end=nz.get_edge_center(UP) + direction,
                )
            )
        self.play(Create(l) for l in lines)
        poly = RegularPolygon(n=8, color=BLUE).scale(0.6)
        lab = Text("active", font=codefont, font_size=20)
        attr = Group(poly, lab)
        dotted = lambda x, y: DashedLine(x, y, dashed_ratio=0.1)

        attr = attr.shift(3 * (DOWN + RIGHT) + RIGHT)
        dashed_1 = dotted(
            n2[0].get_edge_center(DOWN) + 0.5 * DOWN,
            n2[0].get_edge_center(DOWN) + 2 * DOWN,
        )
        dashed_2 = dotted(
            n4[1].get_edge_center(DOWN) + 0.5 * DOWN,
            attr.get_edge_center(UP) + 0.2 * UP,
        )
        dashed_3 = dotted(
            n2[0].get_edge_center(DOWN) + 0.5 * DOWN + 0.5 * RIGHT,
            attr.get_edge_center(UP) + 0.2 * UP + 0.5 * LEFT,
        )
        self.play(Create(attr[0]), Write(attr[1]))
        self.play(
            Create(dashed_1),
            Create(dashed_2),
            Create(dashed_3),
        )
        self.play(FadeOut(a))
        start = attr.get_center()
        end=attr.get_center() + 3 * UP + 1.5 * RIGHT
        arc = ArcBetweenPoints(start=start, end=end)
        self.play(MoveAlongPath(attr, arc))
        self.play(Transform(attr, node('...').move_to(attr)))
        arc = ArcBetweenPoints(start=end, end=start)
        self.play(MoveAlongPath(attr, arc))
        self.wait(1)
