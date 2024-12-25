#!/usr/bin/env manim
from manim import Text, VGroup, Transform, Rectangle, DashedVMobject, np, Write, ReplacementTransform, FadeOut, UP, DOWN, LEFT, RIGHT, Scene, Tex, UL, DR, UR, DL, FadeIn
from typing import List, Tuple

# I come from a procedural / imperative programming background
# and prefer structs to classes.
from dataclasses import dataclass

# this import's a catchall for experimenting around
# from manim import *

np.random.seed(42)

@dataclass
class TensorElement:
    value: np.dtypes.Float32DType()
    text: Text

@dataclass
class Tensor:
    representation: VGroup
    matrix: np.array

    # Generally in case of a quadratic input size, the width equals the height
    def new(
        width: int,
        height: int | None = None,
        padding=0,
        text_opacity=0,
        corner=UL,
        **kwargs,
    ) -> 'Tensor':
        height = height or width
        tensor_raw = np.random.randint(10, size=(width, height))
        tensor_padded = np.pad(tensor_raw, padding)

        row_group = VGroup()
        for row in range(height + 2 * padding):
            col_group = VGroup()
            for col in range(width + 2 * padding):
                pixel = Rectangle(height=1, width=1, grid_xstep=1, grid_ystep=1, **kwargs)
                value = Text(str(tensor_padded[row, col])).scale(0.75)
                if (
                    row < padding
                    or row > height - 1 + padding
                    or col < padding
                    or col > width - 1 + padding
                ):
                    # this is a padding cell, make it dashed
                    pixel = DashedVMobject(pixel, num_dashes=9)

                if (corner == UL).all():
                    value.move_to(
                        pixel.get_corner(UL)
                        + value.width / 2 * RIGHT
                        + value.height / 2 * DOWN
                        + 0.2 * DR
                    )
                else:
                    value.move_to(
                        pixel.get_corner(DR)
                        + value.width / 2 * LEFT
                        + value.height / 2 * UP
                        + 0.2 * UL
                    )

                value.set_opacity(text_opacity)
                pixel_with_value = VGroup(pixel, value)
                col_group.add(pixel_with_value)
            col_group.arrange(buff=0)
            row_group.add(col_group)
        row_group.arrange(direction=DOWN, buff=0)
        return Tensor(row_group, tensor_padded)

    def values_under_kernel(self, output_col_m1: int, output_row: int, stride: int, kernel_size: int) -> Tuple[List[TensorElement], List[TensorElement]]:
        truthy = []
        falsy = []
        for i, t_row in enumerate(self.representation):
            for j, t_val in enumerate(t_row):
                t_val = iter(t_val)
                _cell = next(t_val)
                text = next(t_val)
                if (
                    output_row * stride <= i < (output_row) * stride + kernel_size
                    and (output_col_m1 + 1) * stride <= j < (output_col_m1 + 1) * stride + kernel_size
                ):
                    truthy.append(TensorElement(self.matrix[i][j], text))
                else:
                    falsy.append(TensorElement(self.matrix[i][j], text))
    
        return (truthy, falsy)

    def values(self) -> List[TensorElement]:
        values = []
        for i, k_row in enumerate(self.representation):
            for j, k_val in enumerate(k_row):
                k_val = iter(k_val)
                _cell = next(k_val)
                text = next(k_val)
                values.append(TensorElement(self.matrix[i][j], text))
        return values

def fake_isometry(p, theta: float, gamma: float):
    x = p[0]
    y = p[1]
    return np.array([
        x * np.cos(theta) - y * np.sin(theta),
        x*gamma * np.sin(theta) + y * gamma * np.cos(theta),
        p[2]
    ])

def anim_dot_product(scene: Scene, row, col, kernel: Tensor, truthy, output: Tensor, bottom_line: Text, run_time: float, bottom_line_val: Text):
    dot_product = 0
    for op_a, op_b in zip(kernel.values(), truthy):
        op_a_str = str(op_a.value)
        op_b_str = str(op_b.value)
        prod = op_a.value * op_b.value
        prod_str = str(prod)
        dot_product += prod
        equation_str = f"{op_b_str}({op_a_str}) = {prod_str}"
        equation = Text(equation_str, font_size=26)
        equation.next_to(bottom_line, UP).to_edge(LEFT)
        op_a_copy = op_a.text.copy()
        op_b_copy = op_b.text.copy()
        op_a.text.set_opacity(0)
        op_b.text.set_opacity(0)
        scene.add(op_a_copy)
        scene.add(op_b_copy)
        scene.play(
            ReplacementTransform(op_a_copy, equation[:len(op_b_str)]),
            ReplacementTransform(op_b_copy, equation[len(op_b_str)+1:len(op_b_str)+1+len(op_a_str)]),
            run_time=run_time,
        )
        scene.play(Write(equation[len(op_b_str)]), Write(equation[len(op_b_str)+1+len(op_a_str):]), run_time=run_time)
        bottom_line_val_next = Text(str(dot_product), font_size=26).next_to(bottom_line, RIGHT)
        prod_text = equation[len(op_b_str)+1+len(op_a_str)+2:]
        scene.play(ReplacementTransform(VGroup(bottom_line_val, prod_text), bottom_line_val_next), FadeOut(equation[:len(op_b_str)+1+len(op_a_str)+2]), run_time=run_time)
        bottom_line_val = bottom_line_val_next

    cell = output.representation[row][col+1]
    cell.z_index = 4
    bottom_line_val.z_index = 4
    bottom_line_val_next = Text(str(0), font_size=26).next_to(bottom_line, RIGHT)
    scene.play(Transform(bottom_line_val, cell), Write(bottom_line_val_next), run_time=run_time)
    return bottom_line_val_next

