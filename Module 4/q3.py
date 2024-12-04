"""
Question: Compare and contrast mutable and immutable objects in Python with examples.

Answer:
        Mutuable objects - Those objects which we can change after they are created are 
                            said as mutuable objects.
                                    e.g.- Lists

        Immutable objects - Those objects which we cannot change after they are created are
                            said as immutable objects.
                                    e.g.-Strings

"""
# Mutuable
list = [1,2,3,4,5]
list[2] = 8
print(list)      #[1,2,3,4,5,8]

# Immutable
str = "helen"
str[1]='p'
print(str)     # It will throw an error





