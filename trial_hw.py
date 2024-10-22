menu={"Burger": 100,
"Pizza" : 200, 
"French Fries" : 300}



def show_menu():

    for number in range(0,len(menu)):
        print(menu)

def add_menu():
    show_menu()
#item_name = input("Enter menu item to add:  ")
#menu.append(item_name)
#item_price = input("Enter menu price to add:  ")
#menu.pop(item_price)
#show_menu()
new_item = input("Please enter new item")
new_item_price = input ("Please enter new item price")
menu[new_item] = new_item_price
print (menu)
