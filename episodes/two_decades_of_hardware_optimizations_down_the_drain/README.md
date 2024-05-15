This video is based on the blog post "'Clean' Code, Horrible Performance" by
Chris. The link to the original post will be in the video description.

Clean code, for the longest time has been a concept that has been peddled
by schools, universitites and everything in between. It is an idea coined by
Robert C Martin also known as "Uncle Bob" which incentivises creating layers of
abstraction to make it "readable", "understandable" and "maintainable". Today
we'll be focusing on debunking some of the design principles laid out by this
philosophy by starting with a program implemented the "cleanest" way and slowly
breaking the rules to restructure the code, making it easier to understand from
the computer's perspective.

In a surprising turn of events, we'll find the compiler being able to pick up
certain patterns and make the resulting binary even faster.

To do justice to "clean code," we write the Rust version of the very sample that
"clean code" proponets use in their examples. This code creates structures for
different shapes and a trait, also known as an interface in other languages, to
calculate the area of any Shape object. It follows the clean code preference of
polymorphism where subclasses with shared behavior are preferred to branching
conditionals like if-else or match statements. Here the subclasses are the shape
structures like square, circle, etc. and the shared behavior is the area method
defined on them by the Shape trait.

To benchmark the code, we'll be using the bench macro in Rust nightly.
Our benchmark is going to be incredibly simple, we create a list of 10240
shape objects and for each of those, we calculate the area and add it to an
accumulator.

Running this benchmark gives us the baseline of 54956 nanoseconds per iteration.

Our friend Chris here, found out that we can improve upon this baseline with relative
ease by modifying the code that performs the benchmark. Instead of using a single accumulator,
we switch to using 4 accumulators and adding them up after all the iterations.

This results in a performance improvement from the baseline by 3.1 times to
17,725 nanoseconds per iteration.

What sort of black magic is this? We'll get to this in a while but for now, know
that it's related to horizontal scaling with regards to the CPU.

Due to the inherent nature of how polymorphism works, we are constrained to
using this Box dyn syntax. I have covered how boxing values work in a previous
video but the gist of it is that these Boxed objects are called trait objects
or fat pointers. They have a raw untyped pointer that points to the underlying
structure on the heap and another pointer pointing to the virtual dispatch table
mapping the trait methods to machine code.

Obviously this presents us with two layers of indirection to perform the lazy
call to the `area` method. First we have to jump to the virtual dispatch table
or vtable from the pointer in the trait object, then we have to follow the
pointer in the vtable to reach the struct specific machine code.

Let's break the rule of preferring polymorphic code and replace the trait
with a simple yet idiomatic usage of enums and match statements. This type of
conditional matching is prevalent of Rust code you might come across with the
only downside being if our code is a library. In that case, dependents of said
library would not be able to implement the Shape trait on their custom types
like a hexagon.

This design change shows a whopping 3.2 times perforance improvement from the
baseline to 17141 ns/iter. If we split the task among 4 accumulators as we did
before, we get a massive 8.5 times improvement to 6434 ns/iter.

As Chris points out, the performance gains here come indeed from the removal
of the Box construct. With the shapes now being represented as enum variants
instead of trait implementors, the compiler knows the size of each element in
the vector. It no longer needs to create a trait object and follow two levels of
indirection during runtime.

Let's crank this up a notch by using a lookup table like construct where the
shape structure itself holds the width and height as well as a multiplier for a
specific shape type. The concrete shapes are defined as the variants of an enum
type. The constructor for the shape type ingests these variants and chooses a
multiplier accordingly. For example, it would choose 1 for a square, pi for a
circle and so on.

Nonetheless, it's not too different from the previous iterations, except for
when it comes to speed. This code is 6.4 times faster than the baseline and
applying the 4 accumulators trick on top of it yields a program that's 11 times
faster!

Okay. Time to address the elephant in the room. What's so special about
splitting up the accumulator into 4 independent ones and then adding them up in
the end. To investigate, we will look at the test binaries under a decompiler.
This will allow us to see the exact machine instructions the compiler generates
from our code.

I'll be using radare2 on a x86_64 machine, if you're following along on a
different architecture, you mileage may vary. We run the mnemonic `aaa` to
analyze all functions. Now that the functions are analyzed, we can proceed to
list all the functions to find the address of the main function.

We will do so using the `afl` menmonic that stands for analyse function list and
pipe the output to ripgrep to search for main. Okay so we notice that the main
function is located at the address hex 000086c0.

Now we will print the disassembly of the function using the `pdf` mnemonic.
print disassembly of the function at hex 000086c0. Here, we can notice memory
allocations for the initial vectors. The eagle eyed viewers among you might have
noticed the while loop right between the physical addresses hex 000088e0 and
hex 00008974. It's also conveniently represented by the dotted line.

We can notice it performing a conditional jump after comparing the rcx register
with hex 2803 which translates to 10243. This seems close to our total object
count but why the extra three? Well, because the compiler assigned 3 to the
lower half of the register and started counting backwards when indexing the
shape vector [at address 0x000088c9]. The compiler is way smarter than you and I.

The real magic is what happens inside the loop. If you've reverse engineered
software before, you might have noticed that instead of the move (`mov`), add
or multiply (`mul`) instructions, what we have here are `movss`, `addss` and
`mulss` operations on weird looking registers starting with `xmm`.

Turns out these instructions and registers are a part of the streaming SIMD
extensions introduced by Intel in their CPUs about two decades ago. What
is SIMD? It stands for `single instruction multiple data`. These operations
perform a the same operation on multiple operands. For example, the highlighted instructions
merge the multipliers for the 4 current shapes. Each value is
represented by a single precision 32 bit floating point number, into giant 128 bit `xmm`
registers.

The same happens with the move instructions for the widths and heights. Finally,
these gaint registers are multiplied with one another to calculate the areas of
the shapes. The takeaway from all of this is that multiplying 4 of these numbers
in parallel using SSE takes the same time as performing one of the multiplications
using regular instructions from the instruction set.

The portable-simd documentation for rust states that SSE is enabled by default
for `x86_64` targets. Rightfully so, it makes a lot of sense considering it was
introduced two decades ago. Practically, every desktop computer in use has this
functionality built right into it! There have also been more recent improvements
in SIMD extensions such as Advanced Vector Extensions, AVX and AVX-512.
Obviously, we can't assume that all machines sport these extensions and being
less mindful when enabling extensions can make our binaries less portable.

As for ARM CPUs, we only have to enable one extension called NEON to have SIMD
but this is not enabled by default.

How does clean code fit into this picture? It doesn't. In fact, the implicit
use of SIMD with the clean code version still had to go through the layers of
abstractions instead of being able to directly access the floating point numbers.

The separation of concerns can still be achieved by moving code related to a
specific functionality into its own module. The ungodly powerful idea of namespacing can
promote separation of concerns while preserving locality of behavior.

All of this is not aimed to be a dunk on uncle bob. I think he has some great insights.
You might want to watch him getting interviewed by your local Vim enthusiast.

That's all for now, I hope you learned something. As usual, sources and the
code to render these animations will be linked in the description. Thank you
Chris for letting me make a video based on your blog. Until then, I will see
you around!
