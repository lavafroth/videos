#!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import *

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """>>  134 LOAD_NAME                3 (   )
    136 LOAD_NAME                2 (        )
    138 CALL_FUNCTION            1
    140 LOAD_NAME                3 (len)
    142 LOAD_NAME                0 (input_list)
    144 CALL_FUNCTION            1
    146 COMPARE_OP               0 (<)
    148 POP_JUMP_IF_FALSE      162"""
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5).shift(LEFT)

        stack.shift(2.5 * DOWN + 4 * RIGHT)
        code[2].set_opacity(1)
        self.add(code, stack)
        me = stackvar(BLUE).next_to(stack, UP).set_z_index(-1)
        tete = MonoText('len(key_list)',  t2c={'len(':PURPLE, ')': PURPLE}).shift(.5 * DOWN)
        tete_ = MonoText('len(key_list)', t2c={'len(':LIGHT_PINK, ')': LIGHT_PINK}).move_to(me)
        self.play(Transform(tete, tete_), Create(me))
        self.wait(2)
        self.play(code[3].animate.set_opacity(1), code[2].animate.set_opacity(.5))
        len_ = code[3][-4:-1].set_opacity(0)
        self.play(VGroup(stack, me, tete).animate.shift(DOWN * (1 + MED_SMALL_BUFF)))
        self.play(code[4].animate.set_opacity(1), code[3][:-4].animate.set_opacity(.5), code[3][-1].animate.set_opacity(.5))
        meme = stackvar(WHITE).next_to(me, UP).set_z_index(-1)
        meme = stackvar(WHITE).next_to(meme, UP).set_z_index(-1)
        input_list = code[4][-11:-1]
        input_list_box = code[4][-11:-1].copy()
        self.play(input_list.animate.move_to(meme), Transform(input_list_box, meme))
        gr = VGroup(input_list, input_list_box)
        self.play(code[4][:-11].animate.set_opacity(0.5), code[4][-1].animate.set_opacity(0.5), code[5].animate.set_opacity(1))
        teteh = MonoText('len(input_list)', t2c={'len(':PURPLE, ')': PURPLE}).shift(.5 * DOWN)
        self.play(ReplacementTransform(gr, teteh[4:-1]))
        self.add(teteh)
        meesa = stackvar(BLUE).next_to(stack, UP)
        meesa = meesa.next_to(meesa, UP).set_z_index(-1)
        teteh_ = MonoText('len(input_list)', t2c={'len(':LIGHT_PINK, ')': LIGHT_PINK}).move_to(meesa)
        self.play(Transform(teteh, teteh_), Create(meesa))
        self.play(code[6].animate.set_opacity(1), code[5].animate.set_opacity(.5))

        input_list = VGroup(teteh, meesa)
        key_list = VGroup(tete, me)

        input_list_copy = input_list.copy()
        key_list_copy = key_list.copy()
        input_list.set_opacity(0)
        key_list.set_opacity(0)
        cmp = code[6][-2]
        cmp.set_opacity(0)
        self.wait(2)
        raw_2 = """150 LOAD_NAME                2 (key_list)
152 LOAD_METHOD              4 (extend)
154 LOAD_NAME                2 (key_list)
156 CALL_METHOD              1
158 POP_TOP
160 JUMP_ABSOLUTE          134"""
        code_2 = MonoParagraph(raw_2).next_to(code, DOWN, buff=0).set_opacity(0.5).shift(.2 * RIGHT + .5 * UP)
        self.play(FadeIn(code_2, shift=2 * UP))
        self.wait(1)
        self.play(FadeOut(code_2, shift=2 * DOWN))
        code.set_opacity(0)
        stack.set_opacity(0)
        self.add(input_list_copy)
        self.add(key_list_copy)
        cmp.set_opacity(1)
        vg = VGroup(key_list_copy, cmp, input_list_copy)
        self.play(vg.animate.arrange())
        self.play(vg.animate.scale(.6).to_edge(DL))
        self.wait(3)
        self.play(FadeOut(vg, shift=4 * LEFT))

