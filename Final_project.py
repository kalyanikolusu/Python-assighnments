# The application will have a log-in for admin.
print("\n Admin User id & Password")
admin_name=input("Enter adminname :")
password=input("Enter a password : ")
class Admin_login():
    def signup(self,admin_name,password):
        self.admin_name=admin_name
        self.password=password
        return "singup succeed"
    def login(self,admin_name,password):
        if self.admin_name==admin_name and self.password==password:
            return "logged in"
        else:
            return "WrongId & Password"
ad1=Admin_login()
print(ad1.signup(admin_name,password))
print(ad1.login(admin_name,password))
     
#  Admin will have the following functionalities: 
#  Add new food items. Food Item will have the following details:
print("\n Add new food items.Food item will have the following details")
class food_items():
    def __init__(self,id,name,quantity,price,discount):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.discount=discount
ft1=food_items(1,'paneer 65','250grm',200,'5%')
ft2=food_items(2,'vegpulav','500grm',350,'4%')
ft3=food_items(3,'mushrooms_pakodi','250grm',200,'5%')
ft4=food_items(4,'friedrice','500grm',250,'0%')
ft5=food_items(5,'ice-cream','100grm',90,'5%')
ft6=food_items(6,'7up','100ml',60,'0%"')
print(ft1.id,ft1.name,ft1.quantity,ft1.price,ft1.discount)
print(ft2.id,ft2.name,ft2.quantity,ft2.price,ft2.discount)
print(ft3.id,ft3.name,ft3.quantity,ft3.price,ft3.discount)
print(ft4.id,ft4.name,ft4.quantity,ft4.price,ft4.discount)
print(ft5.id,ft5.name,ft5.quantity,ft5.price,ft5.discount)
print(ft6.id,ft6.name,ft6.quantity,ft6.price,ft6.discount)
# stock
print("\n stock")
stock=int(input("Enter stocks value :"))
if stock<=100:
    print("stock available")
else:
    print("out of stock")
#Amount left in stock in restaurent
print("\n amount left in stock in restaurent")
stock_sale=int(input("Enter  the stock sale value : "))
if stock_sale<=50:
    print("\n 50 stock available")
elif stock_sale>=70:
    print("\n 30 stock available")
else:
    print("\n out of stock")    
# Edit food items using foodid
if ft1.id==3:
    print("\n (Truffle Cake 500gm) [INR 900] 10 per n/")
else : 
    print("\n Chicken leg piece  500rs 4 piece 10% Dis ")
# View the list of all food items.
dict1={'name1':'panner65','name2': 'vegpulav','name3':'mushrooms_pakodi','name4':'friedrice','name5':'ice-cream','name6':'7up'}
list_dict=list(dict1.items())
print(list_dict)  
# Remove a food item from the menu using FoodID.
if ft1.id == 1:

    print("\n Tandoori Chicken (4 pieces) [INR 240] 5 per")
else :
    print("\n 2 Vegan Burger (1 pieces) [INR 320] 5 per")

# The user will have the following functionalities:
class user():
    full_name=input("Enter user fullname :")  
    phone_number=int(input("Enter user phone number : "))
    Email=input("Enter user emailid : ")
    address=input("Enter user address name : ")
    password=input("Enter user password : ")
    def __init__(self,full_name,phone_number,Email,address,password):
        self.full_name=full_name
        self.phone_number=phone_number
        self.Email=Email
        self.address=address
        self.password=password
us=user('full_name','phone_number','Email','address','password')
#creating user login details .first signup and then login.
class User_login(): 
    user_name=input("Enter user user name : ")
    password=input("Enter user password : ")
    def signup(self,username,password):
        self.username = username
        self.password = password
        return "singup succeed"
    
    def login(self,username,password):
        if self.username == username and self.password==password:
            return "logged in"
        else:
            return "Username and password is incorrect"
        
us =  User_login()
print(us.signup('user_name','password'))
print("register sucessful")
print(us.login('user_name','password'))
print("login successful")
# Place New Order: The user can place a new order at the restaurant.
# Show list of food. The list item should as follows:
# 1. Tandoori Chicken (4 pieces) [INR 240]
# 2. Vegan Burger (1 Piece) [INR 320]
# 3. Truffle Cake (500gm) [INR 900]
class place_order(food_items):
    
    def __init__ (self):
        
        if place_order == food_items :
            return (food_items)
        else:
            print("1. Tandoori Chicken (4 pieces) [INR 240] 5 per")
            print("2. Vegan Burger (1 pieces) [INR 320] 5 per")
            print("3. Truffle Cake (500gm) [INR 900] 10 per")
f1 = place_order()

# Order History should show a list of all the previous orders
print("\n Order History should show a list of all the previous orders :-  ")
class order_history(food_items):
    
    def __init__ (self):
        
        if order_history == food_items :
            return (food_items)
        else:
            print("2. Vegan Burger (1 pieces) [INR 320] 5 per")
            print("3. Truffle Cake (500gm) [INR 900] 10 per")
f3 = order_history()


# Update Profile: the user should be able to update their profile.
print("\n Update Profile: the user should be able to update their profile :-  ")
class User_update_profile (user):  
                      
    def __init__(self,full_name,phone_number,Email,address,password):
        super().__init__(full_name,phone_number,Email,address,password)
udate=user('full_name','phone_number','Email','address','password')
print(input("Enter user updated fullname :"))
print(input("Enter user updated  mobile no :"))
print(input("Enter user updated  email : "))
print(input("Enter user updated  address : "))
print(input("Enter user updated password : "))
print(input("Updated successfully"))
print(input("visit again"))
      
         
         
        
        
        
        
        
        
        



        
