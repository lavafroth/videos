Introduction


“I have a friend that enjoys coding and he hasn't stopped talking about a snake recently. He left this file on my computer and dares me to uncover a secret phrase from it. Can you assist?”


At least, that's what is the description for a capture the flag challenge we're going to work through today.


My recent poll on the channel's community page where I asked you about the kind of videos you want to watch had CTFs in the lead for the first few days. So, I started working on the script of this video but not long after, the results of the poll sided with explainers on programming patterns.


Since I had already started working on this video, I chose to continue with the video at hand instead of course correcting. So please bear with me, programming related videos are on their way.


With that out of the way, today we'll begin with a rather easy challenge from PicoCTF called "Weird Snake" which should explain what I said in the beginning of the video. For those of you unaware of PicoCTF, it's a "Capture the Flag" platform hosted by Carnegie Mellon University, and it's completely free for you to register and practice their challenges.


The challenge has a text file attached. Opening it reveals these long columns of what seem to be assembly-like instructions. I say assembly-like because these aren't opcode mnemonics that you'd find in a real instruction set like ARM, x86 or RISC-V.


Scrolling down to the paragraph marked 9, we observe that the LOAD_CONST instruction is followed by a line saying code object listcomp from file snake dot py. This is a dead giveaway that the challenge has something to do with a python source file. The listcomp makes sense as it stands for "list comprehension" in this context. We'll get to this but even if there was no dead giveaway of being related to python, we could try looking up one or more of these instructions.


This would lead us to the page for `dis`, the Python bytecode disassembler which provides a helpful description for what each instruction does. Let's try to build an intuition for this Python bytecode idea from the ground up. So Python, or more precisely CPython runs a python script by compiling it into bytecode and running it in a virtual machine. Ever noticed that weird looking "__pycache__" directory when running python scripts? That's where the compiled bytecode gets stored as ".pyc" files. We can also manually compile our python files into these ".pyc" files.


That said, we must not confuse this virtual machine with solutions like KVM+libvirt or VirtualBox. This python virtual machine is a simple stack machine that executes the bytecode instructions one by one, pushing and popping values on a stack as needed to perform these operations.


While it is possible to use the dis module to show the textual disassembly of such bytecode or a source file, the disassembly is only meant for human consumption and can't be converted back into code mechanically. There are tools like python-xasm that attempt to solve this but we have to pass in metadata like the current state of the stack, the constants, etc. to get it working.


Unfortunately, we have to go the manual route to make sense of these instructions.


Reverse Engineering


Let's start with the first block comprising a bunch of LOAD_CONST opcodes. The load const operation indexes into the constants baked into the output bytecode and pushes the retrieved value onto the stack. Although this list of baked in constants, known as co_consts, is not directly available in the disassembly, each line ends with a handy representation in parentheses of what's being operated on.


Thus, we can deduce that the first instruction loads the zeroth constant from co_consts, which happens to be the number 4, and pushes it onto the stack.


The program continues this process of loading constants onto the stack for 40 elements in total. This is followed by a BUILD_LIST operation with the operand 40. This instructs the virtual machine to take these 40 elements we just pushed onto the stack, wrapping them in a list and pushing it back onto the stack.


The STORE_NAME instruction subsequently stores the list away with the name input_list. Storing a value in a variable pops the value off the stack and binds it with the variable name.


Next up, the disassembly loads the string 'J' as a constant and stores it as the variable key_str. Remember, the STORE_NAME instruction stores variables away but right after loading the underscore character, the value of the key_str is loaded back on the stack.


With these two strings on the stack, we perform the `BINARY_ADD` operation. Now, the order of binary operations is to first use the lower value and then the upper value on the stack. As an aside, the order of operands and operators here would represent a post order traversal in terms of a binary tree. This is especially important with the string type since addition means concatenating two strings and reversing the order yields a different string altogether.


We see a similar pattern right in the next block except that the order of loading the strings is switched  up, meaning, instead of prepending characters, we'll append to the `key_str`. Similar string additions go on for the next 3 blocks, two appends and one prepend.


Next we see the VM load a code object from another address and the string listcomp. With the `MAKE_FUNCTION` instruction, the code object is bound to the name `listcomp` and the newly created function is pushed onto the stack. The name `listcomp` suggests that this is a list comprehension.


We then load the value of the `key_str` variable to grab an iterator that sequentially yields each character in the string. With the function and the iterator on the top of the stack, the subsequent `CALL_FUNCTION` instruction, well, calls the function passing the iterator as the argument.


Let's examine what the function does. Going down the disassembly, we'll find that these code objects are disassembled separately in their own sections. We'll check out the disassembly section corresponding to line 9. The section starts out by building a list. It then loads an identifier named dot zero (`.0`) onto the stack. Now, under normal circumstances, variable names beginning with dots are forbidden in python. The exception being when the bytecode represents function arguments. In the bytecode representation, each regular argument is named a dot followed by the index of the argument. Meaning, the first argument is named dot zero, the second as dot one and so on.


