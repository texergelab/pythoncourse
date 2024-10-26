menu = {
    
    "Burger": 100,
    "Pizza" : 200, 
    "French Fries" : 300
    }




def show_menu ():
    for item in menu:
        print(f"{item} : {menu[item]} /-")


# Add to the menu
def add_menu():
    print("Currently We have following menu items : ")
    show_menu()
    menu_item = input("Enter menu item to be added")
    menu_item_price = input("Enter menu item price to be added")

    menu[menu_item] = menu_item_price
    print("Menu successfully added!!")
    show_menu()

def remove_menu():
    pass

def update_menu():
    pass

def discounted_price():
    pass