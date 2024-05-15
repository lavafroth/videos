#!/usr/bin/env python
# coding: utf-8

from manim import *
from difflib import SequenceMatcher
from typing import List
import itertools

def tokenize(code: Code, str_tokens: List[str]) -> List[VMobjectFromSVGPath|Dot]:
    tokens = []
    lens = [len(s) for s in str_tokens]
    ctr = 0
    for line in code[2]: # 0 = frame, 1 = dot, 2 = paragraph
        current_vmobject_group = []
        for vmobject in line:
            head = lens[0]

            if isinstance(vmobject, Dot):
                continue

            ctr += 1
            if ctr == head + 1 and len(current_vmobject_group) > 0:
                tokens.append(VGroup(*current_vmobject_group))
                if len(lens) > 1:
                    lens = lens[1:]
                else:
                    lens = []

                ctr = 1
                current_vmobject_group = []

            current_vmobject_group.append(vmobject)
            
        if len(current_vmobject_group) > 0:
            tokens.append(VGroup(*current_vmobject_group))
    return tokens


# In[9]:


def rewrites(code, replacement, initial_tokens, final_tokens):
    sequence_matcher = SequenceMatcher(None, initial_tokens, final_tokens)
    opcodes = list(sequence_matcher.get_opcodes())

    unwrites = []
    for op, i0, i1, j0, j1 in opcodes:
        if op == 'delete' or op == 'replace':
            for x in range(i0, i1):
                unwrites.append(Unwrite(code[x]))
    
    unwrites = AnimationGroup(*unwrites)

    transforms = []
    for op, i0, i1, j0, j1 in opcodes:
        if op == 'equal':
            for x, y in zip(range(i0, i1), range(j0, j1)):
                transforms.append(Transform(code[x], replacement[y]))

    transforms = AnimationGroup(*transforms)

    writes = []
    for op, i0, i1, j0, j1 in opcodes:
        if op == 'insert' or op == 'replace':
            for x in range(j0, j1):
                writes.append(Write(replacement[x]))

    writes = AnimationGroup(*writes, lag_ratio=0.30)

    for op, i0, i1, j0, j1 in opcodes:
        if op == 'insert' or op == 'replace':
            for x in range(j0, j1):
                code[x] = replacement[x]

    return unwrites, transforms, writes


# In[ ]:


class Intro(Scene):
    def construct(self):
        dead_cells = SVGMobject("cloud", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        self.play(Write(dead_cells))
        self.wait(3)
        self.play(dead_cells.animate.shift(2 * LEFT))

        archlinux = SVGMobject("container", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        archlinux.shift(2 * RIGHT)
        self.play(Write(archlinux))

        self.wait(4)

        dead_cells_ = dead_cells.copy()
        dead_cells_.shift(2 * LEFT)
        dead_cells_.set_opacity(0)

        archlinux_ = archlinux.copy()
        archlinux_.shift(2 * LEFT)
        archlinux_.scale(1.2)
        
        self.play(AnimationGroup(
            Transform(dead_cells, dead_cells_),
            Transform(archlinux, archlinux_)
        ))

        self.play(archlinux.animate.shift(LEFT * 3.5))

        linux = SVGMobject("linux", fill_color=BLUE, stroke_color=BLUE, fill_opacity=0.6)
        linux.shift(3.5 * RIGHT)

        arrow = Arrow(start=archlinux.get_center() + 1.5 * RIGHT, end=linux.get_center() + 0.75 * LEFT)

        self.play(
            AnimationGroup(
                FadeIn(linux),
                FadeIn(arrow),
            ),
        )

        self.wait(4)

        unshare_calls = [
            ["unshare(", "...", ")"],
            ["unshare(", "CLONE_NEWNS", ")"],
            ["unshare(", "CLONE_NEWPID", ")"],
            ["unshare(", "CLONE_NEWNET", ")"],
            ["unshare(", "CLONE_NEWUTS", ")"],
            ["unshare(", "CLONE_NEWIPC", ")"],
        ]

        namespaces = (
            "mount",
            "process ID",
            "network",
            "hostname",
            "   interprocess\ncommunication",
        )

        namespaces = list(Text(text, font_size=28) for text in namespaces)
        for namespace in namespaces:
            namespace.shift(0.3 * DOWN + 0.25 * RIGHT)
        namespaces[-1].shift(0.2 * DOWN)
        
        unshare_code = [
            (Code(code="".join(initial_tokens), language="C", insert_line_no=False), initial_tokens)
            for initial_tokens in unshare_calls
        ]
        for code, _ in unshare_code:
            code.shift(0.3 * UP + 0.25 * RIGHT)

        unshare_code = [
            (tokenize(code, initial_code), initial_code)
            for code, initial_code in unshare_code
        ]
        
        for thing in unshare_code[0][0]:
            self.play(Write(thing))

        for x in range(1, len(unshare_code)):
            code, initial_tokens = unshare_code[0]
            replacement, final_tokens = unshare_code[x]
            unwrites, transforms, writes = rewrites(code, replacement, initial_tokens, final_tokens)
            if x - 2 > -1:
                unwrites = AnimationGroup(unwrites, Unwrite(namespaces[x-2]))
            self.play(unwrites)
            self.play(transforms)
            writes = AnimationGroup(writes, Write(namespaces[x-1]))
            self.play(writes)
            self.wait()

        self.wait(4)
