#!/usr/bin/env python
# coding: utf-8

from manim import *
from hackermanim import *

class Convinced(Scene):
    def construct(self):
        code = Code(code='Box<dyn std::error::Error>', language='rust', font_size=34)[2][0].shift(2.5*RIGHT)
        heap_label = Text("The heap").to_edge(UR).shift(0.75 * LEFT)
        heapspace = Rectangle(width=8, height=10, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.5).to_edge(RIGHT).shift(3.25 * RIGHT)
        heap_blocks = Rectangle(width=4, height=2, grid_ystep=1.0, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(DR)
        heap = Group(heapspace, heap_blocks, heap_label)
        anims = AnimationGroup(
            FadeIn(heap),
            code.animate.shift(5.5 * LEFT),
        )
        self.play(anims)
        self.wait(2)

        _data = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(RIGHT)
        data = code[len('Box<dyn '):]
        table = code[:len('Box<dyn ')]
        _table = Rectangle(width=4, height=3, color=YELLOW, fill_color=YELLOW, fill_opacity=0.3, grid_ystep=3/4).to_edge(DL)
        pointer = Circle(radius=0.1, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(code.get_center() + 0.25 * RIGHT).set_opacity(0)
        _pointer = Circle(radius=0.25, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(code.get_center() + 0.25 *RIGHT)
        text = Text("destructor\nsize\nalign", font='monospace', font_size=34, line_spacing=1.1).move_to(_table.get_edge_center(UP) + 1.15 *DOWN)
        fmt = Text("fmt", font='monospace', font_size=34).move_to(_table.get_edge_center(DOWN) + 0.35 * UP + 1 * LEFT)
        arrow_end = _data.get_edge_center(LEFT) + .5 * RIGHT
        arrow = Arrow(start=code.get_center(), end=arrow_end)
        arrow_1 = Arrow(start=_pointer.get_center(), end=_table.get_edge_center(UP) + .1 * DOWN)
        self.play(AnimationGroup(
            Transform(table, _table),
            Transform(data, _data),
            Transform(pointer, _pointer),
            Write(text),
            Create(arrow),
            Create(arrow_1),
        ))
        self.play(Write(fmt))
        self.wait(2)
        _text = Text("...", font='monospace', font_size=34, line_spacing=1.1).move_to(table.get_edge_center(UP) + 0.35 *DOWN)
        _table = Rectangle(width=4, height=3/2, color=YELLOW, fill_color=YELLOW, fill_opacity=0.3, grid_ystep=3/4).to_edge(DL).shift(UP * 3/2)
        _fmt = Text("fmt", font='monospace', font_size=34).move_to(_table.get_edge_center(DOWN) + 0.35 * UP)
        self.play(AnimationGroup(
            Transform(text, _text),
            Transform(table, _table),
            Transform(fmt, _fmt),
            Transform(arrow_1, arrow_1),
        ))
        self.wait(2)
        vtable = Group(table, fmt, text)
        _vtable = vtable.copy().shift(3.5 * RIGHT + 1.5 * DOWN)
        _pointer = Rectangle(width=2, height=3/2, color=BLUE, fill_color=BLUE, fill_opacity=0.3, grid_ystep=3/4).move_to(pointer.get_center())
        _arrow_1 = Arrow(start=_pointer.get_center() + 0.5 * DOWN, end=_vtable.get_edge_center(UP) + .2 * DOWN)
        _arrow = Arrow(start=_pointer.get_center() + 0.2 * UP + 0.6 * RIGHT, end=arrow_end)
        trait_object = Text("data\nvtable", font='monospace', font_size=34, line_spacing=1.1).move_to(_pointer.get_center())
        self.play(AnimationGroup(
            Transform(vtable, _vtable),
            AnimationGroup(
                Transform(pointer, _pointer),
                Write(trait_object),
                lag_ratio=0.7,
            ),
            Transform(arrow_1, _arrow_1),
            Transform(arrow, _arrow),
        ))
        trait_object = Group(trait_object, pointer)
        machine_code = Text("machine\ncode", font='monospace', font_size=34).to_edge(DL)
        arrow_2 = Arrow(start=fmt.get_center() + 0.5 * LEFT, end=fmt.get_center() + 3.5 * LEFT)
        self.play(AnimationGroup(
            Write(machine_code),
            Create(arrow_2),
        ))
        
        self.wait(2)
        _vtable = vtable.copy()
        dispatch = Text("dynamic\ndispatch\ntable", font='monospace', font_size=34, color=YELLOW).move_to(vtable.get_center() + 0.6 * RIGHT)
        self.play(Transform(vtable, dispatch))
        self.wait(3)
        self.play(Transform(vtable, _vtable))
        self.play(ripple(fmt), run_time=1)
        
        self.wait(2)
        self.play(ripple(machine_code), run_time=1)
        self.wait(2)
        self.play(AnimationGroup(
            [FadeOut(x) for x in (
                vtable, arrow_2, arrow_1, arrow, data, heap, machine_code, text,
            )] + [trait_object.animate.move_to(ORIGIN)]
        ))
        self.wait(3)
        dyn = Code(code='dyn', language='rust', font_size=34)[2][0].shift(1.5 * DOWN + 0.25 * LEFT)
        dyn_ref = Code(code='&dyn std::error::Error', language='rust', font_size=34)[2][0].shift(1.5 * DOWN + 0.25 * LEFT)
        dyn_box = Code(code='Box<dyn std::error::Error>', language='rust', font_size=34)[2][0].shift(1.5 * DOWN +  0.25 * LEFT)
        self.play(Write(dyn))
        self.wait(2)
        l, o, r = dyn_ref[:1], dyn_ref[1:4], dyn_ref[4:]
        self.play(AnimationGroup(
            Write(l),
            Transform(dyn, o),
            Write(r),
        ))
        self.wait(2)
        L, O, R = dyn_box[:4], dyn_box[4:7], dyn_box[7:]
        self.play(AnimationGroup(
            Transform(l, L),
            Transform(dyn, O),
            Transform(r, R),
        ))
        self.wait(2)
        dyn = Group(l, dyn, r)
        text = Text("Trait object", font_size=34).shift(1.5 * DOWN)
        self.play(Transform(dyn, text))
        self.wait(4)
        c = Circle(radius=1.5, color=WHITE, fill_color=WHITE, fill_opacity=.5)
        circle = Circle(radius=0.3, color=WHITE).shift(0.3 * UL)
        num_points = 20
        angles = [n * (360 / num_points) for n in range(num_points)]
        points = [circle.point_at_angle(n*DEGREES) for n in angles]
        dots = [Circle(radius=0.01, color=WHITE, fill_opacity=1).move_to(p) for p in points]
        # Add the circle to the scene
        self.play(
            AnimationGroup(
                Transform(trait_object, c),
                FadeOut(dyn),
                AnimationGroup(Create(dot) for dot in dots),
            )
        )
        self.wait(1)
