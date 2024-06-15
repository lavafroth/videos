#!/usr/bin/env manim
from manim import *
from hackermanim import *

codefont = "Terminess Nerd Font Propo"


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style="monokai")
        code_0 = '''fn main() {
    if let Err(e) = fs::read_to_string("nonexistent") {
        let error = MyError::Io { source: e };
        println!("{:#?}", error.source());
    }
}
'''
        code_0 = Code(code=code_0, language="rust", insert_line_no=False, font_size=38)[2]
        self.add(code_0)
        target = code_0[3][26:-2];
        vb = RoundedRectangle(width=code_0[0][0].width * (1.28 * len(target)), height=target.height + .1, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05).move_to(target.get_center()).set_z_index(0)
        self.play(Create(vb))
        output = '''Some(
    Os {
        code: 2,
        kind: NotFound,
        message: "No such file or directory",
    },
)
'''
        code_1 = Code(code=output, language="rust", insert_line_no=False, font_size=34)[2].to_edge(DOWN)
        vb_ = SurroundingRectangle(code_1, buff=.25, color=BLUE, fill_opacity=0.2, fill_color=BLUE, corner_radius=0.05)
        
        self.play(code_0.animate.to_edge(UP), FadeIn(code_1), Transform(vb, vb_))
        self.wait(8)
        self.play(FadeOut(code_0, vb, code_1))
