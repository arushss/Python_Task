# Section 1
def reverse(name):
    rev=''
    length=len(name)-1
    while length>=0:
        rev+=name[length]
        length-=1
    return rev
print("Enter your name")
name=input()
answer=reverse(name)
print("your reversed name is {}".format(answer))

# Section 2
upper_case=0
lower_case=0
def calculate(name):
    global upper_case, lower_case
    for i in name:
        if i.islower():
            lower_case+=1
        elif i.isupper():
            upper_case+=1

print("Enter any string")
name=input()
calculate(name)
print("No. of Upper case characters :", upper_case)
print("No. of Lower case characters :", lower_case)

# Section 3
def unique(numbers):
    return list(set(numbers))

print("Enter any numbers that might be repeated separated by commas")
numbers=input().split(',')
answer=unique(numbers)
print(answer)
print(type(answer))

# Section 4
print("Enter list of words separated by hyphen")
names=input().split("-")
names.sort()
print(names)
print("-".join(names))

# Section 5
lines=[]
print("enter sequence of lines")
while True:
    inp = input()
    if inp:
        lines.append(inp)
    else:
        break

print(lines)
for i in range(len(lines)):
    print(lines[i].capitalize())

# Section 6
def sum(a,b):
    return int(a)+int(b)

print("Enter any two numbers")
x=input()
y=input()
result=sum(x,y)
print("The resultant sum is: ", result)

# Section 7
def print_string(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    elif len(a)==len(b):
        print(a)
        print(b)

print("enter the first string")
str1=input()
print("enter the second string")
str2=input()
print_string(str1,str2)

# Section 8
def squares():
    test=[]
    for i in range(1,21,1):
        test.append(i**2)
    print(tuple(test))
squares()

# Section 9
def showNumbers(limit):
    for i in range(0,limit+1,1):
        if i%2==0:
            print(i," EVEN")
        elif i%2 !=0:
            print(i," ODD")
print("Enter any integer number")
sample=eval(input())
showNumbers(sample)

# Section 10
sample=[]
for i in range(1,21,1):
    sample.append(i)

def checker(x):
    if x%2==0:
        return True
    else:
        return False
answer = list(filter(checker,sample))
print(answer)

# Section 11
sample=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x: x%2==0,sample)
print(even)
answer=map(lambda x: x**2,list(even))
print(list(answer))

# Section 12
try:
    5/0
except ZeroDivisionError:
    print("Cant divide any number by zero")

# Section 13
from functools import reduce

def test(x1,x2):
    return x1+x2
print(reduce(test,[[1,2,3],[4,5],[6,7,8]]))
sample=reduce(test,[[1,2,3],[4,5],[6,7,8]])
print(reduce(lambda x,y: x*10+y, sample))

# Section 14
(i) 2
(ii) NameError: name 'f' is not defined