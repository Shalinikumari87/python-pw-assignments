"""
question: Can you modify the elements of a tuple? Explain why or why not?
Answer: No, we cannot modify elements in a tuple in Python. This is because tuples are immutable,
        meaning their content cannot be changed after they are created.
        because Tuples do not support item assignment. Since they are immutable if we make an attempt
        change an element throw an error.

"""
tup = (1,2,3,4,5)
tup[1] = 8 # we can't change elements
print(tup) # It will throw an error
