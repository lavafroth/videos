#!/usr/bin/env manim
from manim import *
from hackermanim import *


def stackvar(color, opacity=0.5):
    return RoundedRectangle(
        width=4,
        height=1,
        color=color,
        fill_color=color,
        fill_opacity=opacity,
        corner_radius=0.05,
    )


class Sc(Scene):
    def construct(self):
        codefont = "Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        MonoParagraph.set_default(font=codefont, font_size=32)
        MonoText.set_default(font=codefont, font_size=32)

        raw = """
162 LOAD_CONST              37 (<code object <listcomp>
                                at 0x7f04f6bdedf0,
                                file "snake.py", line 15>)
164 LOAD_CONST              36 ('<listcomp>')
166 MAKE_FUNCTION            0
168 LOAD_NAME                5 (zip)
170 LOAD_NAME                0 (input_list)
172 LOAD_NAME                2 (key_list)
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        stack_var = stackvar(BLUE)
        n = 3
        stack = (stack_var.copy().fade(x / n) for x in range(n))
        stack = VGroup(*stack).arrange(DOWN).shift(2.5 * DOWN + 4 * RIGHT)
        self.play(FadeIn(code, shift=4 * UP), FadeIn(stack, shift=4 * LEFT))
        self.play(code[:3].animate.set_opacity(1))
        bob = VGroup(code[0][-21:], code[1], code[2][:-1])
        address_box = stackvar(PURPLE).next_to(stack, UP).set_z_index(-1)
        address_txt = MonoText("0x7f04f6bdedf0").move_to(address_box)
        address_grp = VGroup(address_box, address_txt)
        self.play(ReplacementTransform(bob, address_grp))
        code.set_opacity(0)
        raw = """
162 LOAD_CONST              37 (
                                                  
                                                         )
164 LOAD_CONST              36 ('<listcomp>')
166 MAKE_FUNCTION            0
168 LOAD_NAME                5 (zip)
170 LOAD_NAME                0 (input_list)
172 LOAD_NAME                2 (key_list)
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[:3].set_opacity(1)
        self.add(code)
        self.play(code[:3].animate.set_opacity(0.5), code[3].animate.set_opacity(1))
        listcomp_box = stackvar(ORANGE).next_to(address_box, UP).set_z_index(-1)
        listcomp_txt = code[3][-13:-1]
        listcomp_txt_copy = listcomp_txt.copy()
        listcomp_txt.set_opacity(0)
        self.play(
            ReplacementTransform(listcomp_txt_copy.copy(), listcomp_box),
            listcomp_txt_copy.animate.move_to(listcomp_box),
        )

        code.set_opacity(0)
        raw = """
162 LOAD_CONST              37 (
                                                  
                                                         )
164 LOAD_CONST              36 (            )
166 MAKE_FUNCTION            0
168 LOAD_NAME                5 (zip)
170 LOAD_NAME                0 (input_list)
172 LOAD_NAME                2 (key_list)
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[3].set_opacity(1)
        self.add(code)
        self.play(code[3].animate.set_opacity(0.5), code[4].animate.set_opacity(1))
        self.wait(3)
        listcomp_box.set_opacity(0)
        listcomp_txt_copy.set_opacity(0)
        address_grp.set_opacity(0)
        self.wait(4)
        self.play(
            stack.animate.shift(2 * DOWN),
            code[4].animate.set_opacity(0.5),
            code[5].animate.set_opacity(1),
        )
        phantom = stackvar(WHITE).next_to(stack, UP)
        listcomp_txt = code[5][-4:-1]
        listcomp_txt_copy = listcomp_txt.copy()
        listcomp_txt.set_opacity(0)
        zippa_box = stackvar(PURPLE).next_to(phantom, UP)
        self.play(
            ReplacementTransform(listcomp_txt_copy.copy(), zippa_box),
            listcomp_txt_copy.animate.move_to(zippa_box),
        )

        code.set_opacity(0)
        raw = """
162 LOAD_CONST              37 (
                                                  
                                                         )
164 LOAD_CONST              36 (            )
166 MAKE_FUNCTION            0
168 LOAD_NAME                5 (   )
170 LOAD_NAME                0 (input_list)
172 LOAD_NAME                2 (key_list)
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[5].set_opacity(1)
        self.add(code)
        self.play(code[5].animate.set_opacity(0.5), code[6].animate.set_opacity(1))
        listcomp_txt = code[6][-11:-1]
        listcomp_txt_copy = listcomp_txt.copy()
        listcomp_txt.set_opacity(0)
        zippa_box = stackvar(WHITE).next_to(zippa_box, UP)
        self.play(
            ReplacementTransform(listcomp_txt_copy.copy(), zippa_box),
            listcomp_txt_copy.animate.move_to(zippa_box),
        )

        code.set_opacity(0)
        raw = """
162 LOAD_CONST              37 (
                                                  
                                                         )
164 LOAD_CONST              36 (            )
166 MAKE_FUNCTION            0
168 LOAD_NAME                5 (   )
170 LOAD_NAME                0 (          )
172 LOAD_NAME                2 (key_list)
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[6].set_opacity(1)
        self.add(code)
        self.play(code[6].animate.set_opacity(0.5), code[7].animate.set_opacity(1))
        listcomp_txt = code[7][-9:-1]
        listcomp_txt_copy = listcomp_txt.copy()
        listcomp_txt.set_opacity(0)
        zippa_box = stackvar(WHITE).next_to(zippa_box, UP)
        self.play(
            ReplacementTransform(listcomp_txt_copy.copy(), zippa_box),
            listcomp_txt_copy.animate.move_to(zippa_box),
        )

        code.set_opacity(0)
        raw = """
162 LOAD_CONST              37 (
                                                  
                                                         )
164 LOAD_CONST              36 (            )
166 MAKE_FUNCTION            0
168 LOAD_NAME                5 (   )
170 LOAD_NAME                0 (          )
172 LOAD_NAME                2 (        )
174 CALL_FUNCTION            2
176 GET_ITER
178 CALL_FUNCTION            1
180 STORE_NAME               6 (result)
""".strip()
        code = MonoParagraph(raw).to_edge(UL).set_opacity(0.5)
        code[7].set_opacity(1)
        self.add(code)
        self.play(code[7].animate.set_opacity(0.5), code[8].animate.set_opacity(1))
        self.play(FadeOut(code[:8], shift=4 * UP), code[8:].animate.to_edge(UL))
        self.wait(3)
