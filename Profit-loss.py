actual_cost = float(input("Plese enter the actual product price:"))
sale_amount = float(input("Plese enter the sale amount:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = ",amount)
else:
    print("No profit!!!")    