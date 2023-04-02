# In this challenge, you need to implement a method that squares passing variables and returns their sum.
#Problem statement: Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:
#Task 1  Implement a constructor to initialize the values of three properties: x, y, and z.
#Task 2: Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

'''class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqsum(self):
        print("squares of sum of numbers is",self.x*self.x+self.y*self.y+self.z*self.z) 
ob1=point(2,4,6)
print(ob1.x)
print(ob1.y)
print(ob1.z)
ob1.sqsum() '''

#In this exercise, you have to implement a calculator that can perform addition, subtraction, multiplication, and division.
#Problem statement Write a Python class called Calculator by completing the tasks below:

'''class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Addition of the numbers is : ",self.num1+self.num2)  
    def subtract(self):
        print("subtraction of the numbers is : ",self.num1-self.num2)
    def multiply(self):
        print("Multiplication of the numbers is : ",self.num1*self.num2)
    def divide(self):
        print("Division of the numbers : ",self.num1/self.num2)   
obj=calculator(150,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()  ''' 

# Challenge 3: Implement the Complete Student Class.In this challenge, you will implement a student class.
#Problem statement:
#Implement the complete Student class by completing the tasks below
#Task
#Implement the following properties as private:
# name
# rollNumber
#Include the following methods to get and set the private properties above:
# getName()
#setName()
# getRollNumber()
# setRollNumber()

class student:
    def __init__(self,name,rollnumber):
        # Implement the properties as private
        self.__name=name
        self.__rollnumber=rollnumber
     #  instance methods:
    def getname(self):
        print("name : ",self.__name)
    def getrollnumber(self):
        print("Rollnumber is : ",self.__rollnumber)
    def setname(self,name):
        self.__name=name
        print("The set name is : ",self.__name)
    def setrollnumber(self,rollnumber):
        self.__rollnumber=rollnumber
        print("The setrollnumber is :",self.__rollnumber)
#creating object of class
st1=student("jessa",101)
#calling public methods of teh class
st1.getname()
st1.getrollnumber()  
# change the name =John and rollnumber =102 using setter 
st1.setname("john")
st1.setrollnumber(102)


