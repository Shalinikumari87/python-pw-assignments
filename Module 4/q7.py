"""
question: Describe the different types of loops in Python and their use cases with examples.

Answer:
        Loops are used to do a task repeatedly.
        Here are the different types of loops are:
      1.While loop: It repeatedly executes a block untill a condition is met.
                    When we are not sure about number of iterations, then we usually prefer while loop over for loop
                    e.g. do sum of natural numbers and break when sum is 99999 , so here number of iterations is not predetermined, and swe are doing repeative task of
                        doing the addition , thats why while loop is preferable here
                    
      2.For loop: It iterates the elements in sequencial order and where we know that how many iteratoions will be . 
                    Although what things we can do via for loop is also doable via while loop 
                    e.g. print first 10 natural numbers, here number of iterations = 10
      3.Nested loop: It exists inside the body of another loop.
"""
# while loop
a = 1
while a<=5:
    print(a)
    a+=1

# for loop
x = [4,5,6,7,8,9]
for i in x:
    print(i)

# nested loop
m = [1,2]
n = [4,5]
for i in m:
    for i in n:
        print(m,n)

