#!/usr/bin/env manim
from manim import *
from hackermanim import *


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Mono"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont)
        p = MonoText("__pycache__")
        self.play(Write(p))
        tree = """.
├── 01.py
├── 02.py
├── 03.py
├── 04.py
└── __pycache__"""
        tree_expanded = """.
├── 01.py
├── 02.py
├── 03.py
├── 04.py
└── __pycache__
    ├── 01.cpython-311.pyc
    ├── 02.cpython-311.pyc
    ├── 03.cpython-311.pyc
    └── 04.cpython-311.pyc
"""
        tree = MonoParagraph(tree)
        tree_expanded = MonoParagraph(tree_expanded)

        header = Text("Project Tree").to_edge(UP)
        self.play(
            ReplacementTransform(p, tree[5][3:]),
            FadeIn(tree[:5], tree[5][:3]),
            FadeIn(header),
        )
        trailer = tree_expanded[6:]
        self.wait(2)
        self.play(
            AnimationGroup(
                ReplacementTransform(tree[:6], tree_expanded[:6]),
                Write(trailer),
                lag_ratio=0.5,
            )
        )
        dotpyc = VGroup()
        for line in trailer:
            dotpyc.add(line[-4:])

        line = trailer[0]
        rect = RoundedRectangle(
            width=line[-4:].width + 0.2,
            height=line.height * 4,
            corner_radius=0.2,
            color=BLUE,
        ).move_to(dotpyc.get_center())
        self.play(Create(rect))
        self.play(FadeOut(rect))
        self.wait(4)
