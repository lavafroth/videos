enum ShapeType {
    Square,
    Rectangle,
    Triangle,
    Circle,
}

impl ShapeType {
    fn constant(&self) -> f32 {
        match self {
            ShapeType::Square => 1f32,
            ShapeType::Rectangle => 1f32,
            ShapeType::Triangle => 0.5f32,
            ShapeType::Circle => PI,
        }
    }
}

struct Shape {
    shape_type: ShapeType,
    width: f32,
    height: f32,
}
