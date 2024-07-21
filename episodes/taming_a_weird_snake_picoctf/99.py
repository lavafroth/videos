#!/usr/bin/env manim

from manim import *
from manim import VGroup as V, ReplacementTransform as RT, Transform as T
from hackermanim import *
from stack import *


def stackvar_(color, opacity=0.5):
    return stackvar(color, opacity).set_z_index(-1)


def chunks3(obj, x, y):
    return (obj[:x], obj[x:y], obj[y:])


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)
        raw = """
182 LOAD_CONST              38 ('')
184 LOAD_METHOD              7 (join)
186 LOAD_NAME                8 (map)
188 LOAD_NAME                9 (chr)
190 LOAD_NAME                6 (result)
192 CALL_FUNCTION            2
194 CALL_METHOD              1
196 STORE_NAME              10 (result_text)
198 LOAD_CONST              39 (None)
200 RETURN_VALUE
        """.strip()

        code = MonoParagraph(raw).to_edge(UL).set_opacity(1).shift(0.3 * LEFT)
        stack.shift(4.5 * DOWN + 4 * RIGHT)
        l, chra, r = chunks3(code[3], -4, -1)
        mapa = stackvar_(PURPLE)
        f = [
            stackvar_(WHITE),
            stackvar_(WHITE),
            mapa,
            stackvar_(WHITE),
            stackvar_(WHITE),
        ]
        V(*list(reversed(f))).arrange(DOWN).next_to(stack, UP)
        t = MonoText("map").move_to(mapa)
        mapg = V(mapa, t)

        popo = V(
            MonoText("map(", font_size=40, color=PURPLE),
            Tex("$f$", font_size=60),
            MonoText(",", font_size=40, color=PURPLE),
            SVGMobject("iter-rot", fill_color=WHITE).scale(0.3),
            MonoText(")", font_size=40, color=PURPLE),
        ).arrange()
        maph = V(
            popo[0],
            popo[2],
            popo[4],
        )
        f = popo[1]
        i = popo[3]
        self.play(RT(mapg, maph))
        self.play(Write(f), FadeIn(i))
        self.wait(1)

        c = Circle(radius=0.2, color=TEAL, fill_color=TEAL, fill_opacity=0.5)
        c_ = c.copy().move_to(i).set_opacity(0)
        fc = f.copy()
        fifi = (
            V(
                Tex("$f$", font_size=60),
                Tex("$($", font_size=60),
                c,
                Tex("$)$", font_size=60),
            )
            .arrange()
            .next_to(popo, DOWN)
        )
        self.play(i.animate.rotate(PI / 2), RT(c_, c), FadeIn(fc))
        self.play(RT(fc, fifi[0]), Write(fifi[1]), Write(fifi[3]))

        for _ in range(2):
            fio = fifi

            c = Circle(radius=0.2, color=TEAL, fill_color=TEAL, fill_opacity=0.5)
            c_ = c.copy().move_to(i).set_opacity(0)
            fc = f.copy()
            fifi = (
                V(
                    Tex("$f$", font_size=60),
                    Tex("$($", font_size=60),
                    c,
                    Tex("$)$", font_size=60),
                )
                .arrange()
                .next_to(popo, DOWN)
            )
            self.play(
                i.animate.rotate(PI / 2),
                RT(c_, c),
                FadeIn(fc),
                FadeOut(fio, shift=DOWN),
            )
            self.play(RT(fc, fifi[0]), Write(fifi[1]), Write(fifi[3]))

        self.play(FadeOut(fifi, shift=DOWN))
        self.wait(2)
        self.play(popo.animate.move_to(3.5 * LEFT + 2 * DOWN))
        self.play(FadeOut(f), FadeOut(i))
        t = MonoText("map(   ,       )", font_size=40, color=PURPLE).move_to(popo)
        self.play(
            Transform(popo[0], t[:4]),
            Transform(popo[2], t[4]),
            Transform(popo[4], t[-1]),
        )
        self.wait(1)
