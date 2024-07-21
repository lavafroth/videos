# (WHITE)!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """124 MAKE_FUNCTION            0
126 LOAD_NAME                1 (key_str)
128 GET_ITER
130 CALL_FUNCTION            1
132 STORE_NAME               2 (key_list)"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        stack.shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        code[0].set_opacity(1)
        self.add(code)
        self.play(FadeOut(code[0], shift=2 * UP), code[1:].animate.to_edge(UL))

        phantom = stackvar(WHITE).next_to(stack, UP)

        co_box = stackvar(ORANGE).set_z_index(-1).next_to(phantom, UP)
        co_txt = MonoText("'t_Jo3'").move_to(co_box).set_z_index(1)
        co = VGroup(co_txt, co_box)

        key_str = code[1][-8:-1]
        key_str_copy = key_str.copy()
        key_str.set_opacity(0)
        self.play(
            ReplacementTransform(key_str_copy.copy(), co_box),
            ReplacementTransform(key_str_copy.copy(), co_txt),
        )

        off = (4 + SMALL_BUFF) * LEFT
        itera = SVGMobject("iter-rot", fill_color=WHITE).move_to(co).scale(0.3)
        line = Line(co.get_edge_center(RIGHT) + off, itera)

        self.play(FadeOut(code[1], shift=2 * UP), code[2:].animate.to_edge(UL))
        self.play(co.animate.shift(off), code[2].animate.set_opacity(1))

        self.play(FadeIn(itera, shift=RIGHT), Create(line), lag_ratio=0.8)

        iter_box = (
            stackvar(YELLOW_B, 0)
            .set_z_index(-1)
            .next_to(phantom, UP)
        )
        line_ = Line(co.get_edge_center(RIGHT), iter_box.get_edge_center(LEFT))
        self.play(Create(iter_box), Transform(line, line_), itera.animate.shift(LEFT))

        iter_res_box = (
            RoundedRectangle(
                width=0.8,
                height=0.8,
                color=ORANGE,
                fill_color=ORANGE,
                fill_opacity=0.5,
                corner_radius=0.05,
            )
            .set_z_index(-1)
            .move_to(iter_box.get_edge_center(RIGHT) + (0.4 + 0.1) * LEFT)
        )
        iter_res_txt = MonoText("'t'").move_to(iter_res_box).set_z_index(1)
        iter_res = VGroup(iter_res_box, iter_res_txt)

        self.play(itera.animate.rotate(PI / 2), FadeIn(iter_res, shift=RIGHT))

        for txt in "_Jo3":
            iter_res_box = (
                RoundedRectangle(
                    width=0.8,
                    height=0.8,
                    color=ORANGE,
                    fill_color=ORANGE,
                    fill_opacity=0.5,
                    corner_radius=0.05,
                )
                .set_z_index(-1)
                .move_to(iter_box.get_edge_center(RIGHT) + (0.4 + 0.1) * LEFT)
            )
            iter_res_txt = (
                MonoText("'{}'".format(txt)).move_to(iter_res_box).set_z_index(1)
            )
            iter_res_next = VGroup(iter_res_box, iter_res_txt)
            self.play(
                itera.animate.rotate(PI / 2),
                FadeOut(iter_res, shift=RIGHT),
                FadeIn(iter_res_next, shift=RIGHT),
            )
            iter_res = iter_res_next
        self.play(itera.animate.rotate(PI / 2), FadeOut(iter_res, shift=RIGHT))
        self.play(FadeOut(line, co), itera.animate.move_to(iter_box.get_center()))
        self.wait(1)