Here, we are loading the first argument onto the stack. With the for iter instruction, each element yielded by the iterator is pushed onto the stack, some operation is performed on it and it's popped off the stack. The operations performed in the loop body are demarcated both using the text saying "to 18" in parentheses as well as the two closing angle brackets that serve as visual cues.


Inside the loop body, the current element is popped off the stack and stored as the variable `char`. We then load the global function `ord` onto the stack and load back the value of the `char` variable so as to feed it as an argument to the ord function. The ord function converts the text into the corresponding unicode code point.


We then append this number to the list we had built earlier. Not that the number 2 denotes the stack element at index 2. The jump absolute instruction jumps back to the for iter instruction to repeat this process for the remaining characters.


Okay, going back to the main listing, we see the list created by the list comprehension is stored away as `key_list`.


The next section concerns some sort of comparison. Let's see, the `len` or the length function in python is loaded, and it gets called with `key_list` as the argument. This pushes the length of the `key_list` variable on the stack. Similarly, we find the length of the `input_list`. With both of these lengths on the stack, we perform a compare operation which checks if the first operand is less than the second. If true, we continue to the next section. Otherwise, we jump to a distant instruction at byte 162 as inferred from the `POP_JUMP_IF_FALSE` instruction.


To cover all grounds, let's continue down the happy path to the next section. Now here, after loading the key_list variable, instead of loading a global function or a code object, we load the `extend` method associated with the list object. In python, the extend function requires an iterable argument and for that, we again load the `key_list` onto the stack. Then we call the method and the None value returned is discarded using the `POP_TOP` instruction. The loop continues with a jump back to byte 134.


Moving on, we come across another list comprehension. We'll examine its disassembly but before that, let's see what arguments it accepts. After loading the list comprehension on the stack, the bytecode loads the `zip` function, the input list and key list respectively. The `zip` function, when called [highlight the `CALL_FUNCTION` instr], produces an iterator object that picks one element from each list and yields a pair every iteration. The following instruction pushes this iterator from the `zip` object on the stack and calls the function. Which function, you might ask? The list comprehension we mentioned earlier.


Let's now dive into the disassembly of this second list comprehension. As usual, we build a list that will store the resultant values, load the zeroth argument on the stack and start a loop. Now remember how the `FOR_ITER` instruction pushes the next element from the iterator on the stack? The subsequent `UNPACK_SEQUENCE` unpacks it into some number of individual elements, right to left, and pushes those individually on the stack. Here, the bytecode instructs the VM to unpack the sequence into two elements, stored as variables `a` and `b` respectively. 


After loading the values that we just stored as variables, we perform a binary XOR on them. A binary XOR, otherwise known as an exclusive or is an involuntary function which in its simplest form, takes two bits and outputs a boolean true value when both of them are different and false otherwise.


Since we're working with numbers, recall that we used the `ord` function on the characters, the xor operates on each pair of bits in the binary representation of the numbers. The number resulting from the XOR operation is then appended to the final list which in turn gets returned to the main disassembly section.


Back there, the result is stored in the variable named `result`.


In the final section, the bytecode loads an empty string and its join method. We then load the `map` function, the `chr` function and the `result` list and call the function. Now, this might seem a bit complicated and difficult to take in at once. Let's break it down and use contextual cues. First, we're using a `CALL_FUNCTION`, which is different from `CALL_METHOD` that would be used for the join. To figure out which function we are calling, we'll look at the number next to the instruction, 2. So, we're calling the function at index 2 of the stack, which happens to be `map`. The arguments to it will be what's left above it.


In python, the map function takes a function and an iterable as arguments. Here they are `chr` and `result` respectively. What comes out the other end is an iterator that yields each object in the iterable with the function applied to it.


In our case, the iterator applies `chr` on each number in the `result` list to convert it back into a character. Finally, with this iterator on the stack, we come across the `CALL_METHOD` instruction that calls the join _method_. The join method simply joins the characters or strings in a list with the original string as the delimiter. However, since our original string is empty, we just join all the characters back to back.


This final string is then stored as the variable `result_text` and the program ends. No, really, the program ends.


Reconstruction


Obviously, from what we can infer, it seems to be that the `result_text` is what we need to figure out as the flag for this challenge. So, we'll take another run through the main ideas and recreate the script.


First, create a list of these numbers. Name it input list. Next, initialize a variable `key_str` with the string 'J'. Prepend an underscore, append an 'o' and a '3', and finally prepend a 't'.


Create a list comprehension for each character `char` in `key_str` and apply the `ord` function on it. Store the result in `key_list`. Great!


Now, while the `key_list` is smaller than the input list, extend the `key_list` with its own elements. Essentially duplicating the list onto itself.


Once we're done with that, we zip the input and the key lists and create a list comprehension where for each pair `a` and `b`, we calculate their binary xor. This gets stored in a variable called `result`.


Lastly, we map each number in the `result` with the `chr` function, join them back to back with an empty string '' and we're done!


The only thing we'd do in addition to all of this is print the resulting text to actually see the fruits of our labor.


Footnotes


1. Forbidden names in listcomp: https://stackoverflow.com/questions/60809021/why-does-python-use-0-to-represent-an-iterator-in-disassembled-byte-code
2. Dis manual: https://docs.python.org/3/library/dis.html