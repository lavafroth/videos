#!/usr/bin/env manim

from manim import *
from manim import VGroup as V, Transform as T
from hackermanim import *


def stackvar(color, opacity=0.5):
    return RoundedRectangle(
        width=4,
        height=1,
        color=color,
        fill_color=color,
        fill_opacity=opacity,
        corner_radius=0.05,
    ).set_z_index(-1)

def chunks3(obj, x, y):
    return (obj[:x], obj[x:y], obj[y:])

class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        # be very consistent with color coding things
        # I swear this will become my selling point at some point.
        turbo = Text(">>>", color=GRAY, font=codefont, font_size=40)
        t = Text("'/'.join(('foo', 'bar', 'baz'))", t2c={
                     "'/'": ORANGE,
                     'join': PURPLE,
                     "'foo'": ORANGE,
                     "'baz'": ORANGE,
                     "'bar'": ORANGE,
                 },
                 font=codefont,
                 font_size=40,
        )
        o = Text("'foo/bar/baz'", color=GRAY, font=codefont, font_size=40)
        line0 = V(turbo, t).arrange()
        V(line0, o).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(turbo))
        self.play(Write(t))
        pairs = [
            (t[11:14], o[1:4]),
            (t[17:20], o[5:8]),
            (t[23:26], o[9:-1]),
        ]
        slash = t[1]
        self.play(
            Write(o[0]),
            Write(o[-1])
        )
        self.play(
            AnimationGroup(
                (AnimationGroup(Transform(a.copy(), b)) for a, b in pairs),
                lag_ratio=.5
            ),
        )
        self.play(
            AnimationGroup(
            Transform(slash.copy(), o[4]),
            Transform(slash.copy(), o[8]),
            lag_ratio=.5
            ),
        )
        self.wait(3)
