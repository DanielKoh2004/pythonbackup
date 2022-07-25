suit1 = float(input("Enter cost of first suit : "))
suit2 = float(input("Enter cost of second suit : "))
if suit1 > suit2:
    suit2 = suit2 * 0.5
else:
    suit1 = suit1 * 0.5
total = suit1 + suit2
print("Cost of the two suits is $",total)
