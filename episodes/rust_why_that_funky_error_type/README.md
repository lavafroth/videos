# Rust: Why that funky error type?

Now that universities are finally changing their curriculum to include languages like Rust instead of this garbage (Java), I think now is a time better than any for us to wrap our heads around some of the alien looking syntax in Rust.

So, today we're going to be tackling this expression which you might have come across as the return type of some functions, especially ones which may return multiple types of errors.

Specifically, it serves in coalescing multiple error types
into some constrained identity. But we'll get to that later. First, let's walk through the parts that make up this datatype.

A Result is an enumerable or enum type with two variants: Ok and Err. Enum variants in Rust are mutually exclusive, meaning, a function returning a Result would either be a success value wrapped in the Ok variant or a failure wrapped in an Err variant. Note that the Ok and Err variants only tell us that whatever is wrapped by them is a success or error value. To tell the compiler the concrete types for these values, the 
Result enum itself takes in the generic types T and E for the success and failure values respectively.

Now, since the success value depends upon the function's output, we leave it as a generic T for now and focus on the more hairy looking error type.

When working with different datatypes in Rust, the primitive types like bytes, integers or floating point numbers are all allocated on the stack in our computer's virtual memory. The sizes of these structures are fixed and known to the compiler. For composite types like a vector or a String, their sizes may depend upon user input, for example, and are thus not known to the compiler. These dynamically sized types are allocated
on the heap memory. Unlike the primitive types, passing them around as function arguments or return types actually translates to passing around a pointer to the memory
allocated on the heap.

Wrapping a value in a Box type, sometimes referred to simply as boxing a value, explicitly puts it on the heap. This again means we are passing around a pointer to the value in the heap.

But why does an error have to be wrapped in a Box? Doesn't the compiler already know the size of each error type? Well, yes, but the type we are specifying inside the Box is not a concrete type but more of a constraint for what can go inside the Box. Differently sized structures can be put inside the box as long as they conform to the constraint.

You see, standard error Error, is something known as a trait which defines a set of methods that a structure must implement to qualify for that trait. Here, a structure must implement the format method to qualify as an Error. This means, any arbitrary underlying type can be made an Error as long as it implements this method.

Great! We have convinced the compiler to not care about the underlying concrete type. It cat pass around a pointer to the error as long as the trait constraints are met. Except, there's a teeny tiny problem:
implementations of the format method could very well differ from structure to structure. Whereas a network error gives you details about a peer address, a logging error might tell you about the file it couldn't open. Now that the compiler has forgotten the underlying type and only cares about a pointer, it has no way to deduce the correct implementation to call for the structure at hand.

And this is where I kinda lied to you because when you're passing something that implements a trait inside a Box, you're not passing one pointer, you actually passing two. The first points to the structure allocated on the heap but the other points to a table. This table contains function pointers to the trait method implementations, specific to our struct. These tables are known as dynamic dispatch tables since they dispatch to the correct machine code that can be called on whatever object we have at hand. Speaking of objects, this structure created with the use of the dyn keyword before a name of a trait, be it a reference or a Box, is known as a trait
object or a fat pointer.

These trait objects are inherently opaque because they are raw untyped pointers. The underlying fields can't be accessed directly. One can only call the methods that they expose.

With all of this context, you should be able to explain this expression to yourself or a friend! But let's breeze through the ideas we've learned so far.

A result is an enum with two variants, Ok to wrap success values and Err to wrap, well, errors.

We use a Box to allocate memory for errors values independent of sizes as long as they implement the format method defined in the trait. These methods themselves are accessed through the dynamic dispatch table which of course leads to the struct specific machine code.

In practice, we'll often use this expression with this question mark or the try operator. This syntax sugar boils down to a match statement like this which consumes the success value if it's present or it resorts to bubbling up the error values.

Finally, there's an awesome crate known as anyhow which banks on this idea of error trait objects. It defines its own result enum that takes a generic type T for the success value but the errors are taken care of by the crate itself and we get the added benefit of being able to add contexts to errors.
