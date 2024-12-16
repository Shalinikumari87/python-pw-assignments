"""
question: Describe the time complexity of accessing elements in a dictionary?
Answer:  The time complexity of accessing elements in a dictionary depends on the underlying 
         data structure used by the dictionary. In Python, dictionaries are implemented using 
         a hash table.
         The time complexity for accessing an element by key in a dictionary is O(1) (constant time)
         This means that, on average, it takes the same amount of time to access any key,
         regardless of the size of the dictionary.

         This happens because:

       1.  Python uses a hash function to compute a hash value for the key.
       2.  The hash value determines where the key-value pair is stored in the dictionary.

"""