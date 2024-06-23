#!/usr/bin/env python
# coding: utf-8

from manim import *

class Convinced(Scene):
    def construct(self):
        ferris_thinking = SVGMobject('../assets/rustacean-flat-gesture.svg').shift(3 * LEFT)
        reject = SVGMobject('1faf8.svg').scale(0.5).shift(0.5 * RIGHT)
        _reject = reject.copy().set_opacity(0).shift(0.5 * LEFT)
        code = Code(code='struct', language='rust', font_size=40)[2][0].shift(3*RIGHT)
        self.play(AnimationGroup(
            FadeIn(ferris_thinking),
            Write(code),
        ))
        self.play(Transform(_reject, reject))
        self.wait(2)
        self.play(FadeOut(_reject, code))
        _reject = SVGMobject('261d.svg').scale(0.5).shift(2 * LEFT).rotate(PI, axis=np.array([0, 1, 0])).rotate(-0.2*PI)
        reject = _reject.copy().set_opacity(0).shift(0.5 * LEFT)
        code = Code(code='&dyn std::error::Error', language='rust', font_size=40)[2][0].shift(2.5*RIGHT)
        self.play(AnimationGroup(
            ferris_thinking.animate.shift(2*LEFT),
            Transform(reject, _reject),
            Write(code),
        ))
        self.wait(2)

        heap_label = Text("The heap").to_edge(UR).shift(0.75 * LEFT)
        heapspace = Rectangle(width=8, height=10, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.5).to_edge(RIGHT).shift(3.25 * RIGHT)
        heap_blocks = Rectangle(width=4, height=2, grid_ystep=1.0, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(DR)
        heap = Group(heapspace, heap_blocks, heap_label)
        anims = AnimationGroup(
            FadeIn(heap),
            FadeOut(reject),
            code.animate.shift(5.5 * LEFT),
            FadeOut(ferris_thinking),
        )
        self.play(anims)
        self.wait(2)

        heap_block = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(RIGHT)
        pointer = Circle(radius=0.1, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(code.get_center() + 0.25 * RIGHT).set_opacity(0)
        _pointer = Circle(radius=0.25, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(code.get_center() + 0.25 *RIGHT)
        address = Text("address: 0xcafec0c0", font='monospace', font_size=20).move_to(_pointer.get_edge_center(DOWN) + 0.25 * DOWN)
        arrow_end = heap_block.get_edge_center(LEFT) + .5 * RIGHT
        arrow = Arrow(start=code.get_center(), end=arrow_end)
        self.play(
            Transform(code, heap_block),
            Transform(pointer, _pointer),
            Create(arrow),
            Write(address),
        )
        self.wait(2)

        for displacement in (2 * UL, 4 * DOWN, 3 * RIGHT + UP):
            _pointer = pointer.copy().shift(displacement)
            _address = Text("address: 0xcafec0c0", font='monospace', font_size=20).move_to(_pointer.get_edge_center(DOWN) + 0.25 * DOWN)
            _arrow = Arrow(start=_pointer.get_center() + 0.25 * LEFT, end=arrow_end)
            self.play(
                Transform(pointer, _pointer),
                Transform(arrow, _arrow),
                Transform(address, _address),
            )
        self.wait(2)
        self.play(
            FadeOut(pointer),
            FadeOut(address),
            FadeOut(arrow),
            FadeOut(heap),
            FadeOut(code),
        )
        self.wait(2)
