#!/usr/bin/env python
# coding: utf-8

from manim import *
from hackermanim import *
from typing import List

def whitespace_indices(s: str) -> List[int]:
    return [i for i, c in enumerate(s) if c.isspace()]

class OpeningScene(Scene):
    def construct(self):
        code = "Result<T, Box<dyn std::error::Error>>"
        splits = [len('Result<'), len('Result<T'), len('Result<T, Box<dyn std::error::Error>')] + whitespace_indices(code)
        tfmr = CodeTransformer(code, splits, language='rust')
        
        code = """fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file = std::fs::File::open("meaning_of_life.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let number: u16 = contents.parse()?;
    println!("{}", number + 27);
}"""
        
        splits = [
            len('fn main() -> '),
            len('fn main() -> Result<'),
            len('fn main() -> Result<()'),
            len('fn main() -> Result<(), Box<dyn std::error::Error>')
         ] + whitespace_indices(code)
        
        tfmr.ingest(code, splits, language='rust')
        self.play(tfmr.writes())
        self.wait(2)
        self.play(tfmr.unwrites())
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        self.wait(4)
        
        code = "Result<T, E>"
        splits = [len('Result<'), len('Result<T'),len('Result<T, E')] + whitespace_indices(code)
        tfmr.ingest(code, splits, language='rust')
        
        self.play(FadeOut(x) for x in tfmr.unwritables())
        self.play(tfmr.transforms())
        self.play(tfmr.rewrites())
        self.wait(2)

        # A little hack: set the old chunks to invisible ...
        for chunk in tfmr.post.chunks:
            chunk.chunk.set_opacity(0)
        code = Code(code=code, language='rust')[2]
        # ... and add the unprocessed code object
        # classic switcheroo
        self.add(code)
        _code = code.copy().shift(3 * UP).scale(1.5)
        self.play(Transform(code, _code))
        self.wait(3)
        text = Text("enumerable", font_size=50)
        _text = Text("enum", font_size=50, font='monospace')
        self.play(Write(text))
        self.wait(2)
        tfm = AnimationGroup(FadeOut(text[4:]), Transform(text[:4], _text))
        self.play(tfm)
        self.wait(4)
