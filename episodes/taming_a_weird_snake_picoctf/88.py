#!/usr/bin/env manim
from manim import *
from manim import VGroup as V
from hackermanim import *
from stack import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        stack.shift(4.5 * DOWN + 4 * RIGHT)

        raw = """      0 BUILD_LIST               0
      2 LOAD_FAST                0 (.0)
>>    4 FOR_ITER                16 (to 22)
      6 UNPACK_SEQUENCE          2
      8 STORE_FAST               1 (a)
     10 STORE_FAST               2 (b)
     12 LOAD_FAST                1 (a)
     14 LOAD_FAST                2 (b)
     16 BINARY_XOR
     18 LIST_APPEND              2
     20 JUMP_ABSOLUTE            4
>>   22 RETURN_VALUE"""
        iter_box = stackvar(YELLOW_B, opacity=0)
        iter_txt = (
            SVGMobject("iter-rot", fill_color=WHITE)
            .move_to(iter_box)
            .scale(0.3)
            .shift(1.5 * LEFT)
        )
        kc = Circle(radius=0.2, color=WHITE, fill_color=WHITE, fill_opacity=0.2)
        ic = Circle(radius=0.2, color=WHITE, fill_color=WHITE, fill_opacity=0.2)
        V(kc, ic).arrange().shift(RIGHT)
        itera = V(iter_txt, iter_box, kc, ic).next_to(stack, UP)
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        self.add(stack, code, itera)
        self.play(code[0].animate.set_opacity(1))
        lis = stackvar(WHITE, 0).next_to(itera, UP)
        self.play(Create(lis))
        self.play(code[1].animate.set_opacity(1), code[0].animate.set_opacity(0.5))
        phantom = stackvar(WHITE, 0).next_to(lis, UP)
        arr =CurvedArrow(itera.get_edge_center(LEFT), phantom.get_edge_center(LEFT), angle=-PI/2)
        self.play(FadeIn(itera.copy()))
        self.play(Create(arr), itera.animate.next_to(lis, UP))
        self.play(FadeOut(arr))
        self.play(code[2].animate.set_opacity(1), code[1].animate.set_opacity(0.5))
        self.wait(1)
