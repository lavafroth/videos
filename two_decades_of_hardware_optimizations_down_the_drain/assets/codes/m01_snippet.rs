trait Shape {
    fn area(&self) -> f32;
    fn corner(&self) -> f32;
}

struct Square {
    side: f32,
}

impl Shape for Square {
    fn area(&self) -> f32 {
        self.side * self.side
    }
}

struct Rectangle {
    width: f32,
    height: f32,
}
