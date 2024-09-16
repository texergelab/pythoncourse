
def add(number1, number2):
    return number1 + number2

def multiply(number1, number2):
    return number1 * number2

def sub(number1, number2):
    
    return number1 - number2

def div(number1, number2):

    if (number2 == 0):
        return "Not allowed"
    else:
        return number1 // number2

# taking inputs

first_number = int(input("Enter one number : "))
second_number = int(input("Enter second number : "))


add_res = add(first_number, second_number)
mul_res = multiply(first_number, second_number)
div_res = div(first_number, second_number)
sub_res = sub(first_number, second_number)

print(f"The sum is. : {add_res}")
print(f"The mul is. : {mul_res}")

print(f"The div is. : {div_res}")
print(f"The sub is. : {sub_res}")