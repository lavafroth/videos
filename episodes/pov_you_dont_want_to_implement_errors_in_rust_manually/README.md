A few moons ago, I made a video on Rust errors where I focused on using Boxed
objects implementing the Error trait. Some of you in the comments were quick
to point out that it is more utilitarian to build custom error types especially
when we're building a library to be used by downstream projects.

But what if you don't want to go through the hassle of implementing the error
trait on your types? Luckily, we can use the `Error` macro from the
`thiserror` crate to easily derive the standard Error trait on our types. Today
we'll talk about the different attributes that we can use with the macro and
for each of these, I'll also gently touch on how they work under the hood.

Before we begin, let's understand how these attributes work. Attributes can be
active or inert. During attribute processing, active attributes
remove themselves from the abstract syntax tree and transform (or expand) what
they are annotating into some other code. Inert attributes, on the other hand,
stay on the thing they're annotating.

Take the example of the active attributes `cfg`. When we annotate a block of
code with `#[cfg(target_os = "windows")]` for it to only compile for windows.
If we now compile our program for linux, the `cfg` attribute gets removed and it
transforms the code into nothing.

Take another example of the `test` attribute, which is inert when we're
compiling for tests but active otherwise. It has to stay on the test functions
when compiling for tests but it gets removed and transform the function it
annotates into nothing other times.

In our case, the only active attributes we'll talk about is this derive macro.
Apart from that, all other macros we will discuss are inert and are known
as [derive macro helper attributes](https://doc.rust-lang.org/reference/procedural-macros.html#derive-macro-helper-attributes).
They don't get removed and don't transform any code by themselves.

Thiserror comprises a single procedural macros, `Error`, glorified into a crate.
To add it to our project, we'll run the command `cargo add thiserror`.

Let's start with the most common use case where we create an enum with
each variant representing a variant of our custom error. We import the `Error`
macro from thiserror and derive it on our enum like so. We also need to derive
the Debug trait so that our error can be debug formatted with this `"{:?}"`
formatting notation.

Now, the Error trait in the standard library requires us to implement the `fmt`
method as required by the Display trait. This ensures that the error can be displayed
in a console window or a log.

To ease the implementation of the Display trait, `thiserror` supports the
`#[error()]` attribute to display an error message. We can also interpolate this
message with the inner fields of our error. For example, here's the parse error
for a config parser which only expects ascii characters. Our error variant for
reporting unexpected characters can be a tuple struct containing one character.
To report the unexpected character to the user, we can access it using a zero in
this curly braces format string. This translates to writing the `.0`th member to
the formatter.

With the use of the debug notation, we can display the debug representation of
the field. All of this formatting equally applies to named fields. For example,
if we name the character from the previous error, we can access it using its
name in the format string. The error attribute allows any additional format
arguments just like a regular call to the format macro.

Arguably the thing that annoys most Rust beginners is `std::io::Result`, you're
creating a file or perhaps reading from one and you just want to convert the
`io::Error` in the `Result` type into your custom error type.

`thiserror` makes such conversions trivial with its `#[from]` attribute.
Just create a variant in your custom error enum with an `io::Error` member and
annotate it with the `#[from]` attribute. During compilation, the macro creates
a `From` implemention for an `io::Error` for conversion `into()` your error
type.

For a better understanding, let's take a look at how the macro gets expanded
using the `cargo-expand` tool. To install it, run `cargo install cargo-expand`,
note the hyphen between cargo and expand.
Now run `cargo expand --lib` to expand your crate's library or `cargo expand --bin`
followed by a target binary if you're creating a binary.

Now, there are cases where you might want to have one catchall variant for
underlying errors you don't really care about. It would be desirable to delegate
the display methods of the variant directly to those of the underlying error.
This can be achieved by using the `#[error(transparent)]` annotation. This way,
when the errors are logged, we don't see mentions of the outer error but the
error messages directly from the inner error.

Another use case as demonstrated by the crate's documentation is when we want
to have an opaque public error type with accessors we deliberately decide to
expose publicly. The underlying error type can remain private and gives us the
flexibility to change its fields and implementations while keeping the public
API stable.

[!NOTE: DELETE REDUNDANCY FROM RECORDING]
The internal error and the public error might be displayed differently in the logs
across different minor versions of our crate. However, downstream crates will
still be able to use the publicly exposed accessors for additional checks.

Now let's get to some of the more nuanced attributes. We'll start with the
`#[source]` attribute but first let's revisit the standard error trait itself. [](assets/code/error_trait.rs)

[!NOTE: MOVE THIS AHEAD] Every error implements this set of methods; additionally, every type that
implements `Error` is required to implement `Debug` and `Display` as well.
Looking at the `source` method, we see that it returns a reference to `Some` 
underlying error if it exists or the default `None`. With the `#[source]` attribute,
we can make this method return a reference to an inner member as `Some` underlying error.

The first nuance is that using the `#[from]` attribute on a field in your error type implicitly applies the `#[source]`
attribute to it. During compilation, the `Error` macro prevents
the use of the `#[source]` attribute with multiple fields and consequently,
also prevents us from using both the `#[from]` and the `#[source]`
attributes on different fields. [](assets/code/source.rs)

The second nuance is that given your struct derives the Error trait using thiserror's
Error macro, naming a struct fields as `source` automatically annotates it with the
`#[source]` attribute. Consider this example:
[](assets/code/source_magic.rs)

We can inspect the output with a main function and we can clearly see

[](assets/code/source_magic.output.txt)

the source method call returns Some reference to an io::Error that we
simply used as the value for the source field, despite not
explicitly annotating it with the source attribute.

The last quirk that I want to address is the provide method of the error trait.
As of writing, this method is only available in Rust nightly. It provides
(no pun intended) a way to extract references to members of a dyn Error trait
object. Generally these include contextual information for error reports
like backtraces. To see backtraces, you'd typically set the RUST_BACKTRACE
environment variable to 1.

Coming back to our custom error, if a field is either annotated with the `#[backtrace]`
attribute or has the type named (Backtrace `std::backtrace::Backtrace`), the
provide method for our type yields that member as a reference.

There's a subtle difference between this and using the
`#[backtrace]` annotation in conjunction with either of `#[source]` or `#[from]`.
In such a case, the
provide method for our custom error is forwarded to that of the source so that
both layers of the error share the same backtrace.

So yeah, that is more or less how you use the `Error` derive macro from thiserror.
A big thank you to David Tolnay, the author of `thiserror`, for fact checking
the script for this video and helping me clear some of the misconceptions I
myself had regarding thiserror. I hope you have learned something along the way.
Until the next video, I'll see you around.
