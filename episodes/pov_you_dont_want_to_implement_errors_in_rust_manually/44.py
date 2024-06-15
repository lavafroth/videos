#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        code = """#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[error("failed to read config")]
        source: std::io::Error,
    },
    // ...
}"""
        code = Code(code=code, language="rust", insert_line_no=False, font_size=38)[2]
        ripple = code[0][9:14]
        anims = []
        curve = ParametricFunction(
            lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]
        )
        for char in ripple:
            curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))

        self.add(code)
        self.play(AnimationGroup(anims, lag_ratio=0.1))

        target = code[4][8:]
        vb = RoundedRectangle(width=code[0][0].width * (1.28 * len(target)), height=target.height + .1, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05).move_to(target.get_center()).set_z_index(0)

        target_ = code[4][8:14]
        vb_ = RoundedRectangle(width=code[0][0].width * (1.3 * len(target_)), height=target.height + .1, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05).move_to(target_.get_center()).set_z_index(0)
        self.play(Create(vb))
        self.play(Transform(vb, vb_))

        code_1 = """#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[error("failed to read config")]
        #[source]
        source: std::io::Error,
    },
    // ...
}"""
        code_1 = Code(code=code_1, language="rust", insert_line_no=False, font_size=38)[2]
        code_1[4].set(color=BLUE).set_opacity(0.5)
        code_2 = code.copy()
        self.play(
            Transform(code[:4], code_1[:4]),
            Transform(code[-4:], code_1[-4:]),
            Transform(vb, code_1[4][8:]),
        )
        self.wait(2)
        self.play(
            Transform(code[:4], code_2[:4]),
            Transform(code[-4:], code_2[-4:]),
            FadeOut(vb)
        )
        self.wait(1)
        code_3 = '''fn main() {
    if let Err(e) = fs::read_to_string("nonexistent") {
        let error = MyError::Io { source: e };
        println!("{:#?}", error.source());
    }
}
'''
        code_3 = Code(code=code_3, language="rust", insert_line_no=False, font_size=38)[2].shift(8 * DOWN)
        self.play(code.animate.shift(8 * UP), code_3.animate.shift(8 * UP))
        self.wait(2)
