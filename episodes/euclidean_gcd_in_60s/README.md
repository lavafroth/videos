Calculating the greatest common divisor or GCD of two numbers could be one of the most
important functions in cryptography and while schools have taught us how to
do this using the brute-force-esque prime factorizaion method, here's a more clever
and faster way called the Euclidean GCD.

Consider two integers a and b where a is the lesser of the two. We could divide b by
a which yields a quotient q and a remainder r. Now, we can rearrange this result as
an expression for b. b equals a times q plus r.

Assuming the gcd of a and b is some integer g, we can express a as some constant k1
times g and b as some other constant k2 times g. Subtracting q times a from both sides
we get a left hand side with a common term g, which if we factor out, tells us that
the remainder is also a multiple of g. Thus, to hone in on g, we could keep repeating
this process for b and the next remainder until the remainder becomes zero. In
that case, the last remainder was the gcd itself.

That was the Euclidean GCD algorithm in sixty seconds.
