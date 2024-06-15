#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


def boxattr(attr: str):
    d = Text(attr, font=codefont, font_size=32).set_z_index(1)
    box = bwopa(0.2, d)
    return Group(d, box)


def bwopa(opa, d):
    return (
        RoundedRectangle(
            width=d.width + 0.5,
            height=d.height + 0.5,
            corner_radius=0.2,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=opa,
        )
        .move_to(d)
        .set_z_index(0)
    )


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        public = Circle(
            color=WHITE, fill_color=WHITE, fill_opacity=0.5, radius=1.25
        ).shift(3 * LEFT)
        r = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.5).shift(
            3 * LEFT
        )
        ut = Text("public", font=codefont, font_size=32).move_to(
            public.get_center() + 1.5 * UP
        )
        rt = Text("private", font=codefont, font_size=32).move_to(r)
        self.play(Create(public), FadeIn(ut))
        self.play(Create(r), FadeIn(rt))
        _u = Circle(color=WHITE, fill_color=WHITE, fill_opacity=1).shift(
            3 * LEFT
        )
        d = DashedLine(_u.get_edge_center(RIGHT), r.get_edge_center(LEFT) + 6 * RIGHT)
        wraps = Text("wraps", font=codefont, font_size=32).next_to(d, direction=DOWN)
        self.play(
            Transform(public, _u),
            Transform(
                ut,
                Text("public", font=codefont, font_size=32, color=BLACK).move_to(
                    public
                ),
            ),
            Group(r, rt).animate.shift(6 * RIGHT),
            Create(d),
            Write(wraps),
        )

        ev = Group(r, rt, d)
        nev = Group(public, ut)
        ev_s = 2 * RIGHT
        shif = 0.75 * RIGHT
        self.play(
            ev.animate.shift(ev_s),
            nev.animate.shift(ev_s + 2 * shif),
            wraps.animate.shift(ev_s + shif),
        )

        pub_fn = [
            boxattr(attr).shift(2.5 * LEFT + 1 * UP + i * DOWN)
            for i, attr in enumerate(("line_no", "stack_position", "last_mode"))
        ]
        conns = [
            Line(
                public.get_edge_center(LEFT)
                + DOWN / 2 * (i - 1)
                + RIGHT / 2 * abs(i - 1),
                box.get_edge_center(RIGHT),
            )
            for i, box in enumerate(pub_fn)
        ]
        self.play(
            AnimationGroup((FadeIn(*fn) for fn in zip(pub_fn, conns)), lag_ratio=0.4)
        )
        brace = Brace(Group(*pub_fn), direction=LEFT)
        brace_text = Text("methods\nexposed\nexplicitly", font_size=30).next_to(
            brace, direction=LEFT
        )
        self.play(Write(brace), Write(brace_text))
        self.play(
            Transform(
                r,
                RegularPolygon(
                    n=6, color=GREEN, fill_color=GREEN, fill_opacity=0.5
                ).move_to(r),
            )
        )
        self.play(
            Transform(
                r, Square(color=BLUE, fill_color=BLUE, fill_opacity=0.5).move_to(r)
            )
        )
        for thing in pub_fn:
            b = bwopa(0.5, thing[0])
            b_ = bwopa(0.2, thing[0])
            self.play(Transform(thing[1], b), run_time=0.5)
            self.play(Transform(thing[1], b_), run_time=0.5)
        divider = Line(10 * LEFT, 10 * RIGHT).shift(8 * DOWN)
        self.play(divider.animate.shift(6 * UP), Group(brace, brace_text, *conns, *pub_fn, ev, nev, wraps).animate.shift(UP))
        buff=.5
        disre = Text("Display represenation for version", font_size=30).next_to(
            divider, direction=DOWN, buff=buff
        ).to_edge(LEFT)
        v = Text('1.0.0', font=codefont, font_size=30).next_to(disre).set_z_index(1)
        vb= SurroundingRectangle(v, color=GREEN, fill_opacity=0.2, fill_color=GREEN, corner_radius=0.05)
        disre_act = Text("error:", color=RED, font=codefont, font_size=30).next_to(disre, direction=DOWN).to_edge(LEFT)
        disre_pr = Text("I'm a teapot", font=codefont, font_size=30).next_to(disre_act)
        disre_pr_ = Text("""HTTPError{code: 418, status: "I'm a teapot"}""", font=codefont, font_size=30).next_to(disre_act)
        self.play(FadeIn(disre, disre_act, disre_pr, v, vb))
        self.wait(2)
        v_ = Text('1.0.1', font=codefont, font_size=30).next_to(disre)
        vb_ = SurroundingRectangle(v, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05)
        self.play(Transform(disre_pr, disre_pr_), Transform(v, v_), Transform(vb, vb_))
        self.wait(6)
