#!/usr/bin/env manim
from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from custom import CodeTransformer, octicon


class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
        r2 = Text("radare2", font="Terminess Nerd Font Propo")
        self.add(r2)
        invoc = Text(
            "r2 target/release/cleancode",
            font="Terminess Nerd Font Propo",
            font_size=28,
        ).to_edge(UL)
        self.play(Transform(r2, invoc))
        pr = (
            Text(
                """WARN: Relocs has not been applied.
Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next
time
[0x00008450]>""",
                font="Terminess Nerd Font Propo",
                font_size=28,
                t2c={"[-13:]": YELLOW},
            )
            .to_edge(UL)
            .shift(0.5 * DOWN)
        )
        self.play(Write(pr))
        aaa = (
            Text("aaa", font="Terminess Nerd Font Propo", font_size=28)
            .to_edge(UL)
            .shift(2.8 * RIGHT + 1.7 * DOWN)
        )
        self.play(Write(aaa))
        _aaa = Text("a\na\na", font="Terminess Nerd Font Propo", font_size=28)
        self.play(Transform(aaa, _aaa))
        _aaa = Paragraph(
            "analyze\nall\n(autonamed) functions",
            font="Terminess Nerd Font Propo",
            font_size=28,
        )
        self.play(Transform(aaa, _aaa))
        self.wait(2)
        _aaa = Text("a\na\na", font="Terminess Nerd Font Propo", font_size=28)
        self.play(Transform(aaa, _aaa))
        _aaa = (
            Text("aaa", font="Terminess Nerd Font Propo", font_size=28)
            .to_edge(UL)
            .shift(2.8 * RIGHT + 1.7 * DOWN)
        )
        self.play(Transform(aaa, _aaa))
        logs = Text(
            """INFO: Analyze all flags starting with sym. and entry0 (aa)
INFO: Analyze imports (af@@@i)
INFO: Analyze entrypoint (af@ entry0)
INFO: Analyze symbols (af@@@s)
WARN: Cannot find basic block for switch case at 0x0002674f bbdelta
WARN: Cannot find basic block for switch case at 0x00021fb7 bbdelta
INFO: Recovering variables
INFO: Analyze all functions arguments/locals (afva@@@F)
INFO: Analyze function calls (aac)
INFO: Analyze len bytes of instructions for references (aar)
INFO: Finding and parsing C++ vtables (avrr)
INFO: Analyzing methods
INFO: Recovering local variables (afva)
INFO: Type matching analysis for all functions (aaft)
INFO: Propagate noreturn information (aanr)
INFO: Use -AA or aaaa to perform additional experimental analysis""",
            font="Terminess Nerd Font Propo",
            font_size=28,
            t2c={"INFO:": ORANGE, "WARN:": PURPLE},
        ).shift(1.6 * DOWN)
        grp = Group(r2, aaa, logs, pr)
        self.play(Write(logs))
        self.play(grp.animate.shift(8 * UP))
        pr = (
            Text(
                "[0x00008450]>",
                font="Terminess Nerd Font Propo",
                font_size=28,
                color=YELLOW,
            )
            .to_edge(UL)
            .shift(.3 * DOWN)
        )
        self.play(Write(pr))
