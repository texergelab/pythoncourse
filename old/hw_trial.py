special_menu = ["burger", "pasta", "pizza"]
special_menu_price = [100,200,300]
starter_menu = ["nachos", "fries", "samosa"]
starter_menu_price = [50,100,150]
main_course = ["nun", "curry", "veg biryani"]
main_course_price = [100,300,500]

input("What would you like to have?")
for item1, item2 in zip(special_menu, special_menu_price): #what does zip mean?
    print (item1,item2)

for item3, item4 in zip(starter_menu, starter_menu_price): #what does zip mean?
    print (item3,item4)

for item5, item6 in zip(main_course, main_course_price): #what does zip mean?
    print (item5,item6)