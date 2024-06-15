#!/usr/bin/env manim
from manim import *
from hackermanim import *

class Sc(Scene):
    def construct(self):
        codefont="Terminess Nerd Font Propo"
        Text.set_default(font="Poppins")
        Code.set_default(font=codefont, style='monokai')

        bt= '''thread 'main' panicked at src/main.rs:16:19:
index out of bounds: the len is 3 but the index is 3
stack backtrace:
   0: rust_begin_unwind
   1: core::panicking::panic_fmt
   2: core::panicking::panic_bounds_check
   3: <usize as core::slice::index::SliceIndex<[T]>>::index
             at /build/rustc-1.77.2-src/library/core/src/slice/index.rs:255:10
   4: core::slice::index::<impl core::ops::index::Index<I> for [T]>::index
             at /build/rustc-1.77.2-src/library/core/src/slice/index.rs:18:9
   5: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
             at /build/rustc-1.77.2-src/library/alloc/src/vec/mod.rs:2771:9
   6: demo::main
             at ./src/main.rs:16:19
   7: core::ops::function::FnOnce::call_once
             at /build/rustc-1.77.2-src/library/core/src/ops/function.rs:250:5
note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.'''
        bt = Text(bt, font=codefont, font_size=24, color=RED)
        self.play(FadeIn(bt))
        self.wait(2)
        bt_ = Text("backtrace", font=codefont, font_size=40, color=WHITE)
        self.play(Transform(bt, bt_))
        self.wait(2)
