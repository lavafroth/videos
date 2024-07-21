#!/usr/bin/env manim

from manim import *
from manim import VGroup as V
from hackermanim import *
from stack import stack, stackvar as stackvar_


def stackvar(color, opacity=0.5):
    return stackvar_(color, opacity).set_z_index(-1)


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)
        raw = """
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[0].set_opacity(1)
        stack.shift(4.5 * DOWN + 4 * RIGHT)
        self.add(code, stack)
        phantom = stackvar(WHITE).next_to(stack, UP)
        zip = V(stackvar(PURPLE), MonoText("zip")).next_to(phantom, UP)
        input_list = V(stackvar(WHITE), MonoText("input_list")).next_to(zip, UP)
        key_list = V(stackvar(WHITE), MonoText("key_list")).next_to(input_list, UP)

        fcall = MonoText(
            "zip(input_list, key_list)",
            t2c={"zip": PURPLE},
        )
        zoe = V(fcall[:4], fcall[14], fcall[-1])
        kl = fcall[4:14]
        il = fcall[15:-1]
        self.play(
            ReplacementTransform(zip, zoe),
            ReplacementTransform(key_list, kl),
            ReplacementTransform(input_list, il),
        )
        iter_box = stackvar(YELLOW_B, 0)
        iter_txt = (
            SVGMobject("iter-rot", fill_color=WHITE)
            .move_to(iter_box)
            .scale(0.3)
            .shift(1.5 * LEFT)
        )
        itera = V(iter_txt, iter_box).next_to(phantom, UP)
        kc = Circle(radius=0.2, color=WHITE, fill_color=WHITE, fill_opacity=0.2)
        ic = Circle(radius=0.2, color=WHITE, fill_color=WHITE, fill_opacity=0.2)
        V(kc, ic).arrange().move_to(iter_box).shift(RIGHT)
        self.wait(2)
        self.play(
            ReplacementTransform(zoe, itera),
            ReplacementTransform(kl, kc),
            ReplacementTransform(il, ic),
        )
        self.wait(1)
        kcc = kc.copy().shift(UP)
        icc = ic.copy().shift(UP)
        sep = MonoText("(  ,  )", font_size=36).move_to(
            (kcc.get_center() + icc.get_center()) / 2
        )
        self.play(
            iter_txt.animate.rotate(PI / 2),
            FadeIn(kcc, icc, sep, shift=UP),
        )
        kcc_ = kc.copy().shift(UP)
        icc_ = ic.copy().shift(UP)
        sep_ = sep.copy().move_to(
            (kcc.get_center() + icc.get_center()) / 2
        )
        self.play(
            iter_txt.animate.rotate(PI / 2),
            FadeIn(kcc_, icc_, sep_, shift=UP),
            FadeOut(kcc, icc, sep, shift=UP),
        )
        self.play(
            FadeOut(kcc_, icc_, sep_, shift=UP),
        )
        self.wait(1)
        self.play(code[0].animate.set_opacity(0.5), code[1].animate.set_opacity(1))
        self.wait(1)
        self.play(code[1].animate.set_opacity(0.5), code[2].animate.set_opacity(1))
        self.wait(5.5)
        self.play(
            FadeOut(code, shift=4 * UP), V(itera, kc, ic).animate.next_to(stack, UP)
        )
        self.wait(1)
