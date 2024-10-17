#revenue, cost

revenue = int(input("How much revenue you have : "))
cost = int(input("How much cost you spend : "))

def profit_margin_calculator():
    return ((revenue - cost)/revenue)*100


print(f'Your profit is {profit_margin_calculator()}%')