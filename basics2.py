# Section 1 of Task 2 in python 
print("enter a number to test its divisibility by 3 or 5")
x=eval(input())
if(x%3==0 and x%5==0):
    print("Consultadd Python Training")
elif(x%5==0):
    print("c")
else:
    print("Consultadd")

# Section 2 of Task 2 in python
print("enter 1 for addition")
print("enter 2 for subtraction")
print("enter 3 for division")
print("enter 4 for multiplication")
print("enter 5 for average")
x=eval(input())
if(x==1):
    print("enter two numbers for addition one at a time")
    first = eval(input())
    second = eval(input())
    result = first + second
    print("final result is: ", result)
    if (result < 0):
        print("Zsa")
elif(x==2):
    print("enter two numbers for subraction one at a time")
    first = eval(input())
    second = eval(input())
    result = first - second
    print("final result is: ", result)
    if (result < 0):
        print("Zsa")
elif(x==3):
    print("enter two numbers for division one at a time")
    first = eval(input())
    second = eval(input())
    result = first / second
    print("final result is: ", result)
    if (result < 0):
        print("Zsa")
elif(x==4):
    print("enter two numbers for multiplication one at a time")
    first = eval(input())
    second = eval(input())
    result = first * second
    print("final result is: ", result)
    if (result < 0):
        print("Zsa")
elif(x==5):
    print("enter two numbers for average one at a time")
    first1 = eval(input())
    second2 = eval(input())
    result = (first1+second2)/2
    print("final result is: ", result)
    if (result < 0):
        print("Zsa")

# Section 3 of Task 2 in python
age = 38
if (age >= 11):
    print("You are eligible to see the Football match.")
    if (age <= 20 or age >= 60):
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You are not eligible to buy a ticket.")

