enum Shape {
    Square { side: f32 },
    Rectangle { width: f32, height: f32 },
    Triangle { base: f32, height: f32 },
    Circle { radius: f32 },
}

impl Shape {
    fn area(&self) -> f32 {
        match self {
            Shape::Square { side } => side * side,
            Shape::Rectangle { width, height } => width * height,
            Shape::Triangle { base, height } => 0.5 * base * height,
            Shape::Circle { radius } => PI * radius * radius,
        }
    }
}
