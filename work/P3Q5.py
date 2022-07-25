numYrs = int(input("Enter number of years : "))
if numYrs > 5:
    interest = 0.075
else:
    interest = 0.054
print("Interest rate is ",format(interest, ".2%"))

