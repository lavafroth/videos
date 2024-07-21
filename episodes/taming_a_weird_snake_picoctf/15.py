#!/usr/bin/env manim
from manim import *
from hackermanim import *
from stack import stackvar

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font='Poppins')
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        vm = SVGMobject('server-24').set_z_index(1).scale(0.7)
        self.play(vm.animate.fade(0.5))

        n = 5
        stack = (stackvar(BLUE).fade(x/n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(DOWN)
        title = Text('Stack machine', font_size=36).to_edge(UP)
        self.play(ReplacementTransform(vm, stack), Write(title))
        st = Text('Stack top', font_size=32).next_to(stack[0], LEFT, buff=1.5)
        arrow = Arrow(st, stack[0].get_edge_center(LEFT))
        self.play(Write(st), Create(arrow))
        self.wait(1)
        sv = RoundedRectangle(width=4, height=1, color=TEAL, fill_color=TEAL, fill_opacity=0.5, corner_radius=0.05)
        old_stack =stack.copy()
        stack_ = stack.copy()
        head = MonoText('instructions:')
        ins = MonoParagraph('''LOAD_CONST 2
POP_TOP''')
        ins[1].set_opacity(0.5)
        instr = VGroup(head, ins).arrange(DOWN).to_edge(DR)
        self.play(FadeIn(instr))
        stack_new = VGroup(sv, stack_).arrange(DOWN).shift(1.6 * DOWN)
        self.play(Transform(stack, stack_))
        self.play(FadeIn(sv, shift=3.5 * LEFT))
        self.play(ins[0].animate.set_opacity(0.5), ins[1].animate.set_opacity(1))
        self.play(FadeOut(sv, shift=3.5 * RIGHT))
        self.play(Transform(stack, old_stack))
        self.play(ins[1].animate.set_opacity(0.5))
        self.wait(2)
