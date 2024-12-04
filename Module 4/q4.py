"""
question:Discuss the different types of operators in Python and provide examples of how they are used.
Answer:
        Opearators are special symbols that are used to perform operations or values or variables.
        Here are the differnt types of opearator:
        1.Arithmetic operators: These are used to perform basic operations like addition,
          mutiplication,subtraction and division.

        2.Comparision operator: These are used for comparing values.
        3.Logical operators: These are used to combine conditional statement and gives a 
         bool value.
        4.Assignment operators: These are used to assign a value to variables.
        5.Bitwise operator: These are used to perform operations on binary numbers.
"""


# Arithmetic operators
a = 3
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)

# Comparison operator
x= 3
y= 5
print(x>y)
print(x<y)
print(x==y)
print(x<=y)
print(x>=y)
print(x!=y)

# Logical operator
a = 2
b = 3
c = 4
d = 5
print(a<b and c>d)   #false
print(a<b or c==d)   #true

"""Insight:

In and (logical operator) as well as & (bitwise operator) operation , if the first condition is true or 1 
then it will go for second condition check , and the result depends on the seconf condition value -> if true(1) -> output true(1) , else output false(0)
Otherwise , if the first condition is false itself , then it will not go for second check and directly result false(0)
This process is known as sort-circuit

But in or as well as (|) operation , if the first condition is true , then the output wil be true,it will not check the second condition 
whereas if the first condition is false , then it will go for further check , and the output solely depends on the second condition 
if true -> true(1)
else false 
"""

# Assignment operator
n = 5
n+=2
n-=4
n/=3
n*=3


# Bitwise operator
num1 = 3
num2 =4
print(num1 & num2)   
print(num1 | num2)
print(num1 ^ num2)