class Sc(Scene):
    def construct(self):

        Text.set_default(font="monospace", font_size=30)
        stride = 2
        padding = 1

        input_size = 5
        kernel_size = 3
        output_size = (input_size - kernel_size + 2 * padding) // stride + 1

        last_run_time = 0.1
        speed_up_factor = last_run_time ** (-1/(output_size ** 2))

        theta = np.pi/4
        gamma = 1.0995574287564276
        fake_3d = lambda p: fake_isometry(p, theta, gamma/(np.pi/2))  # noqa: E731

        self.add(
            VGroup(
                Tex(f"Input size = {input_size}"),
                Tex(f"Kernel size = {kernel_size}"),
                Tex(f"Stride = {stride}"),
                Tex(f"Padding = {padding}"),
            )
            .arrange(DOWN)
            .scale(0.75)
            .to_edge(UR)
        )

        LINE_COLOR = '#b6d09e'

        run_time = 1

        tensor = Tensor.new(
            input_size,
            padding=padding,
            fill_color=LINE_COLOR,
            text_opacity=1,
            fill_opacity=0.5,
            color=LINE_COLOR,
        )

        kernel = Tensor.new(
            kernel_size,
            fill_color='#d4bbd1',
            color='#aea8d1',
            fill_opacity=0.5,
            text_opacity=1,
            corner=DR,
        )
        kernel.representation.move_to(tensor.representation.get_corner(UL) - kernel_size / 2 * UL)
        tensor.representation.apply_function(fake_3d)
        kernel.representation.apply_function(fake_3d)

        output = Tensor.new(
            output_size,
            fill_color="#0e2433",
            fill_opacity=.9,
            color='#75c9cc',
        )

        output.representation.apply_function(fake_3d).shift(.5 * UP)
        self.play(Write(tensor.representation))
        self.play(FadeIn(kernel.representation, shift=0.2 * DOWN))
        truthy, falsy = tensor.values_under_kernel(-1, 0, stride, kernel_size)
        self.play(map(lambda f: f.text.animate.set_opacity(0), falsy))
        bottom_line = Text("Total = ", font_size=26).to_edge(DL)
        bottom_line_val = Text(str(0), font_size=26).next_to(bottom_line, RIGHT)
        self.play(Write(bottom_line), Write(bottom_line_val))

        dangling_animations = []
        for row in range(output_size):
            col = -1
            truthy, falsy = tensor.values_under_kernel(col, row, stride, kernel_size)

            dangling_animations.extend((value.text.animate.set_opacity(1) for value in truthy))
            dangling_animations.extend((value.text.animate.set_opacity(0) for value in falsy))

            self.play(*dangling_animations)

            bottom_line_val = anim_dot_product(self, row, col, kernel, truthy, output, bottom_line, run_time, bottom_line_val)
            run_time /= speed_up_factor

            # Bring the kernel values back on screen
            self.play(value.text.animate.set_opacity(1) for value in kernel.values())

            kernel_original_pos = kernel.representation.copy()

            for col in range(output_size - 1):
                anims = []
                truthy, falsy = tensor.values_under_kernel(col, row, stride, kernel_size)
                anims.extend((value.text.animate.set_opacity(1) for value in truthy))
                anims.extend((value.text.animate.set_opacity(0) for value in falsy))
                
                self.play(kernel.representation.animate.shift(fake_3d(RIGHT) * stride), *anims)

                bottom_line_val = anim_dot_product(self, row, col, kernel, truthy, output, bottom_line, run_time, bottom_line_val)
                # Bring the kernel values back on screen
                self.play(value.text.animate.set_opacity(1) for value in kernel.values())

            run_time /= speed_up_factor
            # don't move the filter down the last time
            if row == output_size - 1:
                break

            kernel_original_pos.shift(fake_3d(DOWN) * stride)
            dangling_animations.append(Transform(kernel.representation, kernel_original_pos))

        self.wait(4)
