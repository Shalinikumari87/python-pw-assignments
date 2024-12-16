"""
question:  Explain the difference between mutable and immutable data types with examples.
Answer:
        Mutuable data type: Those data type which can be changed after their creation are 
        said to be mutable data types.
                e.g. lists, dictionary

        Immutable data type: Those data type which cannot be changed after their creation are
        said to be immutable data types.
                e.g. Tuples, strings
"""
# Mutable data
l = [1,2,3,4,"apple"]
l[0] = "mango" # We can modify elements in lists
print(l)        # output will be ["mango",2,3,4,"apple"]

# Immutable data
s = "BIGBAZAR"
s[1] = 'p' # we cannot change elements in strings
print(s)  # It will throw an error