#score = int(input("Enter Your Score : "))
#if score >= 50:
    #print("Pass")
#else:
    #print("Fail")

amount = eval(input("Enter an amount : "))
member = input("Enter the member type (C)lassic or (G)old : ")
if member.upper() == "C":
    amount = amount * 0.95
else:
    amount = amount * 0.5
print(amount)

