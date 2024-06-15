#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        code = Code('error_trait.rs', font_size=32, insert_line_no=False)[2].set_z_index(1)
        self.play(FadeIn(code))
        self.wait(2)

        self.play(
            FadeOut(code[:-2]),
            FadeOut(code[-1:]),
        )
        target = code[-2]
        self.play(target.animate.move_to(ORIGIN))
        rust_ = SVGMobject('rust.svg', fill_color=WHITE)
        nightly = Text('nightly').next_to(rust_)
        rust_nightly = Group(rust_, nightly).move_to(ORIGIN).shift(2 * DOWN)
        rust = SVGMobject('rust.svg', fill_color=WHITE).set_opacity(0).move_to(rust_).shift(DOWN * .5)
        self.play(Transform(rust, rust_), Write(nightly))
        self.wait(6)
        self.play(FadeOut(rust, nightly))

        table = Rectangle(
            width=2,
            height=3 / 2,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.3,
            grid_ystep=3 / 8,
        ).shift(2 * DR)
        trait_object = Rectangle(
            width=1,
            height=3 / 4,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.3,
            grid_ystep=3 / 8,
        )
        a1 = Arrow(0.2 * UP, 0.2 * UP + 2 * RIGHT)
        a2 = Arrow(0.2 * DOWN, 1.4 * DOWN + 2 * RIGHT)
        a3 = Arrow(2.6 * DOWN + 1.5 * RIGHT, 2.6 * DOWN + 0.1 * LEFT)
        data = Rectangle(
            width=1.5, height=0.5, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3
        ).shift(2 * RIGHT + .2 * UP)
        mc = Text("machine\ncode", font=codefont, font_size=22).shift(2.6 * DOWN + 0.5 * LEFT)
        rdp = Text("raw data\npointer", font=codefont, font_size=22).next_to(data, UP)
        fp = Text("fat pointer", font=codefont, font_size=22).next_to(trait_object, UP)
        ddt = Text("dynamic\ndispatch\ntable", font=codefont, font_size=22).next_to(table, DOWN)
        grp = VGroup(
            trait_object,
            table,
            a1,
            a2,
            a3,
            data,
            mc,
            rdp,
            fp,
            ddt
        )

        grp.shift(UP + LEFT)
        self.play(
            Transform(target, grp),
        )
        member = Circle(radius=.5, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).next_to(data)
        lz = [
            Line(data.get_corner(UR), member.get_edge_center(UP) +   .08 * LEFT, color=TEAL_D),
            Line(data.get_corner(DR), member.get_edge_center(DOWN) + .08 * LEFT, color=TEAL_D),
        ]
        member = Circle(radius=.1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(data.get_edge_center(RIGHT)).set_opacity(0)
        member_ = Circle(radius=.5, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).next_to(data)
        memte = Text("member\nfield", font=codefont, font_size=22).next_to(member_, DOWN)
        self.play(map(Create, lz), Transform(member, member_), Write(memte))
        self.wait(1)
        self.play(x.animate.shift(12 * LEFT) for x in (*lz, target, member, memte))
        self.wait(1)

