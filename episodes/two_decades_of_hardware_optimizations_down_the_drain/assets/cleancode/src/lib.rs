#![feature(test)]
#![allow(dead_code)]
extern crate test;
const COUNT: usize = 1024 * 10;
use std::f32::consts::PI;

pub enum ShapeType {
    Square { side: f32 },
    Rectangle { width: f32, height: f32 },
    Triangle { base: f32, height: f32 },
    Circle { radius: f32 },
}

pub struct Shape {
    pub multiplier: f32,
    pub corner_area_multiplier: f32,
    pub width: f32,
    pub height: f32,
}

impl Shape {
    pub fn new(shape_type: ShapeType) -> Self {
        match shape_type {
            ShapeType::Square { side } => Shape {
                multiplier: 1f32,
                corner_area_multiplier: 1f32 / (1f32 + 4f32),
                width: side,
                height: side,
            },
            ShapeType::Rectangle { width, height } => Shape {
                multiplier: 1f32,
                corner_area_multiplier: 1f32 / (1f32 + 4f32),
                width,
                height,
            },
            ShapeType::Triangle { base, height } => Shape {
                multiplier: 0.5f32,
                corner_area_multiplier: 0.5f32 / (1f32 + 4f32),
                width: base,
                height,
            },
            ShapeType::Circle { radius } => Shape {
                multiplier: PI,
                corner_area_multiplier: PI,
                width: radius,
                height: radius,
            },
        }
    }

    pub fn area(&self) -> f32 {
        self.multiplier * self.width * self.height
    }

    pub fn corner_area(&self) -> f32 {
        self.corner_area_multiplier * self.width * self.height
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::COUNT;
    use test::Bencher;

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

    #[bench]
    fn total_area(b: &mut Bencher) {
        let shapes = init(COUNT);

        b.iter(|| {
            let mut accum = 0f32;
            for shape in &shapes {
                accum += shape.area();
            }

            accum
        });
    }

    #[bench]
    fn total_area_sum4(b: &mut Bencher) {
        let shapes = init(COUNT);

        b.iter(|| {
            let mut accum1 = 0f32;
            let mut accum2 = 0f32;
            let mut accum3 = 0f32;
            let mut accum4 = 0f32;

            let count = COUNT / 4;
            let mut iter = 1;
            while count - iter > 0 {
                accum1 += shapes[iter * 4].area();
                accum2 += shapes[1 + (iter * 4)].area();
                accum3 += shapes[2 + (iter * 4)].area();
                accum4 += shapes[3 + (iter * 4)].area();

                iter += 1;
            }

            accum1 + accum2 + accum3 + accum4
        });
    }

    #[bench]
    fn corner_area(b: &mut Bencher) {
        let shapes = init(COUNT);

        b.iter(|| {
            let mut accum = 0f32;
            for shape in &shapes {
                accum += shape.corner_area();
            }

            accum
        });
    }

    #[bench]
    fn corner_area_sum4(b: &mut Bencher) {
        let shapes = init(COUNT);

        b.iter(|| {
            let mut accum1 = 0f32;
            let mut accum2 = 0f32;
            let mut accum3 = 0f32;
            let mut accum4 = 0f32;

            let count = COUNT / 4;
            let mut iter = 1;
            while count - iter > 0 {
                accum1 += shapes[iter * 4].corner_area();
                accum2 += shapes[1 + (iter * 4)].corner_area();
                accum3 += shapes[2 + (iter * 4)].corner_area();
                accum4 += shapes[3 + (iter * 4)].corner_area();

                iter += 1;
            }

            accum1 + accum2 + accum3 + accum4
        });
    }
}
