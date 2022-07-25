bal = float(input("Enter current balance : "))
withdraw = float(input("Enter amount of withdrawal : "))

if withdraw > bal:
    print("Withdrawal denied")
else:
    newbal = bal - withdraw
    print("The new balance is $", newbal)
    if newbal < 150:
        print("Balance below $150")


