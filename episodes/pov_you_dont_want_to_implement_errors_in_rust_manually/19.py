#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        et = Code("stderr.rs", font_size=32)[2].shift(0.2 * LEFT)
        self.add(et)
        u = et[1:-1]
        self.play(u.animate.set_opacity(0.5))
        self.wait(1)
        buff = et[0][0].height
        a = CurvedArrow(
            et[0][12].get_center() + buff, et[0][19].get_center() + buff, angle=-PI / 2
        )
        b = CurvedArrow(
            et[0][12].get_center() + buff, et[0][28].get_center() + buff, angle=-PI / 2
        )
        d = Text("requires", font_size=28).move_to(
            (a.get_center() + a.get_center()) / 2 + 1 * UP + 0.8 * RIGHT
        )
        self.play(Create(a), Create(b), Write(d))
        self.wait(1)
        dis = et[0][25:-2]
        self.play(FadeOut(et[1:], a, b, d, et[0][:25], et[0][-2:]))
        d = Code("display.rs", font_size=32)[2]
        self.play(
            FadeIn(d[1:], d[0][:10], d[0][-2:]), ReplacementTransform(dis, d[0][10:-2])
        )
        self.play(d.animate.to_edge(UP))
        log = Code(
            code="ERROR: Timed out receiving packets from request stream\nERROR: I am a teapot",
            language="html",
            insert_line_no=False,
            background="window",
        ).scale(1.2)
        self.play(FadeIn(log[0]))
        self.play(Write(log[2][0]))
        self.play(Write(log[2][1]))
        self.wait(2)
        c_1 = '''use thiserror::Error;

#[derive(Error, Debug)]
pub enum MyError {
    Permission,
    Timeout,
}
'''
        c_1 = Code(code=c_1, language='rust', font_size=40)[2].shift(10 * LEFT)
        self.play(Group(d, log).animate.shift(16 * RIGHT), c_1.animate.shift(10 * RIGHT))
        self.wait(2)
