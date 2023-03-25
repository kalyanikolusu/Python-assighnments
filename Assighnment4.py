# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

'''number=lambda y : y+25
n=int(input("Enter any number : " ))       #using input function to take input from user.
print(number(n))'''

# Write a Python program to triple all numbers of a given list of integers. Use Python map.

'''numbers=input("Enter a list of numbers : ").split()
num_intlist=[]
for i in numbers:
    num_intlist.append(int(i))
print(num_intlist)
triple_numbers=map(lambda x : x*3 ,num_intlist)
print(list(triple_numbers)) '''

# Write a Python program to square the elements of a list using map() function.
numbers=input("Enter a list of numbers : ").split()
num_intlist=[]
for i  in numbers:
    num_intlist.append(int(i))
print(num_intlist)
square=map(lambda x:x**2,num_intlist)
print(list(square))



