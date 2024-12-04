"""
Question:
    Describe the role of predefined keywords in Python and provide examples of how they are used in a
    program

Answer: Prefined keywords is also known as reserved keywords that is already stored in python.
        Role of predefined keywords in python are as follows:
        1.Keywords are used to create control statements like loops and conditionals.
        2.keywords heps us to define basic operations of languages.
        3.keywords are used to define a function.

    Here are the examples of predefined keywords:
    1.(and,or) - logical operator
    2.(if,elif and else) - They are conditinals statements keywords.
    3.(while) - It is a loop.
    4.(for)- It is a loop.
    5.(break and continue)
     
    
"""
#and 
x = 5
print(x<7 and x>3)
# or
y = 6
print(y<7 or y>8)

# if,elif and else
weather = "sunny"
if weather == "rainy":
    print("stay home")
elif weather == "sunny":
    print("Go and play")
else:
    print("Do nothing")

# while,break and continue
n = 1
while n<9:
    print(n)
    if n==3:
        break
    n+=1

# continue
i = 0
while i <10:
    if i == 5:
        continue
    print(i)
    i+=1

# for
a = [1,2,3,4,5,6,7]
for i in a:
    print(i)




    



 

    


