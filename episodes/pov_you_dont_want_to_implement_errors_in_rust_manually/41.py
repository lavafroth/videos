#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        c1 = '''#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[source]
        io: std::io::Error,
        #[source]
        parse: std::string::ParseError,
    },
    // ...
}'''
        c1 = Code(code=c1, language='rust', insert_line_no=False, font_size=38)[2]
        self.add(c1)
        self.play(c1.animate.to_edge(LEFT))
        gz = (c1[:3], c1[5:])

        ferris = SVGMobject('rustacean-flat-gesture').scale(.8).shift(5 * RIGHT).shift(8 * RIGHT)
        ferris_gesture_down = SVGMobject('rustacean-flat-gesture-down').scale(.8).shift(5 * RIGHT)

        self.play(
            (x.animate.set_opacity(0.5) for x in gz),
            ferris.animate.shift(8 * LEFT)
        )
        self.wait(1)
        self.play(
            c1[3:5].animate.set_opacity(.5),
            c1[5:7].animate.set_opacity(1),
            Transform(ferris, ferris_gesture_down),
        )
        err = c1[5:7]
        self.play(err.animate.set(color=RED))
        c2 = '''#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[source]
        io: std::io::Error,
        #[from]
        parse: std::string::ParseError,
    },
    // ...
}'''
        c2 = Code(code=c2, language='rust', insert_line_no=False, font_size=38)[2].to_edge(LEFT).set(color=RED)
        c3 = '''#[derive(Error, Debug)]
pub enum MyError {
    Io{
        #[source]
        io: std::io::Error,
        #[from]
        #[source]
        parse: std::string::ParseError,
    },
    // ...
}'''
        c3 = Code(code=c3, language='rust', insert_line_no=False, font_size=38)[2].to_edge(LEFT).set_opacity(0.5)
        c3[5:8].set(color=RED).set_opacity(1)
        c3[6].set_opacity(.5)
        chunks3 = lambda obj, x, y: (obj[:x], obj[x:y], obj[y:])
        e_1 = chunks3(err[0], 10, -1)
        e_2 = chunks3(c2[5], 10, -1)
        self.play(Transform(a, b) for a, b in zip(e_1, e_2))

        self.play(
            Transform(c1[:5], c3[:5]),
            TransformMatchingShapes(Group(*e_1), c3[5]),
            Write(c3[6]),
            Transform(c1[-4:], c3[-4:]),
        )

        i = Text('implicit', font_size=32).shift(2 * DOWN + 3 * RIGHT)
        r = CurvedArrow(i.get_edge_center(LEFT) + .1 * LEFT, c3[6].get_edge_center(RIGHT) + .1 * RIGHT + .1 * DOWN, angle=PI/4)
        self.play(Write(i), Create(r))
        self.wait(2)
        self.play(FadeOut(i, r))

        # curve = ParametricFunction(lambda t: np.array([0.1 * np.sin(PI * t), 0, 0]), t_range=[0, 4]).move_to(err.get_center())
        # self.play(
        #     MoveAlongPath(Group(*e_1, c3[6]), curve)
        # )
        self.wait(2)
