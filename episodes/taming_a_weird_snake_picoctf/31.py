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

        raw = """120 LOAD_CONST              35 (<code object <listcomp>
                                        at 0x7f04f6bded40,
                                        file "snake.py", line 9>)
122 LOAD_CONST              36 ('<listcomp>')
124 MAKE_FUNCTION            0
126 LOAD_NAME                1 (key_str)
128 GET_ITER
130 CALL_FUNCTION            1
132 STORE_NAME               2 (key_list)"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)

        stack_var = RoundedRectangle(width=4, height=1, color=BLUE, fill_color=BLUE, fill_opacity=0.5, corner_radius=0.05)
        n = 3
        stack = (stack_var.copy().fade(x/n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        self.add(stack)

        co_dis = VGroup(code[0][-21:],code[1],code[2][:-1])

        off = (4 + SMALL_BUFF) * LEFT
        co_box = RoundedRectangle(width=4, height=1, color=PURPLE, fill_color=PURPLE, fill_opacity=0.5, corner_radius=0.05).set_z_index(-1).next_to(stack, UP).shift(off)
        co_txt = MonoText("0x7f04f6bded40").move_to(co_box).set_z_index(1)

        co = VGroup(co_txt, co_box)
        self.play(FadeIn(code, shift=2*UP))
        self.play(code[0:3].animate.set_opacity(1))
        self.play(Transform(co_dis, co))
        self.remove(co_dis)


        self.play(co.animate.shift(-off))
        self.play(code[3].animate.set_opacity(1), code[0][:-21].animate.set_opacity(.5), code[2][-1].animate.set_opacity(.5))

        lc_dis = code[3][-13:-1]

        lc_box = RoundedRectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, corner_radius=0.05)
        lc_txt = MonoText("'listcomp'").move_to(lc_box.get_center()).set_z_index(2)
        lc = VGroup(lc_txt, lc_box).next_to(co_box, UP)

        self.play(ReplacementTransform(lc_dis, lc_box), ReplacementTransform(lc_dis.copy(), lc_txt))
        discard = VGroup(code[0][:-21], code[2][-1], code[3][:-13], code[3][-1])
        self.play(FadeOut(discard, shift=2.2 * UP), code[4:].animate.to_edge(UL))
        self.play(code[4].animate.set_opacity(1))
        vg = VGroup(co, lc)
        self.play(vg.animate.move_to(ORIGIN).arrange())

        vg = VGroup(co_box, lc_box)
        vg_txt = VGroup(co_txt, lc_txt)
        end_box = RoundedRectangle(width=4, height=1, color=WHITE, corner_radius=0.05)
        end_txt = MonoText("<listcomp>").move_to(end_box).set_z_index(2)
        self.play(ReplacementTransform(vg, end_box), ReplacementTransform(vg_txt, end_txt))
        self.play(FadeOut(end_box, end_txt))
        self.wait(1)
