#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
'''my_dict={}
for i in range(97, 97 + 26):
    my_dict[chr(i)] = i
print(my_dict)'''


# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
def last(n):
    return n[-1] 
  
def sort(tuples):
    return sorted(tuples, key=last)
  
a=[(2, 5), (1, 2), (4, 4),(2,3),(2,1)]
print("Sorted:")
print(sort(a))
