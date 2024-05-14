#!/usr/bin/env python
# coding: utf-8

from manim import *

def rustcode(code, *args, **kwargs):
    return Code(code=code, language='rust', font_size=50)[2]

def blue(code):
    return Text(code, font_size=50, font='monospace', color=BLUE)

class Primitive(Scene):
    def construct(self):
        text = blue('u8')
        self.play(Write(text))
        self.play(Transform(text, blue('bool')))
        self.play(Transform(text,  blue('f64')))
        self.play(Transform(text, blue('i64')))
        self.wait(2)
        rect = Rectangle(width=4.0, height=8.0, grid_ystep=1.0, color=BLUE).to_edge(LEFT).shift(9 * DOWN)
        _rect = Rectangle(width=4.0, height=8.0, grid_ystep=1.0, color=BLUE).to_edge(LEFT).shift(2.5 * DOWN)
        stack_label = Text("The stack").move_to(_rect.get_center()+5.75 * UP)
        self.play(AnimationGroup(
            Transform(rect, _rect),
            Write(stack_label),
        ))
        stack = Group(stack_label, rect)
        push = Rectangle(width=4.0, height=1.0, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(text.get_center() + 2 * UP)
        self.play(Transform(text, push))
        _push = Rectangle(width=4.0, height=1.0, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(rect.get_center() + 4.5 * UP)
        self.play(Transform(text, _push))
        push = text
        self.wait(2)

        vec = rustcode('String').shift(0.75 * LEFT)
        _vec = rustcode('Vec<u8>').shift(0.75 * LEFT)
        self.play(Write(vec))
        self.play(Transform(vec, _vec))
        heap_block = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(vec.get_center())
        self.play(Transform(vec, heap_block))
        heap_block = Rectangle(width=1, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(vec.get_center())
        self.play(Transform(vec, heap_block))
        heap_block = Rectangle(width=2, height=3, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(vec.get_center())
        self.play(Transform(vec, heap_block))
        heap_block = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(vec.get_center())
        self.play(Transform(vec, heap_block))
        

        heap_label = Text("The heap").to_edge(UR).shift(0.75 * LEFT)
        heapspace = Rectangle(width=8, height=10, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.5).to_edge(RIGHT).shift(3.25 * RIGHT)
        self.play(AnimationGroup(
            Create(heapspace),
            Write(heap_label),
        ))
        

        heap_block = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(RIGHT).shift(.2 * LEFT)
        pointer = Circle(radius=0.1, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(vec.get_center() + 0.25 * RIGHT).set_opacity(0)
        _pointer = Circle(radius=0.25, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(vec.get_center() + 0.25 *RIGHT)
        address = Text("address: 0xcafebabe", font='monospace', font_size=20).move_to(_pointer.get_edge_center(DOWN) + 0.25 * DOWN)
        arrow_end = heap_block.get_edge_center(LEFT) + .5 * RIGHT
        arrow = Arrow(start=vec.get_center(), end=arrow_end)
        self.play(AnimationGroup(
            Transform(vec, heap_block),
            Transform(pointer, _pointer),
            Create(arrow),
            Write(address),
        ))

        _push = Rectangle(width=4.0, height=1.0, color=BLUE, fill_color=BLUE, fill_opacity=0).move_to(rect.get_center() + 3.5 * UP)
        self.play(AnimationGroup(
            Transform(push, _push),
            rect.animate.shift(DOWN)
        ))
        rect = Group(rect, push)
        
        push = Rectangle(width=4.0, height=1.0, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(rect.get_center() + 5 * UP)
        _address = Text("0xcafebabe", font='monospace', font_size=20).move_to(push.get_center())
        _arrow = Arrow(start=push.get_center() + 0.25 * DOWN, end=arrow_end)
        self.play(AnimationGroup(
            Transform(pointer, push),
            Transform(arrow, _arrow),
            Transform(address, _address)
        ))
        self.wait(2)

        pointer = Group(pointer, address)
        _pointer = pointer.copy().shift(5 * DOWN)
        _arrow = Arrow(start=_pointer.get_center() + RIGHT, end=arrow_end + 3 * DOWN)
        self.play(AnimationGroup(
            vec.animate.shift(3 * DOWN),
            rect.animate.shift(5 * DOWN),
            Transform(pointer, _pointer),
            Transform(arrow, _arrow),
        ))
        
        text = rustcode("Box<u8>")[0].shift(LEFT)
        u8 = text[4:6]
        self.play(Write(u8))
        _a = text[:4]
        a = text[:4].copy().set_opacity(0).shift(0.2 * UP)
        _b = text[6:]
        b = text[6:].copy().set_opacity(0).shift(0.2 * UP)
        self.play(AnimationGroup(
            Transform(a, _a),
            Transform(b, _b),
        ))
        text = Group(u8, a, b)
        heap_block = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(RIGHT).shift(.2 * LEFT)
        pointer = Circle(radius=0.1, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(text.get_center() + 0.25 * RIGHT).set_opacity(0)
        _pointer = Circle(radius=0.25, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(text.get_center() + 0.25 *RIGHT)
        address = Text("address: 0xcafebd60", font='monospace', font_size=20).move_to(_pointer.get_edge_center(DOWN) + 0.25 * DOWN)
        arrow_end = heap_block.get_edge_center(LEFT) + .5 * RIGHT
        arrow = Arrow(start=text.get_center(), end=arrow_end)
        self.play(AnimationGroup(
            Transform(text, heap_block),
            Transform(pointer, _pointer),
            Create(arrow),
            Write(address),
        ))
        push = Rectangle(width=4.0, height=1.0, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(rect.get_center() + 6 * UP)
        _address = Text("0xcafebd60", font='monospace', font_size=20).move_to(push.get_center())
        _arrow = Arrow(start=push.get_center() + 0.25 * DOWN + RIGHT, end=arrow_end)
        self.play(AnimationGroup(
            Transform(pointer, push),
            Transform(arrow, _arrow),
            Transform(address, _address)
        ))
        _arrow = Arrow(start=push.get_center() + RIGHT, end=arrow_end + 2 * DOWN)
        self.play(AnimationGroup(
            text.animate.shift(2 * DOWN),
            Transform(arrow, _arrow),
        ))
        self.wait(4)
