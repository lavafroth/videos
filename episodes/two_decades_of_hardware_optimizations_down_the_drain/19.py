#!/usr/bin/env manim
from manim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        enum = Code(code='''enum ShapeType {
    Square,
    Rectangle,
    Triangle,
    Circle,
}''', language='rust', font_size=34)[2]
        self.add(enum)
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
        _impl = impl.copy().shift(6 * DOWN).set_opacity(0)
        self.play(enum.animate.shift(6 * UP).set_opacity(0), Transform(_impl, impl))
        self.wait(7)
