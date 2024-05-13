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
