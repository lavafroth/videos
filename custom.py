from manim import VMobject, Code, VGroup, AnimationGroup, Write, Transform, Unwrite, SVGMobject
from dataclasses import dataclass
from typing import Optional, List, Any
from difflib import SequenceMatcher

@dataclass
class CodeVMobjectPair:
    char: str # char but there's no way to express one in Python
    vmobject: Optional[VMobject]

@dataclass
class RawCodeToVMobjectMapper:
    pairs: List[CodeVMobjectPair]
    
    def __init__(self, raw: str, **kwargs):
        code = Code(code=raw, **kwargs)
        all_vmobjects = []
        for line in code[2]:
            for vmobject in line:
                all_vmobjects.append(vmobject)

        pairs = []

        # pointers to the start of each stack
        i, j = 0, 0
        while i < len(raw) and j < len(all_vmobjects):
            if raw[i] == '\n':
                i += 1
                pairs.append(CodeVMobjectPair(raw[i], None))

            pairs.append(CodeVMobjectPair(raw[i], all_vmobjects[j]))
            i += 1
            j += 1
        
        self.pairs = pairs

    def into_chunks(self, breakpoints: Optional[List[int]] = None) -> 'CodeVMobjectChunks':
        chunks = []
        chunk = []
        token = ""
        breakpoints = breakpoints or [i for i, pair in enumerate(self.pairs) if pair.char.isspace()]
        
        for i, pair in enumerate(self.pairs):
            if i in breakpoints:
                if len(chunk) > 0:
                    chunks.append(CodeVMobjectChunk(token, VGroup(*chunk)))
                    chunk.clear()
                    token = ""
                    
            if pair.vmobject is not None:
                token += pair.char
                chunk.append(pair.vmobject)

        if len(chunk) > 0:
            chunks.append(CodeVMobjectChunk(token, VGroup(*chunk)))

        return CodeVMobjectChunks(chunks)

@dataclass
class CodeVMobjectChunk:
    token: str
    chunk: VGroup

@dataclass
class CodeVMobjectChunks:
    chunks: List[CodeVMobjectChunk]

    def tokens(self) -> List[str]:
        return [chunk.token for chunk in self.chunks]


@dataclass
class CodeTransformer:
    start: CodeVMobjectChunks
    end:   CodeVMobjectChunks
    diffs: List[Any]
    lag_ratio: float
    
    def __init__(
        self,
        start: str,
        end: str,
        start_breakpoints: Optional[List[int]] = None,
        end_breakpoints: Optional[List[int]] = None,
        lag_ratio: float = 0.3,
        **kwargs
    ):
        self.start = RawCodeToVMobjectMapper(start, **kwargs).into_chunks(start_breakpoints)
        self.end = RawCodeToVMobjectMapper(end, **kwargs).into_chunks(end_breakpoints)
        sequence_matcher = SequenceMatcher(None, self.start.tokens(), self.end.tokens())
        self.diffs = list(sequence_matcher.get_opcodes())
        self.lag_ratio = lag_ratio

    def writes(self) -> AnimationGroup:
        return AnimationGroup([Write(chunk.chunk) for chunk in self.start.chunks], lag_ratio=self.lag_ratio)

    def unwrites(self) -> AnimationGroup:
        unwrites = []
        for op, i0, i1, _, _ in self.diffs:
            if op == 'delete' or op == 'replace':
                for x in range(i0, i1):
                    unwrites.append(Unwrite(self.start.chunks[x].chunk))
        return AnimationGroup(unwrites, lag_ratio=self.lag_ratio)

    def transforms(self) -> AnimationGroup:
        transforms = []
        for op, i0, i1, j0, j1 in self.diffs:
            if op == 'equal':
                for x, y in zip(range(i0, i1), range(j0, j1)):
                    transforms.append(Transform(self.start.chunks[x].chunk, self.end.chunks[y].chunk))

        return AnimationGroup(transforms)

    def rewrites(self) -> AnimationGroup:
        writes = []
        for op, _, _, j0, j1 in self.diffs:
            if op == 'insert' or op == 'replace':
                for x in range(j0, j1):
                    writes.append(Write(self.end.chunks[x].chunk))

    def rewrites(self) -> AnimationGroup:
        return AnimationGroup(
            (Write(x) for x in self.rewritables()),
            lag_ratio=self.lag_ratio
        )

    def ingest(self, end: Union[str, Code], breakpoints: Optional[List[int]] = None, **kwargs):
        self.start = self.post
        if isinstance(end, Code):
            self.end = CodeToVMobjectMapper(end).into_chunks(breakpoints)
        else:
            self.end = RawToVMobjectMapper(end, **kwargs).into_chunks(breakpoints)  
        
        sequence_matcher = SequenceMatcher(None, self.start.tokens(), self.end.tokens())
        self.diffs = list(sequence_matcher.get_opcodes())
        self.post = copy(self.end)
        self._committed_transformation = False


def octicon(name: str, *args, **kwargs) -> SVGMobject:
    from os import path
    return SVGMobject(path.join(path.dirname(__file__), 'octicons', 'icons', name), *args, **kwargs)
