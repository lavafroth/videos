#!/usr/bin/env manim
from manim import *
from manim import VGroup as V
from hackermanim import *


def stackvar(color, opacity=0.5):
    return RoundedRectangle(
        width=4,
        height=1,
        color=color,
        fill_color=color,
        fill_opacity=opacity,
        corner_radius=0.05,
    )


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        stack_var = stackvar(BLUE)
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = V(*stack).arrange(DOWN).shift(5.5 * DOWN + 4 * RIGHT)

        opacity = 0.5
        abox = RoundedRectangle(
            width=1,
            height=1,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=opacity,
            corner_radius=0.05,
        ).set_z_index(-1)
        bbox = abox.copy()
        xor = Tex(r"$\oplus$").scale(1.5)
        axorb = V(abox, xor, bbox).arrange()
        t = Text("Exclusive OR").next_to(xor, UP).to_edge(UP)
        atxt = Text("a", font=codefont, font_size=32).move_to(abox)
        btxt = Text("b", font=codefont, font_size=32).move_to(bbox)
        axorb = V(V(atxt, abox), xor, V(btxt, bbox)).arrange().shift(2 * UP)
        self.add(t, axorb)

        buff = 0
        sq_a = (
            Square(
                1,
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=opacity,
            )
            .set_z_index(-1)
            .move_to(abox)
        )
        abits = V(*(sq_a.copy().shift(DOWN * x * (1 + buff)) for x in range(1, 5)))
        sq_b = (
            Square(
                1,
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=opacity,
            )
            .set_z_index(-1)
            .move_to(bbox)
        )
        bbits = V(*(sq_b.copy().shift(DOWN * x * (1 + buff)) for x in range(1, 5)))
        buff = SMALL_BUFF
        bbits_ = V(*(bbox.copy().shift(DOWN * x * (1 + buff)) for x in range(1, 5)))
        abits_ = V(*(abox.copy().shift(DOWN * x * (1 + buff)) for x in range(1, 5)))
        self.play(
            Create(abits),
            Create(bbits),
        )

        a__bits = ["0", "1", "0", "..."]
        b__bits = ["1", "0", "0", "..."]
        r__bits = ["1", "1", "0", "..."]

        abits_txt = V(
            *(
                Text(x, font=codefont, font_size=32).move_to(pos)
                for x, pos in zip(a__bits, abits_)
            )
        )
        bbits_txt = V(
            *(
                Text(x, font=codefont, font_size=32).move_to(pos)
                for x, pos in zip(b__bits, bbits_)
            )
        )
        eqs = V(*(Tex(r"$=$").next_to(pos) for x, pos in zip(r__bits, bbits_)))
        self.play(
            Transform(abits, abits_),
            Transform(bbits, bbits_),
        )
        self.play(Write(abits_txt), Write(bbits_txt))
        disp = (1 + buff) * DOWN
        outs = []
        for x in range(4):
            self.play(xor.animate.shift(disp))
            self.play(Write(eqs[x]))
            res = bbox.copy().next_to(eqs[x])
            bit = Text(r__bits[x], font=codefont, font_size=32).move_to(res)
            self.play(Create(res), Write(bit))
            outs.append(V(res, bit))

        outs = V(*outs)
        out = bbox.copy().move_to(outs.get_center() * RIGHT + bbox.get_center() * UP)
        # bit =Text(r__bits[x], font=codefont, font_size=32).move_to(res)
        self.play(
            (
                eq.animate.move_to(eqs.get_center() * RIGHT + bbox.get_center() * UP)
                for eq in eqs
            ),
            ReplacementTransform(outs, out),
            xor.animate.shift(4 * -disp),
            FadeOut(abits),
            FadeOut(abits_txt),
            FadeOut(bbits),
            FadeOut(bbits_txt),
        )

        stack_var = stackvar(BLUE)
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = V(*stack).arrange(DOWN).shift(5.5 * DOWN + 4 * RIGHT)
        p = stackvar(WHITE).next_to(stack, UP)
        p = p.next_to(p, UP)
        p = p.next_to(p, UP)
        me = stackvar(BLUE).next_to(p, UP)
        eqs[:-1].set_opacity(0)
        self.play(FadeOut(axorb, t, eqs[-1]),Transform(out, me))
        self.wait(1)
