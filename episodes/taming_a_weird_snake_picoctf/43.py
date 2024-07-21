#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """      0 BUILD_LIST               0
      2 LOAD_FAST                0 (.0)
>>    4 FOR_ITER                12 (to 18)
      6 STORE_FAST               1 (char)
      8 LOAD_GLOBAL              0 (ord)
     10 LOAD_FAST                1 (char)
     12 CALL_FUNCTION            1
     14 LIST_APPEND              2
     16 JUMP_ABSOLUTE            4
>>   18 RETURN_VALUE"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack_var = RoundedRectangle(width=4, height=1, color=BLUE, fill_color=BLUE, fill_opacity=0.5, corner_radius=0.05)
        n = 3
        stack = (stack_var.copy().fade(x/n) for x in range(n))
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
        iter_txt = SVGMobject('iter-rot', fill_color=WHITE).move_to(iter_box).scale(.3)
        itera = VGroup(iter_txt, iter_box)
        self.add(itera)

        off = (4 + SMALL_BUFF) * LEFT

        self.play(FadeIn(code, shift=2*UP))
        self.play(code[0].animate.set_opacity(1))
        list_box = RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05).set_z_index(-1).next_to(itera, UP)
        self.play(Create(list_box))


        self.play(FadeOut(code[0], shift=2 * UP), code[1:].animate.to_edge(UL))
        self.play(code[1].animate.set_opacity(1))

        dotzero = code[1][-3:-1]
        dotzero_copy = dotzero.copy()
        dotzero.set_opacity(0)
        phantom = list_box.copy().next_to(list_box, UP)
        self.play(dotzero_copy.animate.move_to(phantom))
        self.wait(1)
