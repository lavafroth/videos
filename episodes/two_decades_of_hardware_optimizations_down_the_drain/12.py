#!/usr/bin/env manim
# coding: utf-8
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style='monokai')
        code = Code(code='Vec<Box<dyn Shape>>', language='rust', font_size=34)[2][0].shift(3*LEFT)
        self.add(code)
        heap_label = Text("The heap").to_edge(UR).shift(0.75 * LEFT)
        heapspace = Rectangle(width=8, height=10, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.5).to_edge(RIGHT).shift(3.25 * RIGHT)
        heap_blocks = Rectangle(width=4, height=2, grid_ystep=1.0, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(DR)
        heap = Group(heapspace, heap_blocks, heap_label)
        anims = AnimationGroup(
            FadeIn(heap),
        )
        self.play(anims)

        _data = Rectangle(width=4, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).to_edge(RIGHT)
        space_index = 'Vec<Box<dyn Shape>>'.find(' ')
        data = code[space_index:]
        table = code[:space_index]
        _table = Rectangle(width=4, height=3, color=YELLOW, fill_color=YELLOW, fill_opacity=0.3, grid_ystep=3/4).to_edge(DL)
        pointer = Circle(radius=0.1, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(code.get_center() + 0.25 * RIGHT).set_opacity(0)
        _pointer = Circle(radius=0.25, color=BLUE, fill_color=BLUE, fill_opacity=0.8).move_to(code.get_center() + 0.25 *RIGHT)
        text = Text("destructor\nsize\nalign", font='Terminess Nerd Font Propo', font_size=34, line_spacing=1.1).move_to(_table.get_edge_center(UP) + 1.15 *DOWN)
        fmt = Text("area", font='Terminess Nerd Font Propo', font_size=34).move_to(_table.get_edge_center(DOWN) + 0.35 * UP + 0.75 * LEFT)
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
        self.wait(1)
        _text = Text("...", font='Terminess Nerd Font Propo', font_size=34, line_spacing=1.1).move_to(table.get_edge_center(UP) + 0.35 *DOWN)
        _table = Rectangle(width=4, height=3/2, color=YELLOW, fill_color=YELLOW, fill_opacity=0.3, grid_ystep=3/4).to_edge(DL).shift(UP * 3/2)
        _fmt = Text("area", font='Terminess Nerd Font Propo', font_size=34).move_to(_table.get_edge_center(DOWN) + 0.35 * UP)
        self.play(AnimationGroup(
            Transform(text, _text),
            Transform(table, _table),
            Transform(fmt, _fmt),
            Transform(arrow_1, arrow_1),
        ))
        vtable = Group(table, fmt, text)
        _vtable = vtable.copy().shift(3.5 * RIGHT + 1.5 * DOWN)
        _pointer = Rectangle(width=2, height=3/2, color=BLUE, fill_color=BLUE, fill_opacity=0.3, grid_ystep=3/4).move_to(pointer.get_center())
        _arrow_1 = Arrow(start=_pointer.get_center() + 0.5 * DOWN, end=_vtable.get_edge_center(UP) + .2 * DOWN)
        _arrow = Arrow(start=_pointer.get_center() + 0.2 * UP + 0.6 * RIGHT, end=arrow_end)
        trait_object = Text("data\nvtable", font='Terminess Nerd Font Propo', font_size=34, line_spacing=1.1).move_to(_pointer.get_center())

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

        self.play(ripple(trait_object[:4]), run_time=1)

        # resize the box now
        data_c = data.copy()
        self.play(Transform(data, Rectangle(width=1, height=1, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(
            heapspace.get_edge_center(LEFT) + 1.25 * RIGHT
        )))
        self.play(Transform(data, Rectangle(width=2, height=3, color=TEAL_D, fill_color=TEAL_D, fill_opacity=0.3).move_to(
            heapspace.get_edge_center(LEFT) + 1.75 * RIGHT
        )))
        self.play(Transform(data, data_c))
        self.wait(1)

        
        trait_object_group = Group(trait_object, pointer)
        machine_code = Text("machine\ncode", font='Terminess Nerd Font Propo', font_size=34).to_edge(DL)
        arrow_2 = Arrow(start=fmt.get_center() + 0.5 * LEFT, end=fmt.get_center() + 3.5 * LEFT)
        self.play(AnimationGroup(
            Write(machine_code),
            Create(arrow_2),
        ))
        
        _vtable = vtable.copy()
        dispatch = Text("dynamic\ndispatch\ntable", font='Terminess Nerd Font Propo', font_size=34, color=YELLOW).move_to(vtable.get_center() + 0.6 * RIGHT)
        self.play(Transform(vtable, dispatch))
        self.wait(2)
        self.play(Transform(vtable, _vtable))

        self.wait(8)
        self.play(ripple(trait_object[4:]), run_time=1)

        curve = ParametricFunction(lambda t: np.array([0.1 * np.sin(PI * t), 0, 0]), t_range=[0, 2]).move_to(arrow_1.get_center())
        self.play(MoveAlongPath(arrow_1, curve), run_time=1)
        self.wait(1)

        self.play(ripple(fmt), run_time=1)
        self.wait(1)

        curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 2]).move_to(arrow_2.get_center())
        self.play(MoveAlongPath(arrow_2, curve))
        self.wait(1)

        self.play(ripple(machine_code), run_time=1)
        self.wait(3)

        poly = Text("Polymorphism").shift(3 * LEFT)
        self.play((FadeOut(x) for x in (
            vtable, arrow_2, arrow_1, arrow, data, heap, machine_code, text
        )), Transform(trait_object_group, poly))
        self.wait(2)



