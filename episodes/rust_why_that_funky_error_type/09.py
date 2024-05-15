#!/usr/bin/env python
# coding: utf-8
from manim import *

class Problem(Scene):
    def construct(self):
        ferris = SVGMobject('rustacean-flat-gesture.svg').scale(0.5).to_edge(LEFT)
        header_sep = Line(start=4.6 * LEFT, end=10*RIGHT)
        sep = Line(start=10 * UP, end=10*DOWN).to_edge(LEFT).shift(2 * RIGHT)
        self.play(AnimationGroup(
            FadeIn(ferris),
            Create(header_sep),
            Create(sep),
        ))
        net = Code(code='TcpConnError', language='rust', font_size=30)[2][0].to_edge(UP).shift(2.5 * LEFT + DOWN)
        log = Code(code='LoggingError', language='rust', font_size=30)[2][0].to_edge(DOWN).shift(2.5 * LEFT + UP)
        net_impl = """fn fmt(&self, f: &mut std::fmt::Formatter<'_>)
-> std::fmt::Result {
    write!(f,
    "connection dropped by peer: {}",
    self.peer_address()
    )
}"""
        log_impl = """fn fmt(&self, f: &mut std::fmt::Formatter<'_>)
-> std::fmt::Result {
    write!(f,
    "could not open file: {}",
    self.log_destination.display()
    )
}"""
        net_impl = Code(code=net_impl, language='rust', font_size=20)[2].to_edge(UP).shift(3 * RIGHT + 0.5 * DOWN)
        log_impl = Code(code=log_impl, language='rust', font_size=20)[2].to_edge(DOWN).shift(3 * RIGHT + 0.5 * UP)
        self.play(AnimationGroup(
            Write(net),
            Write(net_impl),
            Write(log),
            Write(log_impl)
        ))
        self.wait(2)
        anims = []
        for char in net:
            curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]).move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=1)
        self.wait(2)
        anims = []
        for char in log:
            curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]).move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=1)
        self.wait(4)
        self.play(AnimationGroup([FadeOut(x) for x in (net, log, net_impl, log_impl, header_sep, sep)]))
        _ferris = SVGMobject('rustacean-flat-gesture.svg')
        qs = []
        for x in range(3):
            phaser = np.sin(x/3 * PI)
            q = Text('?').rotate(x * PI * -0.2).shift(x * 0.3 * phaser * DR ).shift(UP + RIGHT)
            qs.append(q)
        self.play(Transform(ferris, _ferris))
        self.play(Write(q) for q in qs)
        self.wait(4)
        self.play(FadeOut(*qs, ferris))
        self.wait(4)
