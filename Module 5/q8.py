"""
question: What is a hash table, and how does it relate to dictionaries in Python?
Answer: A hash table is a data structure that allows for efficient data storage and retrieval
        using a mechanism called hashing. It works by using a hash function to convert a key 
        into an index, where the associated value is stored.
        It relates to dictionary in many ways:

        1.Dictionary is an implementation of a hash table, where keys are hashed, and their
          associated values are stored at the index determined by the hash function.

        2.The keys in a Python dictionary are hashed. This means that a dictionary uses the
          hash value of the key to determine where to store the value associated with that key.

        3.For a key to be usable in a dictionary, it must be hashable, meaning it must have a
          consistent hash value over its lifetime. For example, immutable types like strings,
          numbers, and tuples are hashable, whereas mutable types like lists and dictionaries 
          are not.
"""