#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        raw = """>>    4 FOR_ITER                12 (to 18)
      6 STORE_FAST               1 (    )
      8 LOAD_GLOBAL              0 (   )
     10 LOAD_FAST                1 (    )
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
        code[0][:2].set_opacity(1)
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
            RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05, fill_color=WHITE, fill_opacity=0.25)
            .set_z_index(-1)
            .next_to(itera, UP)
        )
        arg = itera.copy()
        itera.next_to(list_box, UP)
        self.add(stack, itera, list_box, code, arg)

        stack_ele = VGroup(stack, itera, list_box, arg).shift(3 * DOWN)

        code[4].set_opacity(1)
        self.play(
            code[4].animate.set_opacity(.5),
            code[5].animate.set_opacity(1),
        )
        two = code[5][-1]
        c = Circle(radius=.2, color=BLUE).move_to(two)

        phantom_display = (
            RoundedRectangle(
                width=4,
                height=1,
                color=TEAL,
                corner_radius=0.05,
            )
            .set_z_index(-1)
            .next_to(itera, UP)
        )

        phantom_text = Text('unicode code point', font=codefont, font_size=32).move_to(phantom_display)
        grp = VGroup(phantom_display, phantom_text).fade(0.75)

        self.play(Create(c), FadeIn(grp))
        numeral_b = [arg, list_box, itera, grp][::-1]
        numerals = VGroup(*[Text(str(x), font=codefont, font_size=32).next_to(boxybox, LEFT) for x, boxybox in enumerate(numeral_b)])
        c_b = Circle(radius=.2, color=BLUE).move_to(numerals[2])
        self.play(Write(numerals), FadeOut(c))
        self.play(Create(c_b))
        self.play(FadeOut(c_b))
        self.play(Unwrite(numerals), code[5].animate.set_opacity(.5), code[6].animate.set_opacity(1))
        four = code[0][2]
        a = CurvedArrow(code[6][-1].get_edge_center(LEFT) + .1 * LEFT, four.get_edge_center(DOWN) + .1 * DOWN, angle=-PI/4)
        self.play(Create(a), four.animate.set_opacity(1))
        turbo_1 = code[0][:2]
        curve_1 = ParametricFunction(lambda t: np.array([0.2 * (1 + np.sin(2 * PI * t)), 0, 0]), t_range=[0, 2]).move_to(turbo_1)
        self.play(FadeOut(a), MoveAlongPath(turbo_1, curve_1))

        for x in range(2):
            list_box_clone = (
                RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05, fill_color=WHITE, fill_opacity=0.5 + 0.25 * x)
                .move_to(list_box)
            )
            grp_box = grp.copy()
            self.play(FadeIn(grp_box))
            self.play(
                grp_box.animate.fade(1).move_to(list_box),
                Transform(list_box, list_box_clone),
            )


        list_box_clone = (
            RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05, fill_color=WHITE, fill_opacity=1)
            .move_to(list_box)
        )
        self.play(
            grp.animate.fade(1).move_to(list_box),
            Transform(list_box, list_box_clone),
        )
        self.play(four.animate.set_opacity(.5),code[6].animate.set_opacity(.5), code[7].animate.set_opacity(1))
        self.wait(2)
        self.play(FadeOut(stack, itera, code, arg), list_box.animate.move_to(ORIGIN))
        self.wait(1)
