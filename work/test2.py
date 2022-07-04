price = float(input("Enter an amount : "))
discount = float(input("Enter a discount : "))

total = price - discount
print(format(price, ".2f"),"-" ,format(discount, ".2f") ,"=" ,format(total, ".2f"))

