#!/usr/bin/env manim

from manim import *
from manim import VGroup as V
from hackermanim import *
from stack import *

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
        self.add(chra)
        res_box = stackvar(WHITE).next_to(stack, UP).set_z_index(-1)
        res_box = res_box.next_to(res_box, UP)
        res_box = res_box.next_to(res_box, UP)
        res_box = res_box.next_to(res_box, UP)
        self.play(Transform(chra.copy(), res_box), chra.animate.move_to(res_box))
        self.wait(5)
