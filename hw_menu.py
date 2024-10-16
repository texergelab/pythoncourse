#special_menu = ["burger", "pasta", "pizza"]
#special_menu_price = [100,200,300]
#starter_menu = ["nachos", "fries", "samosa"]
#starter_menu_price = [50,100,150]
#main_course = ["nun", "curry", "veg biryani"]
#main_course_price = [100,300,500]


menu = ("Burger","pizza","pasta")
price = [100,200,300]
burger = Burger
pizza = Pizza
pasta = Pasta
price = [100,200,300]

users_choice = input("What item would you like to have? Please select from menu")

if users_choice == Burger:
for item1, item2 in zip(menu, price): #what does zip mean?
    print (burger, price)


for item1, item2 in zip(menu, price): 

    print(item1, item2) 
