#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        c = '''pub enum MyError {
    Permission,
    Timeout,
}
'''

        c_ = '''use thiserror::Error;

#[derive(Error)]
pub enum MyError {
    Permission,
    Timeout,
}
'''
        c_1 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    Permission,
    Timeout,
}
'''
        c = Code(code=c, language='rust', font_size=40)[2]
        c_ = Code(code=c_, language='rust', font_size=40)[2]
        c_1 = Code(code=c_1, language='rust', font_size=40)[2]
        self.play(Write(c))
        self.wait(2)
        self.play(ReplacementTransform(c[:], c_[3:]))
        self.play(Write(c_[0]))
        self.wait(1)
        self.play(Write(c_[2]))
        self.wait(2)
        a, b = c_[2][:len('#[derive(Error')], c_[2][-len(')]'):]
        a_1, b_1 = c_1[2][:len('#[derive(Error')], c_1[2][-len(')]'):]
        self.play(
            ReplacementTransform(a, a_1),
            ReplacementTransform(b, b_1),
            Write(c_1[2][len('#[derive(Error'):-2]),
            ReplacementTransform(c_[:2], c_1[:2]),
            ReplacementTransform(c_[3:], c_1[3:]),
        )
        self.wait(2)
        self.play(c_1.animate.shift(3 * LEFT))
        off = .5 * UP
        deb = Code(code='"{:?}"', language='rust', font_size=40)[2].shift(3 * RIGHT).set_opacity(0).shift(off)
        t = Text('Debug formatter', font_size=32).next_to(deb, direction=DOWN, buff=1).set_opacity(0).shift(off)
        self.play(x.animate.shift(-off).set_opacity(1) for x in (deb, t))
        self.wait(2)
        self.play(x.animate.shift(-off).set_opacity(0) for x in (deb, t))
        et = Code('stderr.rs', font_size=32)[2].shift(16 * RIGHT)
        self.play(c_1.animate.shift(8 * LEFT), et.animate.shift(16.2 * LEFT))
        self.wait(1)
