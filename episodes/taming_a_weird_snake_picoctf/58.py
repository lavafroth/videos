#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """>>    4 FOR_ITER                12 (to 18)
      6 STORE_FAST               1 (char)
      8 LOAD_GLOBAL              0 (ord)
     10 LOAD_FAST                1 (char)
     12 CALL_FUNCTION            1
     14 LIST_APPEND              2
     16 JUMP_ABSOLUTE            4
>>   18 RETURN_VALUE"""
        code = MonoParagraph(raw).to_edge(UL)
        turbo_0 = code[0][:2]
        turbo_1 = code[-1][:2]
        self.add(turbo_0, turbo_1)
        curve_0 = ParametricFunction(lambda t: np.array([0.2 * (1 + np.sin(2 * PI * t)), 0, 0]), t_range=[0, 2]).move_to(turbo_0)
        curve_1 = ParametricFunction(lambda t: np.array([0.2 * (1 + np.sin(2 * PI * t)), 0, 0]), t_range=[0, 2]).move_to(turbo_1)
        self.play(MoveAlongPath(turbo_0, curve_0), MoveAlongPath(turbo_1, curve_1), run_time=2)
        self.wait(1)
