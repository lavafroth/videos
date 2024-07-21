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
        code[2][:2].set_opacity(1)
        code[-1][:2].set_opacity(1)
        code[8].set_opacity(1)

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
        itera.next_to(lis, UP)
        abox = stackvar(BLUE).next_to(itera, UP)
        bbox = stackvar(BLUE).next_to(abox, UP)
        atxt = MonoText("a").move_to(abox)
        btxt = MonoText("b").move_to(bbox)
        a = V(abox, atxt)
        b = V(bbox, btxt)
        V(stack, itera, lis, itera_copy, a, b).shift(DOWN)
        bxor = code[8][-10:]
        self.add(bxor, a, b)
        opacity = 0.5
        abox1 = RoundedRectangle(
            width=1,
            height=1,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=opacity,
            corner_radius=0.05,
        ).set_z_index(-1)
        bbox1 = RoundedRectangle(
            width=1,
            height=1,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=opacity,
            corner_radius=0.05,
        ).set_z_index(-1)
        xor = Tex(r"$\oplus$").scale(1.5)
        axorb = V(abox1, xor, bbox1).arrange()
        self.play(
            ReplacementTransform(abox, abox1),
            ReplacementTransform(bbox, bbox1),
            ReplacementTransform(bxor, xor),
            atxt.animate.move_to(abox1),
            btxt.animate.move_to(bbox1),
        )
        t = Text("Exclusive OR").next_to(xor, UP).shift(UP)
        self.play(Write(t))
        axorb = V(V(atxt, abox1), xor, V(btxt, bbox1)).arrange()
        self.play(t.animate.to_edge(UP), axorb.animate.shift(2 * UP))
        tinv = Text("Involuntary function", font_size=34).to_edge(LEFT).shift(DOWN)
        self.play(FadeIn(tinv, shift=RIGHT))
        clone = axorb.copy()
        self.play(FadeIn(clone))
        self.play(clone.animate.next_to(tinv, DOWN))
        clonecopy = clone[1:].copy()
        self.play(FadeIn(clonecopy))
        acp = clone[0].copy()
        self.play(FadeIn(acp), clonecopy.animate.shift(2 * RIGHT))
        eq = Tex(r"$=$").scale(1.5).next_to(clonecopy)
        self.play(Write(eq), acp.animate.shift(6 * RIGHT))
        xor = Tex(r"$\oplus$").scale(1.5)
        left_0_0 = MonoText("0")
        left_1_0 = MonoText("1")
        eq_0 = Tex(r"$=$").scale(1.5)
        res_0 = MonoText("1")
        v = V(left_0_0, xor, left_1_0, eq_0, res_0).arrange().next_to(axorb, DOWN)
        self.play(Write(v))
        self.play(
            left_0_0.animate.move_to(left_1_0),
            left_1_0.animate.move_to(left_0_0),
        )
        self.play(
            left_0_0.animate.move_to(left_1_0),
            left_1_0.animate.move_to(left_0_0),
        )

        left_0_1 = MonoText("0")
        right_0_1 = MonoText("0")
        eq_1 = Tex(r"$=$").scale(1.5)
        res_1 = MonoText("0")
        v = V(left_0_1, xor.copy(), right_0_1, eq_1, res_1).arrange().next_to(v, DOWN)
        self.play(Write(v))
        self.wait(1)
        left_1_1 = MonoText("1").move_to(left_0_1)
        right_1_1 = MonoText("1").move_to(right_0_1)
        self.play(
            Transform(left_0_1, left_1_1),
            Transform(right_0_1, right_1_1),
        )
        self.wait(1)
