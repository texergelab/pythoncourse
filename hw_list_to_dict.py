menu={"Burger": 100,
"Pizza" : 200, 
"French Fries" : 300}



def show_menu():

    for number in range(0,len(menu)):
        print(menu)

def add_menu():
    show_menu()
    item_name = input("Enter menu item to add:  ")
    menu_items.append(item_name)
    item_price = input("Enter menu price to add:  ")
    menu_item_prices.append(item_price)
    show_menu()

def add_menu()
def show_menu()
    new_item = input("Please enter new item")
    new_item_price = input ("Please enter new item price")
    menu[new_item] = new_item_price
    show_menu() 

def remove_menu():
    show_menu()
    item_name = input("Enter menu name which you want to remove")
    index=menu_items.index(item_name)
    menu_items.remove(item_name)
    del menu_item_prices[index]
    # print(menu_item_prices)
    # print(menu_items)
    show_menu()

def take_order():
    order = input("Enter your Order : ")
    if order == "Burger":
        print("Please pay 100 /-")

#add_menu()
#remove_menu()
# show_menu()
# take_order()

#user_choice=input("Do you want show menu, remove menu or add menu? ")

while(True):
    user_choice = int(input("Press \n 1 to show menu :  \n 2 to remove menu :  \n 3 to add menu :  \n 0 to exit :  "))
    
    if user_choice == 1:
        show_menu()
    if user_choice == 2:
        remove_menu()
    if user_choice == 3:
        add_menu()
    if user_choice == 0:
        break

