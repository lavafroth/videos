#!/usr/bin/env manim
from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from custom import CodeTransformer, octicon


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")

        impl = Code(code='''impl Shape {
    fn new(shape_type: ShapeType) -> Self {
        match shape_type {
            ShapeType::Square { side } => Shape {
                multiplier: 1f32,
                width: side,
                height: side,
            },
            ShapeType::Rectangle { width, height } => Shape {
                multiplier: 1f32,
                width,
                height,
            },
            ShapeType::Triangle { base, height } => Shape {
                multiplier: 0.5f32,
                width: base,
                height,
            },
            ShapeType::Circle { radius } => Shape {
                multiplier: PI,
                width: radius,
                height: radius,
            },
        }
    }''', language='rust', font_size=22)[2]
        self.add(impl)
        anims = []
        for char in impl[4]:
            curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]).move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=1.5)
        anims = []

        self.wait(1)

        for char in impl[19]:
            curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]).move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=1.5)
        self.play(FadeOut(impl))
