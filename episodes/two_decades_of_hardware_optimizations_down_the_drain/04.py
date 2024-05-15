#!/usr/bin/env manim
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from custom import octicon

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        
        ferris = SVGMobject('rustacean-flat-noshadow')
        ferris_gesture = SVGMobject('rustacean-flat-gesture').scale(.8).shift(4 * RIGHT)
        self.play(FadeIn(ferris))
        self.wait(4)
        self.play(Transform(ferris, ferris_gesture))
        code = Code('struct_definitions.rs', font_size=34).shift(2 * LEFT)[2]
        self.play(FadeIn(code))
        self.wait(2)
        _code = code.copy().shift(6 * UP).set_opacity(0)

        _ncode = Code('trait_definitions.rs', font_size=34).shift(2 * LEFT)[2]
        ncode = _ncode.copy().shift(6 * DOWN).set_opacity(0)
        self.play(Transform(ncode, _ncode), Transform(code, _code))
        self.wait(6)
