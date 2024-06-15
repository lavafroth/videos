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
        n = node("file").shift(3 * UP)
        n1 = (
            Group(node("Item"), node("Item"), node("Item"))
            .arrange(buff=1.0)
            .shift(1.5 * UP)
        )
        n2 = Group(node("Fn"), node("Fn")).arrange(buff=1.0).shift(3 * LEFT)
        n3 = Group(node("Struct")).arrange(buff=1.0)
        n4 = Group(node("Fn"), node("Enum")).arrange(buff=1.0).shift(3 * RIGHT)
        lines = []
        for nz in n1:
            lines.append(
                Line(
                    start=n.get_edge_center(DOWN),
                    end=nz.get_edge_center(UP),
                )
            )
        for i, nodecoll in enumerate((n2, n3, n4)):
            for nz in nodecoll:
                lines.append(
                    Line(
                        start=n1[i].get_edge_center(DOWN),
                        end=nz.get_edge_center(UP),
                    )
                )
        dotted = lambda x, y: DashedLine(x, y, dashed_ratio=0.1)

        attr = node("...").shift(3 * (DOWN + RIGHT) + RIGHT)
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

        ev = Group(attr, dashed_1, dashed_2, dashed_3, n, n1, n2, n3, n4, *lines)
        self.add(ev)
        f = Text('#[error]', font=codefont, font_size=40, color=GREEN_D)
        bounds = lambda f: (f[:2], f[2:-1], f[-1])
        a, b, c = bounds(f)
        a.scale(3)
        a.shift(4 * LEFT)
        at = Text('attributes', font=codefont, font_size=40, color=GREEN_D).scale(3).shift(.5  * RIGHT)
        c.scale(3).next_to(at)
        grp = Group(a, at, c)
        grp.to_edge(UP).scale(0.5)
        ac = Text('active\nattributes').shift(3* LEFT)
        aa = Arrow(start=grp.get_center() + DL/2, end=ac)
        ia = Text('inert\nattributes').shift(3*RIGHT)
        ai = Arrow(start=grp.get_center() + DR/2, end=ia)
        gg = Group(grp, ac, ia, aa, ai).shift(10 * UP)
        self.play(ev.animate.shift(10 * DOWN), gg.animate.shift(10 * DOWN))
        self.play(x.animate.set_opacity(0.5) for x in (*grp, ac, aa, ai))
        surr = Rectangle(color=GREEN, width=ia.get_width() + .5, height=ia.get_height() + .5).move_to(ia.get_center())
        self.play(Create(surr))
        self.play(FadeOut(surr))
        self.play(ev.animate.shift(10 * UP), gg.animate.shift(10 * UP))
        self.play(FadeOut(attr))
        poly = RegularPolygon(n=8, color=GREEN).scale(0.6)
        lab = Text("inert", font=codefont, font_size=20)
        attr = Group(poly, lab).move_to(attr)
        self.play(Create(attr[0]), Write(attr[1]))
        self.wait(1)
        curve = ParametricFunction(lambda t: np.array([0.1 * np.sin(PI * t), 0, 0]), t_range=[0, 4]).move_to(attr.get_center())
        self.play(MoveAlongPath(attr, curve))

        self.wait(3)
        ev = Group(attr, dashed_1, dashed_2, dashed_3, n, n1, n2, n3, n4, *lines)
        self.play(FadeOut(ev))
