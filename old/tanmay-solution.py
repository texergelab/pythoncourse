
# Write a function calculate_profit_margin
# (revenue, cost) that takes in the revenue and cost as arguments 
# and returns the profit margin percentage.
revenue = int(input("give revenue"))
cost = int(input("give cost"))

def subtract():
    return revenue - cost

def divide():
    profit = subtract()
    return profit / revenue

def percentage():
    abcd = divide()
    return abcd * 100

print(percentage())


