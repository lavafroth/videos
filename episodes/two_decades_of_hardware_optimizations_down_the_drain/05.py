#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        
        ferris = SVGMobject('../assets/rustacean-flat-gesture').scale(.8).shift(4 * RIGHT)
        ferris_gesture_down = SVGMobject('../assets/rustacean-flat-gesture-down').scale(.8).shift(4 * RIGHT)
        code = Code('trait_definitions.rs', font_size=34).shift(2 * LEFT)[2]
        self.add(ferris, code)
        text = Text("Polymorphism").shift(2*LEFT)
        self.wait(3)
        self.play(Transform(ferris, ferris_gesture_down), Transform(code, text))
        subtext_raw = "shared behavior > conditional statements"
        subtext = Text(subtext_raw, font_size=22).shift(2 * LEFT + DOWN)
        gt = subtext[14:15]
        sb = subtext[:14]
        cs = subtext[15:]
        self.play(AnimationGroup(
                AnimationGroup(
                    FadeIn(sb),
                    FadeIn(cs),
                ),
                Write(gt),
                lag_ratio=.5
        ))
        self.wait(5)
        grp = Group(code, gt, sb, cs)
        code = Code('trait_version_overview.rs', font_size=28).shift(2 * LEFT)[2]
        self.play(Transform(grp, code))

        curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1])
        ripples = []
        for line in (0, 4):
            anims = []
            for char in grp[line][:13]:
                curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
                anims.append(MoveAlongPath(char, curve))
            ripples.append(AnimationGroup(anims, lag_ratio=0.1))
        self.play(*ripples, run_time=1.5)

        self.wait(1)

        ripples = []
        for line in (9, 15):
            anims = []
            for char in grp[line][:-1]:
                curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
                anims.append(MoveAlongPath(char, curve))
            ripples.append(AnimationGroup(anims, lag_ratio=0.1))
        self.play(*ripples, run_time=1.5)

        self.wait(2)
        self.play(FadeOut(grp), FadeOut(ferris))
