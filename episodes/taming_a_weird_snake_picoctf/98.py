#!/usr/bin/env manim

from manim import *
from manim import VGroup as V, Transform as T, ReplacementTransform as RT
from hackermanim import *
from stack import *


def stackvar_(color, opacity=0.5):
    return stackvar(color, opacity).set_z_index(-1)


def chunks3(obj, x, y):
    return (obj[:x], obj[x:y], obj[y:])


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=40)

        raw = """
182 LOAD_CONST              38 ('')
184 LOAD_METHOD              7 (join)
186 LOAD_NAME                8 (map)
188 LOAD_NAME                9 (chr)
190 LOAD_NAME                6 (result)
192 CALL_FUNCTION            2
194 CALL_METHOD              1
196 STORE_NAME              10 (result_text)
198 LOAD_CONST              39 (None)
200 RETURN_VALUE
        """.strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5).shift(0.3 * LEFT)
        stack_var = stackvar_(BLUE)
        n = 3
        stack.shift(4.5 * DOWN + 4 * RIGHT)
        self.add(code, stack)
        self.play(code[0].animate.set_opacity(1))
        remnants = []
        l, empty, r = chunks3(code[0], -3, -1)
        remnants.append(l)
        remnants.append(r)
        empty_box = stackvar_(ORANGE).next_to(stack, UP)
        self.play(
            ReplacementTransform(empty.copy(), empty_box),
            empty.animate.move_to(empty_box),
        )
        self.play(V(l, r).animate.set_opacity(0.5), code[1].animate.set_opacity(1))
        l, join, r = chunks3(code[1], -5, -1)
        remnants.append(l)
        remnants.append(r)
        join_box = stackvar_(PURPLE).next_to(empty_box, UP)
        self.play(Transform(join.copy(), join_box), join.animate.move_to(join_box))
        self.play(V(l, r).animate.set_opacity(0.5), code[2].animate.set_opacity(1))
        l, mappa, r = chunks3(code[2], -4, -1)
        remnants.append(l)
        remnants.append(r)
        mappa_box = stackvar_(PURPLE_B).next_to(join_box, UP)
        self.play(
            ReplacementTransform(mappa.copy(), mappa_box),
            mappa.animate.move_to(mappa_box),
        )
        self.play(V(l, r).animate.set_opacity(0.5), code[3].animate.set_opacity(1))
        l, chra, r = chunks3(code[3], -4, -1)
        remnants.append(l)
        remnants.append(r)
        chra.set_opacity(0)
        self.wait(1)
        self.play(V(l, r).animate.set_opacity(0.5), code[4].animate.set_opacity(1))
        l, res, r = chunks3(code[4], -7, -1)
        remnants.append(l)
        remnants.append(r)
        res_box = stackvar_(WHITE).next_to(mappa_box, UP)
        res_box = res_box.next_to(res_box, UP)
        self.play(
            ReplacementTransform(res.copy(), res_box), res.animate.move_to(res_box)
        )
        self.play(V(l, r).animate.set_opacity(0.5), code[5].animate.set_opacity(1))
        self.wait(5)
        two = code[5][-1]
        s = SurroundingRectangle(two, BLUE, corner_radius=0.05)
        self.play(Create(s))
        self.wait(1)
        mappa_box_ = stackvar_(PURPLE_B, 0.8).next_to(join_box, UP)
        mb = mappa_box.copy()
        self.play(T(mappa_box, mappa_box_), run_time=0.5)
        self.play(T(mappa_box, mb), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(s))
        self.wait(1)
        V(mappa, mappa_box).set_opacity(0)
        self.wait(1)
        t = MonoText(
            "map(chr, result)", t2c={"map(": PURPLE, ")": PURPLE, ",": PURPLE}
        ).move_to(3.5 * LEFT + 2 * DOWN)
        res = V(res, res_box)
        self.play(RT(res, t[-7:-1]))
        self.wait(1)
        c = Circle(radius=0.2, color=TEAL, fill_color=TEAL, fill_opacity=0.5)
        chra = t[4:7]
        chra_0 = chra.copy()
        chra_1 = chra.copy()
        chr_call = (
            V(chra_0, MonoText("("), c, MonoText(")")).arrange().next_to(res, DOWN)
        )
        self.play(FadeIn(c, shift=DOWN))
        self.play(RT(chra_1, chra_0), Write(chr_call[1]), Write(chr_call[3]))
        self.wait(1)
        remnants = V(*remnants)
        iter_box = stackvar_(YELLOW, 0).next_to(join_box, UP)
        iter_txt = SVGMobject("iter-rot", fill_color=WHITE).move_to(iter_box).scale(0.3)
        itera = V(iter_box, iter_txt)
        self.play(FadeOut(remnants, shift=4 * UP), code[5:].animate.to_edge(UL))
        self.play(T(t, itera), FadeOut(chr_call))
        self.wait(1)
