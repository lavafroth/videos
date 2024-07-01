#!/usr/bin/env python
# coding: utf-8

from manim import *
from hackermanim import *

class Convinced(Scene):
    def construct(self):
        code = Code(code='Box<dyn std::error::Error>', language='rust', font_size=40)[2][0]
        _code = Code(code='Box<dyn std::error::Error>', language='rust', font_size=34)[2][0].shift(3*LEFT)
        self.play(Transform(code, _code))
        heap_label = Text("The heap").to_edge(UR).shift(0.75 * LEFT)
        heapspace = Rectangle(width=8, height=10, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.5).to_edge(RIGHT).shift(3.25 * RIGHT)
        heap_blocks = Rectangle(width=4, height=2, grid_ystep=1.0, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(DR)
        heap = Group(heapspace, heap_blocks, heap_label)
        self.play(FadeIn(heap))
        self.wait(2)

        _data = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(RIGHT)
        data = code[len('Box<dyn '):]
        table = code[:len('Box<dyn ')]
        pointer = Circle(radius=0.1, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(code.get_center() + 0.25 * RIGHT).set_opacity(0)
        _pointer = Rectangle(width=2, height=3/2, color=BLUE, fill_color=BLUE, fill_opacity=0.3, grid_ystep=3/4).move_to(pointer.get_center())
        arrow_end = _data.get_edge_center(LEFT) + .5 * RIGHT
        _table = Rectangle(width=4, height=3/2, color=YELLOW, fill_color=YELLOW, fill_opacity=0.3, grid_ystep=3/4).to_edge(DL).shift(4 * RIGHT)
        _arrow_1 = Arrow(start=_pointer.get_center() + 0.5 * DOWN, end=_table.get_edge_center(UP) + .2 * DOWN)
        _arrow = Arrow(start=_pointer.get_center() + 0.2 * UP + 0.6 * RIGHT, end=arrow_end)
        trait_object = Text("data\nvtable", font='monospace', font_size=34, line_spacing=1.1).move_to(_pointer.get_center())
        text = Text("...\nfmt", font='monospace', font_size=34, line_spacing=1.4).move_to(_table.get_center() + 0.1 * DOWN)
        self.play(
            Transform(table, _table),
            Transform(data, _data),
            Transform(pointer, _pointer),
            Write(text),
            Create(_arrow),
            Create(_arrow_1),
            AnimationGroup(
                Transform(pointer, _pointer),
                Write(trait_object),
                lag_ratio=0.7,
            ),
        )
        self.wait(2)
        
        self.play(ripple(trait_object[:4]), run_time=1)
        
        data_c = data.copy()
        self.play(Transform(data, Rectangle(width=1, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(
            heapspace.get_edge_center(LEFT) + 1.25 * RIGHT
        )))
        self.play(Transform(data, Rectangle(width=2, height=3, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(
            heapspace.get_edge_center(LEFT) + 1.75 * RIGHT
        )))
        self.play(Transform(data, data_c))
        self.wait(2)

        self.play(ripple(text[3:]), run_time=1)
    
        machine_code = Text("machine\ncode", font='monospace', font_size=34).to_edge(DL)
        arrow_2 = Arrow(start=text.get_center() + 0.5 * LEFT + 0.2 * DOWN, end=text.get_center() + 4 * LEFT + 0.2 * DOWN)
        self.play(AnimationGroup(
            Write(machine_code),
            Create(arrow_2),
        ))
        self.wait(4)
        self.play(FadeOut(machine_code, arrow_2, data, text, _arrow, _arrow_1, table, pointer, trait_object, heap))
        self.wait(1)
