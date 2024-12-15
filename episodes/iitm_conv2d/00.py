#!/usr/bin/env manim
from manim import *


np.random.seed(42)


# Generally in case of a quadratic input size, the width equals the height
def new_tensor(
    width: int,
    height: int | None = None,
    padding=0,
    text_opacity=0,
    corner=UL,
    **kwargs,
) -> VGroup:
    height = height or width
    tensor_raw = np.random.randint(10, size=(width, height))
    tensor_padded = np.pad(tensor_raw, padding)

    row_group = VGroup()
    for row in range(height + 2 * padding):
        col_group = VGroup()
        for col in range(width + 2 * padding):
            pixel = Rectangle(height=1, width=1, grid_xstep=1, grid_ystep=1, **kwargs)
            value = Text(str(tensor_padded[row, col])).scale(0.75)
            # print(value)
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
    return row_group


class ThreeDCameraRotation(ThreeDScene):
    def construct(self):
        # axes = ThreeDAxes()
        stride = 2
        padding = 1

        input_size = 5
        kernel_size = 3
        output_size = (input_size - kernel_size + 2 * padding) // stride + 1

        self.add_fixed_in_frame_mobjects(
            VGroup(
                Tex(f"Input size = {input_size}"),
                Tex(f"Kernel size = {kernel_size}"),
                Tex(f"Stride = {stride}"),
                Tex(f"Padding = {padding}"),
            )
            .arrange(DOWN)
            .scale(0.75)
            .to_edge(UL)
        )

        self.set_camera_orientation(phi=PI / 4, theta=-3 * PI / 4)
        tensor = new_tensor(
            input_size,
            padding=padding,
            fill_color=BLUE,
            color=BLUE_E,
            fill_opacity=1,
        )

        kernel = new_tensor(
            kernel_size,
            fill_color=GRAY,
            color=BLUE_E,
            fill_opacity=0.5,
            text_opacity=1,
            corner=DR,
        ).move_to(tensor.get_corner(UL) - kernel_size / 2 * UL)

        output = new_tensor(
            output_size,
            fill_color=TEAL,
            fill_opacity=1,
            color=TEAL_E,
        ).set_z(2)

        self.play(Write(tensor))
        self.play(FadeIn(kernel))

        dangling_animations = []
        for row in range(output_size):

            anims = []
            for i, t_row in enumerate(tensor):
                for j, t_val in enumerate(t_row):
                    t_val = iter(t_val)
                    _cell = next(t_val)
                    text = next(t_val)
                    if (
                        row * stride <= i < (row) * stride + kernel_size
                        and 0 <= j < kernel_size
                    ):
                        print(f"got one: {i}, {j}")
                        dangling_animations.append(text.animate.set_opacity(1))
                    else:
                        dangling_animations.append(text.animate.set_opacity(0))

            self.play(*dangling_animations)
            dangling_animations.clear()
            self.wait()
            kernel_original_pos = kernel.copy()

            for col in range(output_size - 1):
                anims = []
                for i, t_row in enumerate(tensor):
                    for j, t_val in enumerate(t_row):
                        t_val = iter(t_val)
                        _cell = next(t_val)
                        text = next(t_val)
                        if (
                            (row) * stride <= i < (row) * stride + kernel_size
                            and (col + 1) * stride <= j < (col + 1) * stride + kernel_size
                        ):
                            print(f"got one: {i}, {j}")
                            anims.append(text.animate.set_opacity(1))
                        else:
                            anims.append(text.animate.set_opacity(0))

                self.play(kernel.animate.shift(RIGHT * stride), *anims)
                self.wait()

            # don't move the filter down the last time
            if row == output_size - 1:
                break

            kernel_original_pos.shift(DOWN * stride)
            dangling_animations.append(Transform(kernel, kernel_original_pos))

        self.wait(4)
