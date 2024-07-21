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
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[2].set_opacity(1)
        code[-1][:2].set_opacity(1)

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
        lis = stackvar(WHITE, 0).next_to(itera, UP)
        itera_copy = itera.copy()
        self.add(stack, code, itera_copy, lis)
        itera.next_to(lis, UP)
        self.add(itera)
        self.wait(1)
        kcc = kc.copy().shift(UP)
        icc = ic.copy().shift(UP)
        center = (kcc.get_center() + icc.get_center()) / 2
        sep = MonoText("(  ,  )", font_size=36).move_to(center)
        self.wait(1)
        self.play(
            iter_txt.animate.rotate(PI / 2),
            FadeIn(kcc, icc, sep, shift=UP),
        )
        ctn = stackvar(WHITE, 0).next_to(itera, UP)
        thres = 0.15
        w = (4 - 4 * thres) / 2
        h = (1 - thres / 4) / 2
        c1 = RoundedRectangle(
            width=w,
            height=h,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.5,
            corner_radius=0.05,
        )
        c2 = RoundedRectangle(
            width=w,
            height=h,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.5,
            corner_radius=0.05,
        )
        cs = V(c1, c2).arrange(buff=thres).move_to(ctn)
        self.play(
            ReplacementTransform(sep, ctn),
            ReplacementTransform(kcc, c1),
            ReplacementTransform(icc, c2),
        )
        self.play(
            code[2][2:].animate.set_opacity(0.5),
            code[3].animate.set_opacity(1),
        )
        anim = V(stack, itera, lis, itera_copy, cs, ctn).animate.shift(DOWN)
        self.play(anim)
        self.play(ripple(code[3][1:-1]))
        center_correction = 0.05 * UP
        s = SurroundingRectangle(code[3][-1], BLUE, corner_radius=0.05)
        curve = ParametricFunction(
            lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]
        ).move_to(cs.get_center() + center_correction)
        self.play(Create(s))
        self.wait(1)
        self.play(MoveAlongPath(cs, curve))
        c1_ = stackvar(BLUE).next_to(cs, UP)
        c2_ = stackvar(BLUE).next_to(c1_, UP)
        y = ctn.get_edge_center(DOWN)[1]
        self.play(
            Transform(c1, c1_),
            Transform(c2, c2_),
            ctn.animate.apply_function(
                lambda p: np.array(
                    [
                        p[0],
                        y,
                        0,
                    ]
                )
            ),
            lag_ratio=0.5,
        )
        self.play(V(c1, c2).animate.next_to(itera, UP), FadeOut(s, ctn))
        c1_ = c1.copy().set_z_index(-1)
        c2_ = c2.copy().set_z_index(-1)
        self.play(
            code[3].animate.set_opacity(0.5),
            code[4].animate.set_opacity(1),
        )
        a = code[4][-2].copy().set(color=BLUE)
        self.play(ReplacementTransform(c1, a))
        self.play(
            code[4].animate.set_opacity(0.5),
            code[5].animate.set_opacity(1),
        )
        b = code[5][-2].copy().set(color=BLUE)
        self.play(ReplacementTransform(c2, b))
        self.wait(1)

        self.play(
            code[5].animate.set_opacity(0.5),
            code[6].animate.set_opacity(1),
            a.animate.move_to(code[6][-2].get_center())
        )
        atxt = a.copy().move_to(c1_).set(color=WHITE)
        self.play(Transform(a, c1_), ReplacementTransform(a.copy(), atxt))
        self.play(
            code[6].animate.set_opacity(0.5),
            code[7].animate.set_opacity(1),
            b.animate.move_to(code[7][-2].get_center())
        )
        btxt = b.copy().move_to(c2_).set(color=WHITE)
        self.play(Transform(b, c2_), ReplacementTransform(b.copy(), btxt))
        self.play(
            code[7].animate.set_opacity(0.5),
            code[8].animate.set_opacity(1),
        )
        self.wait(1)
        a = V(a, atxt)
        b = V(b, btxt)
        a.set_opacity(0)
        b.set_opacity(0)
        bxor = code[8][-10:]
        bxor.set_opacity(0)
        self.wait(5)

