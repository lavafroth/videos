#[bench]
fn total_area(b: &mut Bencher) {
    let shapes = init(COUNT);

    b.iter(|| {
        let mut accum1 = 0f32;
        let mut accum2 = 0f32;
        let mut accum3 = 0f32;
        let mut accum4 = 0f32;

        for iter in (0..shapes.len()).step_by(4) {
            accum1 += shapes[iter].area();
            accum2 += shapes[iter + 1].area();
            accum3 += shapes[iter + 2].area();
            accum4 += shapes[iter + 3].area();
        }

        accum1 + accum2 + accum3 + accum4
    });
}
