# Create three variables in a single line and assign different values to them and make sure their data types are different.
# Like one is int, another one is float and the last one is a string.

x, y, z = 10, 20.5, "Consultadd"
print ("x is: ", x)
print ("y is: ", y)
print ("z is: ", z)

# Create a variable of value type complex and swap it with another variable whose value is an integer.
cmplx = 20+5j
x, cmplx = cmplx, x
print("Values after swapping are:")
print("x is: ", x)
print("Cmplex variable is: ", cmplx)

# Swap two numbers using the third variable as the result name and do the same task without using any third variable.
print("x and y will be swapped with third variable called name")
name = x
x = y
y = name
print ("x and y value after swapping is: ", x, y)

print("swapping x and y again without using third variable")
x,y = y,x
print("x and y value after swapping without third variable is: ", x, y)

# Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
print("Enter any number from keyboard")
val = input()
print("value you have entered is: ", val)  # this is printing the value using python 3.x version
print("printing value for 2.x version is going to give us an error because currently I am working on version 3.x but the below line is commented for that purpose")
# print "value of x in version 2.x is", val

# Write a program to complete the task given below:
# Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
# Use z for adding 30 into it and print the final result by using variable results.
print("enter two numbers one by one with values between 1 and 10")
a = int(input())
b = int(input())
z = a + b
results = z + 30
print("The final value is: ", results)

# Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc
print("enter anything so that its data type can be checked")
val2 = eval(input ())
print("The data type of entered value is: ", type(val2))

# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?
# yes the value will be changed because that's why the variable is used for.
# It means we have an access to the memory which can store the data of any type and
# python is smart enough to change the data type of that variable depending upon the value stored in it.
