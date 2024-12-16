"""
question:  How does the “in” keyword work differently for lists and dictionaries?
Answer: For list "in" keyword is used to check whether the element is present in list or not
        and gives a bool vaue if it is present in list or not.

        But for dictionaries "in" is used only for searching key not the values if we search
        for values it will throw an error.
        when we use "in" in dictionaries python checks if key is there in dictionary or not 
        and gives a bool value

"""
list = [1,2,3,4,5,6]
print(2 in list) # output will be true

# 
dict = {'a': 1, 'b': 2,'c': 3 }
print('a' in dict) # output will be true

