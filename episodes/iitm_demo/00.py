#!/usr/bin/env manim
from manim import *
from manim import Transform as T, ReplacementTransform as RT
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")

        radius = 0.5
        circle = Circle(radius, color=TEAL_D, fill_opacity=0.6)
        circles = [circle.copy() for _ in range(5)]
        ellipsis = Tex("...")
        marbles = VGroup(*circles, ellipsis, circle).arrange()
        self.play(AnimationGroup(map(FadeIn, circles), lag_ratio=0.1))
        self.play(Write(ellipsis), run_time=0.2)
        self.play(FadeIn(circle), run_time=0.3)

        brace = Brace(marbles, UP, sharpness=0.4)
        n = Tex("$$n$$").next_to(brace, UP)[0]
        self.play(Write(brace), Write(n))

        n_objects = VGroup(n, brace, marbles)

        self.wait(3)
        self.play(n_objects.animate.shift(UP))

        slot = Line(ORIGIN, RIGHT, color=WHITE)
        slots = [slot.copy() for _ in range(3)]
        slots_w_ell = VGroup(*slots, ellipsis.copy(), slot).arrange().shift(2 * DOWN)
        slots = VGroup(*slots, slot)
        self.play(Write(slots_w_ell), run_time=1.5)
        r_brace = Brace(slots_w_ell, DOWN, sharpness=0.4)
        r = Tex("$$r$$").next_to(r_brace, DOWN)[0]
        self.play(Write(r_brace), Write(r))

        self.wait(3)

        phantom = Circle(0, color=TEAL_D, fill_opacity=0).move_to(
            ellipsis.get_center() + 0.5 * DOWN
        )
        phantom_copy = phantom.copy()
        phantom_into = circle.copy().next_to(slots[3], UP)

        ghost = DashedVMobject(circle.copy(), num_dashes=10)
        ghosts = [ghost.copy() for _ in range(3)]

        anims = []

        for ghost, pos in zip(ghosts, (1, 2, 4)):
            ghost.move_to(circles[pos])
            anims.append(FadeIn(ghost))

        self.play(
            AnimationGroup(
                circles[1].animate.next_to(slots[2], UP),
                circles[2].animate.next_to(slots[0], UP),
                circles[4].animate.next_to(slots[1], UP),
                T(phantom, phantom_into),
                *anims,
            )
        )

        n_objects.add(*ghosts, phantom_copy)
        filled_slots = VGroup(slots_w_ell, phantom, r, r_brace)

        self.wait(2)
        self.play(VGroup(filled_slots, n_objects).animate.shift(2 * LEFT))
        self.wait(2)
        binom = Tex(r"$$\binom{n}{r}$$").shift(4.5 * RIGHT)[0]
        self.play(
            AnimationGroup(
                Write(binom[0]),
                AnimationGroup(RT(n, binom[1]), FadeOut(brace)),
                AnimationGroup(RT(r, binom[2]), FadeOut(r_brace)),
                Write(binom[3]),
                lag_ratio=0.1,
            ),
            run_time=1.5,
        )

        self.wait(3)
        self.play(
            circles[1].animate.move_to(ghosts[0]),
            circles[2].animate.move_to(ghosts[1]),
            circles[4].animate.move_to(ghosts[2]),
            Transform(phantom, phantom_copy),
            *[map(FadeOut, ghosts)],
        )

        self.wait(2)
        self.play(circles[0].animate.set(color=ORANGE))
        self.wait(2)
        highlight = binom.copy()
        self.play(Write(highlight))
        self.play(FadeOut(highlight))
        self.wait(2)

        self.play(
            binom.animate.shift(4 * RIGHT),
            VGroup(slots_w_ell, marbles).animate.shift(2 * RIGHT),
        )

        includes_red = slots_w_ell.copy().scale(0.75).shift(3.5 * LEFT).set_z_index(2)
        excludes_red = slots_w_ell.copy().scale(0.75).shift(3.5 * RIGHT).set_z_index(2)

        surr_in_red = RoundedRectangle(
            width=includes_red.width + 0.5,
            height=2,
            color=ORANGE,
            fill_opacity=0.1,
            corner_radius=0.1,
        ).move_to(includes_red.get_center() + 0.75 * UP)
        surr_ex_red = RoundedRectangle(
            width=includes_red.width + 0.5,
            height=2,
            color=TEAL_D,
            fill_opacity=0.1,
            corner_radius=0.1,
        ).move_to(excludes_red.get_center() + 0.75 * UP)
        marker = marbles.copy().scale(0.75).to_edge(UP)

        arr0 = Arrow(marker.get_center() + 0.5 * DL, surr_in_red, stroke_width=3)
        arr1 = Arrow(marker.get_center() + 0.5 * DR, surr_ex_red, stroke_width=3)

        self.play(
            marbles.animate.scale(0.75).to_edge(UP),
            AnimationGroup(
                AnimationGroup(
                    RT(slots_w_ell, includes_red),
                    RT(slots_w_ell.copy(), excludes_red),
                ),
                AnimationGroup(
                    Create(arr0),
                    Create(arr1),
                    Create(surr_in_red),
                    Create(surr_ex_red),
                ),
                lag_ratio=0.4,
            ),
        )

        teal075 = Circle(radius * 0.75, color=TEAL_D, fill_opacity=0.6)
        red075 = Circle(radius * 0.75, color=ORANGE, fill_opacity=0.6)

        in_red_box = [
            teal075.copy(),
            red075.copy(),
            teal075.copy(),
            teal075.copy(),
        ]

        for x, y in zip(in_red_box, [*includes_red[:3], includes_red[-1]]):
            x.next_to(y, UP)

        in_teal_box = [
            teal075.copy(),
            teal075.copy(),
            teal075.copy(),
            teal075.copy(),
        ]

        for x, y in zip(in_teal_box, [*excludes_red[:3], excludes_red[-1]]):
            x.next_to(y, UP)

        self.play(AnimationGroup(map(FadeIn, in_red_box), lag_ratio=0.2))
        self.wait(1)
        self.play(AnimationGroup(map(FadeIn, in_teal_box), lag_ratio=0.2))

        obscure = VGroup(
            *in_teal_box,
            *in_red_box,
            surr_in_red,
            surr_ex_red,
            includes_red,
            excludes_red,
            arr0,
            arr1,
        )

        obscure_copy = obscure.copy()

        self.play(
            obscure.animate.scale(1.2).shift(8 * DOWN).fade(1),
            marbles.animate.scale(1 / 0.75).move_to(ORIGIN),
        )

        self.wait(3)
        self.play(marbles.animate.shift(UP))

        slots_w_ell.scale(1 / 0.75).move_to(2 * DOWN)
        phantoms = [slot.copy().shift(UP * 0.2).set_opacity(0) for slot in slots_w_ell]
        self.play(
            AnimationGroup(
                (RT(x, y) for x, y in zip(phantoms, slots_w_ell)), lag_ratio=0.1
            )
        )

        self.wait(4)

        n_brace = Brace(marbles, UP, sharpness=0.4)

        red = marbles[0]
        red_ghost = DashedVMobject(red.copy(), num_dashes=10)

        self.play(FadeIn(red_ghost), red.animate.next_to(slots_w_ell[0], UP))

        r_brace = Brace(slots_w_ell, DOWN, sharpness=0.4)
        r = Tex("$$r$$").next_to(r_brace, DOWN)[0]

        self.play(FadeIn(r_brace, r))
        r_1_brace = Brace(slots_w_ell[1:], DOWN, sharpness=0.4)
        r_1 = Tex("$$r - 1$$").next_to(r_1_brace, DOWN)[0]
        self.play(
            T(r_brace, r_1_brace),
            T(r, r_1),
        )

        n = Tex("$$n$$").next_to(n_brace, UP)[0]
        self.play(FadeIn(n_brace, n))

        n_1_brace = Brace(marbles[1:], UP, sharpness=0.4)
        n_1 = Tex("$$n - 1$$").next_to(n_1_brace, UP)[0]

        self.play(
            T(n_brace, n_1_brace),
            T(n, n_1),
        )

        self.wait(4)

        binom_1 = Tex(r"$$\binom{n - 1}{r - 1}$$").shift(5 * RIGHT)[0]
        self.play(
            RT(n, binom_1[1:4]),
            RT(r, binom_1[4:-1]),
            Write(binom_1[0]),
            Write(binom_1[-1]),
            FadeOut(n_brace),
            FadeOut(r_brace),
        )

        self.wait(2)

        self.play(binom_1.animate.to_edge(UR))
        self.play(
            binom_1.animate.set_opacity(0.4),
            FadeOut(red_ghost),
            red.animate.move_to(red_ghost),
        )
        self.wait(4)

        x_scale = 0.5
        x = VGroup(
            Line(start=x_scale * UR, end=x_scale * DL, stroke_width=5, color=RED),
            Line(start=x_scale * UL, end=x_scale * DR, stroke_width=5, color=RED),
        ).move_to(red)

        red_clone = red.copy()
        self.play(
            red.animate.set_opacity(0.4),
            AnimationGroup(map(Create, x), lag_ratio=0.5),
            run_time=1,
        )

        self.wait(2)

        r_brace = Brace(slots_w_ell, DOWN, sharpness=0.4)
        r = Tex("$$r$$").next_to(r_brace, DOWN)[0]
        self.play(FadeIn(r_brace, r))

        n = Tex("$$n$$").next_to(n_brace, UP)[0]
        n_brace = Brace(marbles, UP, sharpness=0.4)

        n_1_brace = Brace(marbles[1:], UP, sharpness=0.4)
        n_1 = Tex("$$n - 1$$").next_to(n_1_brace, UP)[0]

        self.play(FadeIn(n, n_brace))
        self.play(
            T(n, n_1),
            T(n_brace, n_1_brace),
        )

        self.wait(4)

        binom_2 = Tex(r"$$\binom{n - 1}{r}$$").shift(5 * RIGHT)[0]
        self.play(
            RT(n, binom_2[1:4]),
            RT(r, binom_2[4:-1]),
            Write(binom_2[0]),
            Write(binom_2[-1]),
            FadeOut(n_brace),
            FadeOut(r_brace),
        )

        self.wait(2)

        self.play(binom_2.animate.next_to(binom_1, DOWN).set_opacity(0.4))
        self.play(FadeOut(x), T(red, red_clone))

        obscure_copy.scale(0.8).shift(0.4 * UP)
        self.play(
            marbles.animate.scale(0.75).to_edge(UP),
            T(obscure, obscure_copy),
            FadeOut(slots_w_ell),
        )

        self.play(binom_1.animate.next_to(obscure[-6], DOWN).set_opacity(1))
        self.wait(1)
        self.play(binom_2.animate.next_to(obscure[-5], DOWN).set_opacity(1))
        self.wait(2)

        plus = Tex("$$+$$").move_to(binom_1.get_center() * UP)
        self.play(Write(plus))
        expr = VGroup(binom_1, plus, binom_2)
        self.play(FadeOut(obscure), expr.animate.arrange().move_to(ORIGIN))
        delta = LEFT
        expr_clone = expr.copy().shift(delta)
        equ = Tex("$$=$$").next_to(expr_clone, RIGHT)
        self.play(AnimationGroup(expr.animate.shift(delta), Write(equ), binom.animate.next_to(equ), lag_ratio=0.2))
        self.wait(8)
