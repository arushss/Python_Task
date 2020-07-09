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

# Section 4 of Task 2 in python
#Write a program in Python to break and continue if the following cases occur:
#If a user enters a negative number just break the loop and print “It’s Over”
#If a user enters a positive number just continue in the loop and print “Good Going”

while True:
    print("Enter any number")
    x=eval(input())
    if(x<0):
        print("It's Over")
        break
    print("Good Going")
    continue

# Section 5 of Task 2 in python
#Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200.

x=2000
while x<=3200:
    if(x%7==0 and x%5!=0):
        print(x)
    x+=1

# Section 6 of Task 2 in python
# What is the output of the following code examples?
x=123 
for i in x:
    print(i)
# Answer TypeError: int object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")

#Answer
#0
#1
#2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
#Answer Break is not defined

# Section 7 of Task 2 in python
# Write a program that prints all the numbers from 0 to 6 except 3 and 6.
i=0
while i<7:
    print(i)
    i+=1
    if(i==3 or i==6):
        i+=1
        continue

# Section 8 of Task 2 in python
# Write a program that accepts a string as an input from the user and calculates the number of digits and letters.

print("please enter any string that may include digits and letters")
str=input()
digits=letters=0
for i in str:
    if i.isdigit():
        digits+=1
    if i.isalpha():
        letters+=1


print("The number of digits are {}".format(digits))
print("The number of letters are {}".format(letters))

# Section 9 of Task 2 in python
# Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
lucky_number = 5
while True:
    print("write the lucky number")
    x=eval(input())
    if x==lucky_number:
        break
    print("keep guessing")

# Second part of the same question
lucky_number = 5
while True:
    print("write the lucky number")
    number=eval(input())
    if number==lucky_number:
        print("you have guessed right")
        break
    print("Would you like to continue guessing? Enter yes or no")
    answer=input()
    if(answer=='no'):
        break
    else:
        continue

# Section 10 of Task 2 in Python
lucky_number=5
counter=1
while counter<=5:
    print("guess the lucky number")
    x=eval(input())
    if x==lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
    counter+=1
print("Game over!")

# Section 11 of Task 2 in Python

lucky_number=5
counter=1
while counter<=5:
    print("guess the lucky number")
    x=eval(input())
    if x==lucky_number:
        print("Good guess!")
        break
    else:
        if counter<5:
            print("Try again!")
    counter+=1
if counter==6:
    print("Sorry but that was not very successful")
