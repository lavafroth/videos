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
        MonoText.set_default(font=codefont, font_size=32)
        raw = """
192 CALL_FUNCTION            2
194 CALL_METHOD              1
196 STORE_NAME              10 (result_text)
198 LOAD_CONST              39 (None)
200 RETURN_VALUE
        """.strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[0].set_opacity(1)
        stack.shift(4.5 * DOWN + 4 * RIGHT)

        eb = stackvar_(ORANGE).set_z_index(-1).next_to(stack, UP)
        et = MonoText("''").move_to(eb)
        e = V(et, eb)

        jb = stackvar_(PURPLE).set_z_index(-1).next_to(eb, UP)
        jt = MonoText("join").move_to(jb)
        j = V(jt, jb)

        iter_box = stackvar_(YELLOW, 0).next_to(jb, UP)
        iter_txt = (
            SVGMobject("iter-rot", fill_color=WHITE)
            .move_to(iter_box)
            .scale(0.3)
        )
        i = V(iter_box, iter_txt)
        self.add(e, j, i, code, stack)
        self.play(code[1].animate.set_opacity(1), code[0].animate.set_opacity(.5))
        self.wait(1)

        breh = MonoText("''.join(  )", font=codefont, t2c={"''": ORANGE, "join(": PURPLE, ")": PURPLE})
        brehiter = iter_txt.copy().move_to(breh[-2:].get_center())
        self.play(
            RT(e, breh[:2]),
            Write(breh[2]),
            RT(j, breh[3:7]),
            Write(breh[7]),
            Write(breh[-1]),
            T(i, brehiter)
        )

        self.wait(4)
        sqs = V(
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=[0.05, 0.05, 0, 0]),
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=[0, 0, 0, 0]),
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=[0, 0, 0, 0]),
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=[0, 0, 0.05, 0.05]),
        ).arrange(buff=0).next_to(breh, DOWN)
        sqsr = V(
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=.05),
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=.05),
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=.05),
            RoundedRectangle(width=1, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=.5, corner_radius=.05),
        ).arrange().next_to(breh, DOWN)
        self.play(i.animate.rotate(PI/2))
        self.play(Create(sqsr))
        self.play(T(sqsr, sqs))
        self.wait(1)
        self.play(FadeOut(i, breh), sqsr.animate.next_to(stack, UP))
        self.wait(1)
        self.play(code[2].animate.set_opacity(1), code[1].animate.set_opacity(.5))
        rt = code[2][-12:-1]
        rto = rt.copy().set(color=ORANGE)
        self.play(RT(sqsr, rto))
        rt.shift(1000 * DOWN)
        self.play(code[3:].animate.set_opacity(1), code[2].animate.set_opacity(.5), rto.animate.set_opacity(.5))
        self.wait(4)
        self.play(rto.animate.move_to(ORIGIN).scale(2).set_opacity(1), FadeOut(stack, shift=DOWN), FadeOut(code, shift=UP))
        self.wait(3)
