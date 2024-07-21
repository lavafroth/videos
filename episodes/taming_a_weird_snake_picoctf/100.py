#!/usr/bin/env manim

from manim import *
from manim import VGroup as V, Transform as T
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
        
        code = MonoParagraph(raw).to_edge(UL).set_opacity(1).shift(.3 * LEFT)
        stack.shift(4.5 * DOWN + 4 * RIGHT)
        l, chra, r = chunks3(code[3], -4, -1)
        res_box = stackvar_(WHITE).next_to(stack, UP)
        res_box = stackvar_(WHITE).next_to(res_box, UP)
        res_box = stackvar_(WHITE).next_to(res_box, UP)
        res_box = stackvar_(WHITE).next_to(res_box, UP)
        chra.move_to(res_box)
        v = V(chra, res_box)
        t = MonoText("map(chr, result)", font_size=40).move_to(3.5 * LEFT + 2 * DOWN)
        self.add(v)
        self.play(T(v, t[4:7]))
        self.wait(1)
