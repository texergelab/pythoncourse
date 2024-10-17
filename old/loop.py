special_menu = ["burger", "pasta", "pizza"]
starter_menu = ["nachos", "fries", "samosa"]
main_course = ["nun", "curry", "veg briiyani"]
special_menu_price = [100,200,300]

print("===========Special Menu============")
    
for item in special_menu:
    print(item)

print("==============================")



print("---------------Starter Menu----------------")
for item in starter_menu:
    print(item)
print("--------------------------------")

print("------------Main Course Menu---------------")
for item in main_course:
    print (item)
print("--------------------------------")



for i in range (0,3):
    print(starter_menu[i])
    print(special_menu_price[i])