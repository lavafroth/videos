#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')
        
        f = Text('#[source]', font=codefont, font_size=50, color=GREEN_D)
        self.play(Write(f))
        self.wait(3)
        buff = 16 * RIGHT
        code = Code('error_trait.rs', font_size=32, insert_line_no=False)[2].shift(buff).set_z_index(1)
        self.play(x.animate.shift(-buff) for x in (f, code))
        self.wait(6)
        ripple = code[0][:-1]
        anims = []
        curve = ParametricFunction(
            lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1]
        )
        for char in ripple:
            curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
            anims.append(MoveAlongPath(char, curve))
        self.play(AnimationGroup(anims, lag_ratio=0.1), run_time=2)

        vb = RoundedRectangle(width=code[0][0].width * (len(code[2]) + 9), height=code[2].height - .1, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05).move_to(code[2].get_center() + 0.1 * DOWN).set_z_index(0)
        self.play(Create(vb))
        self.wait(1)
        
        ne = code[2][24:54]
        vb_ = RoundedRectangle(width=code[0][0].width * (len(ne) + 7), height=code[2].height - .1, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05).move_to(ne.get_center()).set_z_index(0)
        self.play(Transform(vb, vb_))
        self.play(FadeOut(code[:2], code[3:]))
        scale = 2
        some = Text('Some(', font=codefont).shift(2 * scale * LEFT + DOWN)
        c = Circle(radius=0.4, color=BLUE, fill_color=BLUE, fill_opacity=.5).next_to(some, buff=0.1)
        some_ = Text(')', font=codefont).next_to(c, buff=0.1)

        stroke_width = 3

        none = Text('None', font=codefont).shift(scale * RIGHT + DOWN)
        option = ne[:6]
        asome= Arrow(option.get_edge_center(DOWN), some.get_edge_center(UP), stroke_width=stroke_width)
        anone = Arrow(option.get_edge_center(DOWN), none.get_edge_center(UP), stroke_width=stroke_width)
        self.play(Create(asome), Create(anone))
        self.play(Write(some), Write(some_), Write(none))

        option_t = code[2][24+8:52]
        vb_ = RoundedRectangle(width=code[0][0].width * (len(option_t) + 6.5), height=code[2].height - .1, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05).move_to(option_t.get_center() + .05 * LEFT).set_z_index(0)
        self.play(Transform(vb, vb_))
        grp = Group(vb, code[2][31:53])
        self.play(ReplacementTransform(grp, c))
        some = Group(some, some_)
        
        src_a, src_b, src_c = code[2][:3+4], code[2][3+4:9+4], code[2][9+4:]

        code_2 = '''use thiserror::Error;

#[derive(Debug, Error)]
pub enum MyError {
    Io(#[source] std::io::Error),
}
'''

        code_2 = Code(code=code_2, font_size=40, language='rust', insert_line_no=False)[2]
        crib = code_2[4]
        eve = Group(code_2[:4], code_2[5:], crib[:7], crib[-2:])

        self.play(FadeOut(src_a, src_c, asome, anone, some, none))
        self.play(
                  FadeIn(eve), ReplacementTransform(src_b, crib[9:-18]),
                  ReplacementTransform(c, crib[-16:-2]),
              )
        self.play(Write(crib[7:9]), Write(crib[15]))
        self.wait(5)
        self.play(code_2.animate.shift(14 * LEFT))
