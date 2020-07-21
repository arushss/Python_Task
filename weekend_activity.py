#Section 1
x=["consultadd",10,20,3.14,9.8,5+4j,4+6j,88,5.42,"python"]

# Section 2
x=["consultadd"]
x*=5
print(x)

# Section 3
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#Access list [1, 2, 3, 4]
print(x[5][:4])
#Access list [600, 700]
print(x[6:8])
#Access list [100, 300, 500, 600, 800]
print(x[::2])
#Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])
#Access list [10]
print(x[5][5][:1])
#Access list [ ]
print(x[9:])

# Section 4
b=list(range(1,1000))
b=list(xrange(1,1000))
# Return type of range is list whereas return type of xrange is xrange object
# range occupies more size compared to xrange hence xrange is faster to implement

# Section 5
# Since tuples are immutable type compared to lists, they can be used as a dictionary in various applications.

# Section 6
for i in range(1,100):
    if i%6==0:
        print(i)

# Section 7
print("Enter any string")
name=input()
reverse=""
print("The original string is {}".format(name))
length=len(name)
i=length-1
while i>=0:
    reverse+=name[i]
    i-=1
print("Printing only the vowel alphabet in reversed string")
for position,i in enumerate(reverse):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
        print(i,"found at index:", position)

# Section 8
string = "hello my name is Abcde"
input=[]
input.extend(string.split())
print(input)
for i in range(len(input)):
    if len(input[i]) % 2 == 0:
        print(input[i])

# Section 9
x=[1,2,3,4,5,6,7,8,9,-1]
for i in x:
    for j in x:
        if i+j==8:
            print("the pair of numbers are: {} {}".format(i,j))

# Section 10
even_list=[]
odd_list=[]
print("Enter the number in the range of 1 to 50")
x=eval(input())
while len(even_list) <= 5 and len(odd_list) <= 5:
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)
    x=eval(input())
print("Sum of even lists are: ", sum(even_list), "and a max value is: ", max(even_list))
print("Sum of odd lists are: ", sum(odd_list), "and a max value is: ", max(odd_list))     

# Section 11
dictionary={}
print("Enter any random string")
name=input()
for i in range(len(name)):
    if name[i].isdigit():
        continue
    if name[i] in dictionary:
        dictionary[name[i]] +=1
    else:
        dictionary[name[i]] = 1
print(dictionary)

# Section 12
x=(1,2,3,4,5,6,7,8,9,10)
y=[]
for i in x:
    if i%2==0:
        y.append(i)
answer=tuple(y)
print(answer)