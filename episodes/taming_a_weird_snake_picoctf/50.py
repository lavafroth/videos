#!/usr/bin/env manim
from manim import *
from hackermanim import *
from manim import Transform as T, ReplacementTransform as RT, VGroup as V
from stack import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """      2 LOAD_FAST                0 (  )
>>    4 FOR_ITER                12 (to 18)
      6 STORE_FAST               1 (char)
      8 LOAD_GLOBAL              0 (ord)
     10 LOAD_FAST                1 (char)
     12 CALL_FUNCTION            1
     14 LIST_APPEND              2
     16 JUMP_ABSOLUTE            4
>>   18 RETURN_VALUE"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[0].set_opacity(1)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        iter_box = stackvar(YELLOW_B).set_z_index(-1).next_to(stack, UP)
        iter_txt = SVGMobject("iter-rot", fill_color=WHITE).move_to(iter_box).scale(0.3)
        itera = V(iter_txt, iter_box)

        list_box = stackvar(WHITE, 0).set_z_index(-1).next_to(itera, UP)
        self.add(itera, list_box, code)

        arg = itera.copy()
        conduit = stackvar(YELLOW_B).move_to(itera)
        self.play(Create(conduit))
        self.play(FadeOut(conduit), FadeIn(arg))
        self.play(arg.animate.next_to(list_box, UP))

        stack_ele = V(stack, itera, list_box, arg)
        self.play(
            stack_ele.animate.shift(3 * DOWN),
            FadeOut(code[0], shift=2 * UP),
            code[1:].animate.to_edge(UL),
        )
        self.play(code[1].animate.set_opacity(1), code[-1][:2].animate.set_opacity(1))

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
            .move_to(arg[1].get_edge_center(RIGHT) + (0.4 + 0.1) * LEFT)
        )
        iter_res_txt = MonoText("'t'").move_to(iter_res_box).set_z_index(1)
        iter_res = V(iter_res_box, iter_res_txt)

        self.play(arg[0].animate.rotate(PI / 2), FadeIn(iter_res, shift=RIGHT))

        ephem = stackvar(ORANGE).set_z_index(-1).next_to(arg, UP)

        self.play(T(iter_res_box, ephem), iter_res_txt.animate.move_to(ephem))
        self.wait(1)
        iter_res_box.set_opacity(0)
        iter_res_txt.set_opacity(0)
        self.wait(1)
