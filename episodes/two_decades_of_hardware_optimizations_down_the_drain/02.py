#!/usr/bin/env manim
from manim import *
class Sc(Scene):
    def construct(self):
        with register_font("Poppins-Light.ttf"):
            Text.set_default(font="Poppins")
        cleancode = Text('Clean code').to_edge(UP).shift(3.5 * RIGHT)
        self.add(cleancode)
        name = Text('Robert C. Martin').scale(.5).to_edge(DL).shift(UP + 2 * RIGHT)
        aka = Text('AKA "Uncle Bob"').scale(.5).to_edge(DL).shift(0.5 * UP + 2 * RIGHT)
        self.play(Write(name))
        self.play(Write(aka))
        _layer = Square(fill_color=PURPLE, color=PURPLE, fill_opacity=0.8).rotate(PI/4).apply_function(lambda p: np.array([
                   p[0],
                   .5 * p[1],
                   p[2]
                ])).shift(4 * RIGHT + 2.5 * DOWN)
        layer = _layer.copy().set_opacity(0).shift(0.5 * UP)
        _text = Text("function", font_size=22).move_to(_layer.get_edge_center(LEFT) + LEFT)
        text = _text.copy().set_opacity(0).shift(0.5 * UP)
        self.play(Transform(layer, _layer),
                Transform(text, _text))

        layers = [Group(layer, text)]
        for color, text in (
            (BLUE, "class"),
            (TEAL_D, "inheritance"),
            (GREEN_A, "interface"),
            (TEAL_A, "mixin"),
        ):

            _layer = layer.copy().shift(UP).set(fill_color=color, color=color)
            layer = _layer.copy().shift(0.5 * UP).set_opacity(0)
            _text = Text(text, font_size=22).move_to(_layer.get_edge_center(LEFT) + LEFT)
            text = _text.copy().set_opacity(0).shift(0.5 * UP)
            self.play(Transform(layer, _layer),
                    Transform(text, _text))
            layers.append(Group(layer, text))

        for attr in ('"readable"', '"understandable"', '"maintainable"'):
            self.play(Transform(cleancode, Text(attr).move_to(cleancode)))
            self.wait(2)

        self.play((FadeOut(x) for x in layers), FadeOut(cleancode), FadeOut(name), FadeOut(aka))
