# Section 1
sample=[]
for i in range(1000):
    sample.append(i)

answer=filter(lambda x: x%3!=0 and x%7==0, sample)
print(list(answer))

# Section 2
sample=[]
for i in range(50):
    sample.append(i)

def multiply(x):
    return x*x

answer=map(multiply,sample)
print(list(answer))

# Section 3
print("enter any string with combination of uppercase and lowercase characters")
sample=input()
answer=[i for i in sample if i.isupper()]
print(answer)

# Section 4
student = ['Smit', 'Jaya', 'Rayyan']
subject = ['CSE', 'Networking', 'Operating System']

zipped=zip(student,subject)
zipped=dict(zipped)
print(zipped)

# Section 5
'''
 Generator: A generator-function is defined like a normal function,
 but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
 If the body of a def contains yield, the function automatically becomes a generator function.

 next: Retrieve the next item from the iterator by calling its __next__() method.
 If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

 yield: Yield can produce a sequence of values. yield should be used when we want to iterate over a sequence, 
 but don’t want to store the entire sequence in memory.
 '''

 # Section 6
 s_input="Consultadd Training"
output=(print (i) for i in s_input[::-1])
next(output)

# Section 7
def f():
    
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
        
    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

    
f()

# Section 8
'''
Front end technology deals with setting up the UI elements along with the functionality of a website. 
All the interaction that a user has with the website is set up by a frontend developer.
Top 5 frontend technologies and their applications in companies:
a) ReactJS used by Airbnb
b) Angular used by Netflix
c) AJAX used by Flickr
d) CSS used by Google
e) XML used by Amazon
'''