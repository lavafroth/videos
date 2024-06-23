#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c3 = """#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[source]
        io: std::io::Error,
        #[from]
        #[source]
        parse: std::string::ParseError,
    },
    // ...
}"""
        c3 = (
            Code(code=c3, language="rust", insert_line_no=False, font_size=38)[2]
            .to_edge(LEFT)
            .set_opacity(0.5)
        )

        c4 = """#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[source]
        io: std::io::Error,
        #[from]
        parse: std::string::ParseError,
    },
    // ...
}"""
        c4 = (
            Code(code=c4, language="rust", insert_line_no=False, font_size=38)[2]
            .to_edge(LEFT)
            .set_opacity(0.5)
        )

        for line in (c3[5], c3[7]):
            line.set(color=RED)
            line.set_opacity(1)
        c3[6].set(color=RED)

        for line in (c4[5], c4[6]):
            line.set(color=RED)
            line.set_opacity(1)

        ferris = SVGMobject("../assets/rustacean-flat-gesture-down").scale(0.8).shift(5 * RIGHT)
        self.add(ferris, c3)

        self.play(
            FadeOut(c3[6]),
            ReplacementTransform(c3[:6], c4[:6]),
            ReplacementTransform(c3[-4:], c4[-4:]),
        )
        
        lines = c4[5:7]
        curve = ParametricFunction(
            lambda t: np.array([0.1 * np.sin(PI * t), 0, 0]), t_range=[0, 4]
        ).move_to(lines.get_center())
        self.play(MoveAlongPath(lines, curve))
        line = Line(8 * LEFT, 8 * RIGHT).shift(8 * DOWN)
        c5 = c4.copy().move_to(ORIGIN)
        self.play(
            ferris.animate.shift(8 * RIGHT),
            line.animate.shift(7 * UP),
            c4.animate.scale(0.8).shift(UP).to_edge(UL),
        )
        t = Text(
            """error: #[from] is only supported on the source field, not any other field
 --> src/main.rs:6:9
  |
6 |         #[from]
  |         ^^^^^^^

error: could not compile `demo` (bin "demo") due to 1 previous error
""",
            font=codefont,
            font_size=24,
            t2c={"error:": RED},
        ).to_edge(DOWN).shift(.2 * DOWN)
        self.play(Write(t))
        self.wait(4)
        self.play(Group(t, line).animate.shift(DOWN * 8), Transform(c4, c5))
