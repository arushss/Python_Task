# Section 1 of Task 3 in Python

test=[3,10,"august",2+5j,3.14,4.13,"python",78,45,"arush"]
print("The {} contents of list are {}".format(len(test),test))

# Section 2 of Task 3 in Python
test=["Python", "is", "fun", "to", "learn"]
print(test[2:])
print(test[:])
print(test[1:])
print(test[:3])

# Section 3 of Task 3 in Python
test=[10,20,30,40,50,60,70,80,90,100]
sum=0
multiply=1
for i in test:
    sum+=i
    multiply*=i
print("sum of all elements are {}".format(sum))
print("product of all elements are {}".format(multiply))

# Section 4 of Task 3 in Python
test=[10,20,30,40,50,60,70,80,90,100]
print(min(test))
print(max(test))

# Section 5 of Task 3 in Python
random=[34,65,3423,45,88,32,5467,53,6,788,343,8765,235,433]
ans=[]
for i in random:
    if i%2!=0:
        ans.append(i)
print(ans)

# Section 6 of Task 3 in Python
input=[]
answer=[]
for i in range(1,31,1):
    input.append(i**2)
answer.append(input[:5])
answer.append(input[-5:])
print(answer)

# Section 7 of Task 3 in Python
sample=[[1,3,5,7,9,10],[2,4,6,8]]
sample[0].pop()
sample[0].extend(sample[1])
print(sample)
del sample[1:]
print(sample[0])

# Section 8 of Task 3 in Python
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

# Section 9 of Task 3 in Python
output={}
print("Enter the range:")
x=eval(input())
for i in range(1,x+1,1):
    output[i]=i*i
print(output)

# Section 10 of Task 3 in Python
x=[]
print("enter the comma separated numbers")
x=input().split(',')
y=tuple(x)
print(x)
print(y)
