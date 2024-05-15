trait Shape {
    fn area(&self) -> f32;
}

impl Shape for Square {
    fn area(&self) -> f32 {
        self.side * self.side
    }
}

impl Shape for Rectangle {
    fn area(&self) -> f32 {
        self.width * self.height
    }
}
