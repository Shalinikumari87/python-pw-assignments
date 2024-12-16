"""
question:  How do sets handle duplicate values in Python?
Answer: In Python, sets automatically handle duplicate values by removing them. A set is an
        unordered collection of unique elements, so if we add a duplicate value to a set
        it will simply be ignored. This behavior ensures that each element in a set is unique.

"""
s = {1,2,1,2,3,3,4,4} 
print(s) # output will be {1,2,3,4}

# Above in sets 1,2,3,4 is repeated but sets stores only unique value and that's why the 
# repeated no. automatically removed from sets.