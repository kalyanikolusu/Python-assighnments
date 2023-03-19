# Write a Python function to sum all the numbers in a list.
def sum(numbers):
    return sum
sum=0
numbers=list(input().split())
int_list=[]
for i in numbers:
    int_list.append(i)
    sum=sum+int(i)
result=sum    
print("sum of all the given elemnts in a list : ",result)
      
#-----------------------------------------------------------------------------
#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

x=input("Enter a string: ")
def char(x):
    upper=0
    lower=0
    for i in x:
        if i>='a' and i<='z':
            lower+=1 
        if i>='A' and i<='Z':
            upper+=1      
    print("The number of lowercase letters in a string is : ", lower)
    print("The number of upper case letters in a string is : ", upper)
char(x)  

#------------------------------------------------------------------------------

#Write a Python program to reverse a string.

def reverse_string(str):
    str=input("Enter a string : ")
    str1=(" ")
    for i in str: 
        str1=i+str1
    return str1
print("The original string is : ",str)
print("The reversed string is : ",reverse_string(str)) 







    


























