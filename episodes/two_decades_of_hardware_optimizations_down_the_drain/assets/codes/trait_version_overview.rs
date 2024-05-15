struct Square {
    side: f32,
}

struct Circle {
    radius: f32,
}

impl Shape for Circle {
    fn area(&self) -> f32 {
        PI * self.radius * self.radius
    }
}

impl Shape for Square {
    fn area(&self) -> f32 {
        self.side * self.side
    }
}
