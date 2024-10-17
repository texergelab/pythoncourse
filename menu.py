menu_items = ["Burger","Pizza", "French Fries"]
menu_item_prices = [100,200,300]


def show_menu():

    for number in range(0,3):
        print(f"{menu_items[number]} : {menu_item_prices[number]} /-")

def add_menu():
    item_name = input("Enter menu item to add:  ")
    menu_items.append(item_name)
    item_price = input("Enter menu price to add:  ")
    menu_item_prices.append(item_price)

def 


def take_order():
    order = input("Enter your Order : ")
    if order == "Burger":
        print("Please pay 100 /-")

    

show_menu()
take_order()


