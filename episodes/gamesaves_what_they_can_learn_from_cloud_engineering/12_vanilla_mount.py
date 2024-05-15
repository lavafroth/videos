#!/usr/bin/env manim
from manim import *

def str_to_text_mobject(i: int, s: Text):
    shift = i * 0.5 * DOWN
    return s.to_edge(UL).shift(shift)

class CodeBlock(Scene):
    def construct(self):
        drawables = [
            Text("mkdir upperdir work", t2c={"upperdir": TEAL, "work": YELLOW}, font_size="28", font="monospace"),
            Text("mv game lowerdir", t2c={"lowerdir": BLUE}, font_size="28", font="monospace"),
            Text("mount -t overlay overlay \\", t2c={"upperdir": TEAL, "workdir": YELLOW, "lowerdir": BLUE}, font_size="28", font="monospace"),
            Text("-o lowerdir=lowerdir,upperdir=upperdir,work=work game", t2c={"upperdir": TEAL, "work":YELLOW, "lowerdir": BLUE}, font_size="28", font="monospace"),
        ]
        drawables = [
            str_to_text_mobject(i, s)
            for i, s in enumerate(drawables)
        ]
        for i, drawable in enumerate(drawables):
            self.play(Write(drawable))
            if i == 2:
                continue
            self.wait(4)

        horizontal_line = DashedLine(start=np.array([-8, 1.25, 0]), end=np.array([8, 1.25, 0]), color=GRAY)
        self.play(Create(horizontal_line))
        
        error = Text("""mount: game: must be superuser to use mount.
       dmesg(1) may have more information after failed mount system call.""", font_size="28", font="monospace").to_edge(UL).shift(len(drawables) * 0.5 * DOWN + 0.75 * DOWN)
        self.play(Write(error))
        self.wait(4)
