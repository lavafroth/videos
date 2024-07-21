#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        raw = """>>    4 FOR_ITER                12 (to 18)
      6 STORE_FAST               1 (char)
      8 LOAD_GLOBAL              0 (ord)
     10 LOAD_FAST                1 (char)
     12 CALL_FUNCTION            1
     14 LIST_APPEND              2
     16 JUMP_ABSOLUTE            4
>>   18 RETURN_VALUE"""
        code = (
            Paragraph(raw, font=codefont, font_size=32)
            .to_edge(UL)
            .set_opacity(0.5)
            .set_z_index(-1)
        )
        code[0].set_opacity(1)
        code[-1][:2].set_opacity(1)

        stack_var = RoundedRectangle(
            width=4,
            height=1,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.5,
            corner_radius=0.05,
        )
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        iter_box = (
            RoundedRectangle(
                width=4,
                height=1,
                color=YELLOW_B,
                fill_color=YELLOW_B,
                corner_radius=0.05,
            )
            .set_z_index(-1)
            .next_to(stack, UP)
        )
        iter_txt = SVGMobject("iter-rot", fill_color=WHITE).move_to(iter_box).scale(0.3)
        itera = VGroup(iter_txt, iter_box)
        list_box = (
            RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05)
            .set_z_index(-1)
            .next_to(itera, UP)
        )
        arg = itera.copy()
        itera.next_to(list_box, UP)
        self.add(itera, list_box, code, arg)

        stack_ele = VGroup(stack, itera, list_box, arg).shift(3 * DOWN)
        self.play(
            stack_ele.animate,
        )

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
            .move_to(itera.get_edge_center(RIGHT) + (0.4 + 0.1) * LEFT)
        )
        iter_res = VGroup(iter_res_box)

        self.play(iter_txt.animate.rotate(PI / 2), FadeIn(iter_res, shift=RIGHT))

        ephem = (
            RoundedRectangle(
                width=4,
                height=1,
                color=ORANGE,
                fill_color=ORANGE,
                fill_opacity=0.5,
                corner_radius=0.05,
            )
            .set_z_index(-1)
            .next_to(itera, UP)
        )

        self.play(Transform(iter_res_box, ephem))
        self.play(code[1].animate.set_opacity(1), code[0][2:].animate.set_opacity(0.5))

        char_copy = code[1][-5:-1].copy().set(color=ORANGE).set_z_index(2)
        self.play(ReplacementTransform(iter_res_box, char_copy))
        self.wait(1)
        self.play(
            code[1].animate.set_opacity(0.5),
            char_copy.animate.set_opacity(0.5),
            code[2].animate.set_opacity(1),
        )

        # cant use ord because it is a function
        # hence, edgel - ord
        edgelord = code[2][-4:-1]
        edgelord.set_opacity(0)
        self.play(iter_txt.animate.rotate(PI/2))
        self.wait(1)
