# Create an assignment for File handling of JSON files in Python
#Assignment 1
# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.


'''import json
class Employee:
    def __init__(self):
        self.emp_dic={}
    def creat_JSON(self):
        for i in range(5):
            name = input("Enter your name: ")
            dob = input('Enter your DOB: ')
            height = input('Enter your height: ')
            city = input('Enter your city: ')
            state = input('Enter your state: ')
            emp={'name':name,'dob':dob,'height':height,'city':city,'state':state}
            emp_id = len(self.emp_dic)+1
            self.emp_dic[emp_id]=emp
        with open("emps.json",'w') as f:
            json.dump(self.emp_dic,f)

    def data_print(self):
        with open("emps.json","r") as f:
            data = json.load(f)
        for i in data.values():
            l1 = []
            l1.append(i)
            print(l1)  

x =Employee()            
x.creat_JSON()
print("--------------------------------------------------")
x.data_print()  '''
# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
'''import json
class State_Capital:
    def __init__(self):
        self.st_cap={}
    def creat_JSON(self):
        for i in range(5):
            s_name=input("Enter state name : ")
            c_name=input("Enter capital name: ")
            SC_dict={s_name:c_name}
            self.st_cap.update(SC_dict)
        with open ("state_capital.json",'w') as f:
            json.dump(self.st_cap,f)
    def print_JSON(self):
        with open("state_capital.json",'r') as f:
            data=json.load(f)
        for i,j in data.items():
            print('state:' + i + ' capital:'+j)
x=State_Capital()  
x.creat_JSON()
x.print_JSON()'''

#1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.
class dog:
    def __init__(self,name,age,colour):
        self.name=name
        self.age=age
        self.colour=colour
    def description(self):
        print("The dog name is :",self.name)
        print('Age of ',self.name,' is: ',self.age) 
    def get_info(self):
        print('the colour of ',self.name,'is :',self.colour) 
class JackRussellTerrier(dog):
    def health(self):
        print('The breed has a reputation for being ') 
        print('Jack Russells can live from 14 to 16 years.')
    def Crossbreeds(self):
        print('Crossbreed of a jack Russell terrier and a Beagle is called a Jackbee.')
class Bulldog(dog):
    def health(self):
        print('The avarage life span of the breed as 8 to 10 years.')
        print('Alleries and hip issues in older bulldogs.')
    def Appearance(self):
        print('Thick folds of skin on the brow ,round,black,wide set eyes.')
        print('A rope or nose roll above  the nose.')
dog=Bulldog('Duke',5,'white')
dog.description()
dog.get_info()
dog.health()
dog.Appearance()

dog1=JackRussellTerrier('stella',4,'brown')
dog1.description()
dog1.get_info()
dog1.health()
dog1.Crossbreeds()

                               

                
