#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        text = Text('thiserror::Error',font=codefont, font_size=32).scale(2)
        self.add(text)
        anims = []
        curve = ParametricFunction(lambda t: np.array([0, 0.2 * np.sin(PI * t), 0]), t_range=[0, 1])
        for char in text[len('thiserror::'):]:
            curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=.1))
        self.wait(1)
        crate = octicon('package-24', color=None, fill_color=WHITE).scale(.75)
        self.play(Transform(text, crate))
        self.wait(2)
        self.play(text.animate.to_edge(UR))
        run = '''cargo add thiserror
    Updating crates.io index
      Adding thiserror v1.0.61 to dependencies.
    Updating crates.io index
'''
        r = Paragraph(run, font=codefont, t2c={'Updating': GREEN,'Adding': GREEN}, font_size=36)
        self.play(Write(r[0]))
        self.play(Write(r[1:]))
        self.play(FadeOut(r, text))
