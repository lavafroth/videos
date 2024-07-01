#!/usr/bin/env manim
from manim import *
from hackermanim import *

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
        self.play(ripple(impl[4]), run_time=1.5)
        self.wait(1)

        self.play(ripple(impl[19]), run_time=1.5)
        self.play(FadeOut(impl))
