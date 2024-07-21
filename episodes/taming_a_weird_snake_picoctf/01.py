#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")


        ps = [44, 100-(44+25), 25]
        ps_ = [30, 42, 27]

        ts = ('Capture the flag explainers', 'Programming design patterns', 'Linux automation guides')
        colors = (BLUE, TEAL, GREEN)

        def textbox(t, color, width, width3):
            text_object = Text(t, font_size=32).set(z_index=1)
            box = RoundedRectangle(width=width, height=text_object.height + 0.5, color=color, fill_color=color, fill_opacity=0.4, corner_radius=0.1)
            box2 = RoundedRectangle(width=0.2, height=text_object.height + 0.5, color=color, fill_color=color, fill_opacity=0.4, corner_radius=0.1)
            box3 = RoundedRectangle(width=width3, height=text_object.height + 0.5, color=color, fill_color=color, fill_opacity=0.4, corner_radius=0.1)
            return [text_object, box, box2, box3]
        
        textboxes= [textbox(t, color, p/100 * 10, p_/100 * 10) for (t, color, p, p_) in zip(ts, colors, ps, ps_)]
        ts = VGroup(*[textbox_[0] for textbox_ in textboxes]).arrange(direction=DOWN, buff=1, aligned_edge=LEFT).shift(1.5 * LEFT)
        boxes = VGroup(*[textbox_[1] for textbox_ in textboxes]).arrange(direction=DOWN, buff=0.5, aligned_edge=LEFT).shift(3 * LEFT)
        box3s = VGroup(*[textbox_[3] for textbox_ in textboxes]).arrange(direction=DOWN, buff=0.5, aligned_edge=LEFT).shift(3 * LEFT)
        box2s = [textbox_[2].move_to(textbox_[1].get_center() + textbox_[1].width / 2 * LEFT) for textbox_ in textboxes]
        poll_q = Text("Which of these fields do you feel more interested in?", font_size=36).shift(3 * UP)
        pcts = VGroup(*[Text(f'{p}%') for p in ps]).arrange(direction=DOWN, buff=1, aligned_edge=RIGHT).shift(4.5 * RIGHT)

        self.play(FadeIn(poll_q), (Create(b) for b in box2s))
        self.play(Write(ts), (ReplacementTransform(box2, box) for box2, box in zip(box2s, boxes)))
        self.play(FadeIn(pcts))
        self.wait(4)

        pcts_ = VGroup(*[Text(f'{p}%') for p in ps_]).arrange(direction=DOWN, buff=1, aligned_edge=RIGHT).shift(4.5 * RIGHT)
        self.play((Transform(p, p_) for p, p_ in zip(pcts, pcts_)), (Transform(p, p_) for p, p_ in zip(boxes, box3s)))
        self.wait(6)
