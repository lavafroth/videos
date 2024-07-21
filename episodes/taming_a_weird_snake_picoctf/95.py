#!/usr/bin/env manim

from manim import *
from manim import VGroup as V
from hackermanim import *
from stack import stack,stackvar as stackvar_


def stackvar(color, opacity=0.5):
    return stackvar_(color, opacity).set_z_index(-1)

def chunks3(obj, x, y):
    return (obj[:x], obj[x:y], obj[y:])

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)
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
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5).shift(.3 * LEFT)
        stack.shift(4.5 * DOWN + 4 * RIGHT)
        self.add(code, stack)
        self.play(code[0].animate.set_opacity(1))
        l, empty, r= chunks3(code[0], -3, -1)
        empty_box = stackvar(ORANGE).next_to(stack, UP)
        self.play(ReplacementTransform(empty.copy(), empty_box), empty.animate.move_to(empty_box))
        self.play(V(l, r).animate.set_opacity(0.5), code[1].animate.set_opacity(1))
        l, join, r = chunks3(code[1], -5, -1)
        join_box = stackvar(PURPLE).next_to(empty_box, UP)
        self.play(Transform(join.copy(), join_box), join.animate.move_to(join_box))
        self.play(V(l, r).animate.set_opacity(0.5), code[2].animate.set_opacity(1))
        l, mappa, r = chunks3(code[2], -4, -1)
        mappa_box = stackvar(PURPLE_B).next_to(join_box, UP)
        self.play(ReplacementTransform(mappa.copy(), mappa_box), mappa.animate.move_to(mappa_box))
        self.play(V(l, r).animate.set_opacity(0.5), code[3].animate.set_opacity(1))
        l, chra, r = chunks3(code[3], -4, -1)
        chra.set_opacity(0)
        self.wait(1)
        self.play(V(l, r).animate.set_opacity(0.5), code[4].animate.set_opacity(1))
        l, res, r = chunks3(code[4], -7, -1)
        res_box = stackvar(WHITE).next_to(mappa_box, UP)
        res_box = res_box.next_to(res_box, UP)
        self.play(Transform(res.copy(), res_box), res.animate.move_to(res_box))
        self.play(V(l, r).animate.set_opacity(0.5), code[5].animate.set_opacity(1))
        self.wait(5)
        two = code[5][-1]
        s = SurroundingRectangle(two, BLUE, corner_radius=0.05)
        self.play(Create(s))
        self.wait(1)
