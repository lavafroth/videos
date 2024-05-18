use cleancode::Shape;
use cleancode::ShapeType;
fn init(count: usize) -> Vec<Shape> {
    let mut shapes: Vec<Shape> = Vec::with_capacity(count);
    for i in 0..count {
        match i % 4 {
            0 => shapes.push(Shape::new(ShapeType::Square { side: i as f32 })),
            1 => shapes.push(Shape::new(ShapeType::Rectangle {
                width: i as f32,
                height: i as f32 * 2f32,
            })),
            2 => shapes.push(Shape::new(ShapeType::Triangle {
                base: i as f32,
                height: i as f32 * 2f32,
            })),
            3 => shapes.push(Shape::new(ShapeType::Circle { radius: i as f32 })),
            _ => panic!("impossible to get another value"),
        }
    }

    shapes
}

fn main() {
    let count = 10240;
    let shapes = init(count);
    let mut accum1 = 0f32;
    let mut accum2 = 0f32;
    let mut accum3 = 0f32;
    let mut accum4 = 0f32;

    for iter in (0..count).step_by(4) {
        accum1 += shapes[iter].area();
        accum2 += shapes[iter + 1].area();
        accum3 += shapes[iter + 2].area();
        accum4 += shapes[iter + 3].area();
    }
    let accum = accum1 + accum2 + accum3 + accum4;
    println!("{}", accum);
}
