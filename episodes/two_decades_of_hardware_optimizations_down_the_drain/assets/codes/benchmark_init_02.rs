fn init(count: usize) -> Vec<Shape> {
    let mut shapes: Vec<Shape> = Vec::with_capacity(count);
    for i in 0..count {
        match i % 4 {
            0 => shapes.push(Shape::Square { side: i as f32 }),
            1 => shapes.push(Shape::Rectangle {
                height: i as f32,
                width: i as f32 * 2f32,
            }),
            2 => shapes.push(Shape::Triangle {
                base: i as f32,
                height: i as f32 * 2f32,
            }),
            3 => shapes.push(Shape::Circle { radius: i as f32 }),
            _ => panic!("impossible to get another value"),
        }
    }

    shapes
}
