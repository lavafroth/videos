#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        Text.set_default(font="Poppins")
        Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
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
        ).shift(1.6 * DOWN + 8 * UP)
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

        self.add(logs, pr)
        self.wait(2)
        aaa = (
            Text("afl", font="Terminess Nerd Font Propo", font_size=28)
            .to_edge(UL)
            .shift(2.8 * RIGHT + .3 * DOWN)
        )
        grp = Group(pr, logs, aaa)
        self.play(Write(aaa))
        _aaa = Text("a\nf\nl", font="Terminess Nerd Font Propo", font_size=28)
        self.play(Transform(aaa, _aaa))
        
        _aaa = Paragraph(
            "analyze\nfunction\nlist",
            font="Terminess Nerd Font Propo",
            font_size=28,
        )
        self.play(Transform(aaa, _aaa))
        self.wait(2)
        _aaa = Text("a\nf\nl", font="Terminess Nerd Font Propo", font_size=28)
        self.play(Transform(aaa, _aaa))
        _aaa = (
            Text("afl", font="Terminess Nerd Font Propo", font_size=28)
            .to_edge(UL)
            .shift(2.8 * RIGHT + .3 * DOWN)
        )
        self.play(Transform(aaa, _aaa))
        rg = (
            Text("| rg main", font="Terminess Nerd Font Propo", font_size=28)
            .to_edge(UL)
            .shift(3.6 * RIGHT + .3 * DOWN)
        )
        grp.add(rg)
        self.play(Write(rg))
        logs = (
            Text("""0x000086c0   38    884 sym.cleancode::main::he34f242c79130c17                                                                                                                                                     │
0x00008a80    1     39 main""", font="Terminess Nerd Font Propo", font_size=28, t2c={'main': RED})
            .to_edge(UL)
            .shift(.6 * DOWN)
        )
        grp.add(logs)
        self.play(Write(logs))
        self.wait(4)
        self.play(ripple(logs[:10]), run_time=1)
        self.wait(1)
        pr = (
            Text(
                "[0x00008450]>",
                font="Terminess Nerd Font Propo",
                font_size=28,
                color=YELLOW,
            )
            .to_edge(UL)
            .shift(1.5 * DOWN)
        )
        grp.add(pr)
        self.play(Write(pr))
        pdf = (
            Text(
                "pdf @ 0x000086c0",
                font="Terminess Nerd Font Propo",
                font_size=28,
            )
            .to_edge(UL)
            .shift(2.8 * RIGHT + 1.5 * DOWN)
        )
        grp.add(pdf)
        self.play(Write(pdf))
        self.wait(2)
        dump = (
            Code('pdf.c', font_size=28)[2]
            .to_edge(UL)
            .shift(2 * DOWN)
        )
        grp.add(dump)
        self.play(Write(dump))
        dump = (
            Code('pdf_cont.c', font_size=22)[2]
            .to_edge(UL)
        ).shift(12 * DOWN).set_opacity(0)
        self.play(
            grp.animate.shift(12 * UP).fade(1),
            dump.animate.shift(13 * UP).set_opacity(1)
        )
