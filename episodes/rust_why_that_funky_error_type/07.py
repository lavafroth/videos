#!/usr/bin/env manim
# coding: utf-8

from manim import *
from hackermanim import *

class TraitIntro(Scene):
    def construct(self):
        box = Code(code=' Box<dyn std::error::Error>', language='rust', font_size=40)[2][0]
        self.add(box)
        throwaway_l = box[:len(' Box<dyn')]
        serr = box[len(' Box<dyn '):-1]
        throwaway_r = box[-1]
        self.play(
            throwaway_l.animate.shift(11 * LEFT),  
            throwaway_r.animate.shift(11 * RIGHT),
            serr.animate.shift(1.25 * LEFT),
        )
        self.wait(2)
        trait_def = Code(code='trait Error {\n\n}', language='rust', font_size=40)[2]
        serr_t = serr[:len('std::error::')]
        serr = serr[len('std::error::'):]
        self.play(AnimationGroup(
            Write(trait_def[0][:len('trait ')]),
            Write(trait_def[0][-1]),
            Write(trait_def[1:]),
            FadeOut(serr_t)),
            Transform(serr, trait_def[0][len('trait '):-1])
        )
        self.wait(4)
        _trait_def = Code(code='trait Error {\n\n}', language='rust')[2].to_edge(LEFT).shift(0.2 * LEFT + 0.1 * UP)
        method = Code(code='    fn fmt(&self, f: &mut std::fmt::Formatter<\'_>) -> std::fmt::Result;',
                      language='rust')[2][0]
        serr.set_opacity(0)
        self.play(
            Transform(trait_def, _trait_def),
            Write(method),
        )
        self.wait(2)
        trait_def = Group(trait_def, method)
        text = Text("* Technically, the Error trait relies on the Display or the Debug trait to put the constraint of having the fmt method.\nFor the sake of brevity, I'm writing it as a part of the Error trait itself.", font_size=16).to_edge(DOWN)
        self.play(FadeIn(text))
        decl = Code(code='let e: Box<dyn std::error::Error> = Box::new(CustomStruct{});', language='rust')[2][0].shift(1.5 * DOWN)
        self.play(
            Create(Line(start=10 * LEFT, end=10*RIGHT, stroke_width=1)),
            trait_def.animate.shift(2 * UP),
            Write(decl),
        )
        _ripple_decl_thing = decl[len('let e: Box<dyn std::error::Error> = Box::new('):len('let e: Box<dyn std::error::Error> = Box::new(CustomStruct')]
        self.play(ripple(_ripple_decl_thing), run_time=1)
        self.wait(2)
        self.play(ripple(method), run_time=3)
        self.wait(4)
