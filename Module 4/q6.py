"""
question: How do conditional statements work in Python? Illustrate with examples.
Answer:
        Conditionals helps us to code decisions based on pre conditions whether a conditional
        is true or false.
        There are three conditinals which we generally use in coding are;
       1. if statement
       2. elif statement
       3. else statement
"""
# if statement
a = 2
b = 3
if (a<b):
    print("b is largest")

# elif statement
x=3
y=6
if (x>y):
    print("x is largest")
elif(x<y):
    print("y is largest")

# else statement
bike = "honda"
if bike == "pulsar":
    print("blue")
elif bike == "suzuki":
    print("white")
else:
    print("red")
    
