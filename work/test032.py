quantity = int(input("Enter the quantity : "))
price = float(input("Enter the price : "))
if quantity >= 10:
    price = price * 0.95
total = quantity * price
print("The total is ", format(total, ".2f"))
               
