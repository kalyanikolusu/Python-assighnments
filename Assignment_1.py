     
#Write a Python program to get the Fibonacci series between 0 to 50
'''nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1'''
#------------------------------------------------------------

#write a program to count the number of even and odd numbers from given series of numbers
'''list1=[10, 21, 4, 45, 66, 93, 1] 
even_count, odd_count = 0, 0
# iterating each number in list
for num in list1:
    if num%2==0:
        even_count +=1
    else:
        odd_count+=1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)'''

#---------------------------------------------------------------------
#write a pro

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")


    

           