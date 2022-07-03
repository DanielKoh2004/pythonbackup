num1 = float(input("Enter amount invested in SPY: "))
num2 = float(input("Enter amount invested in QQQ: "))
num3 = float(input("Enter amount invested in EEM: "))
num4 = float(input("Enter amount invested in VXX: "))

total = num1 + num2 + num3 + num4
SPYperc = num1/total
QQQperc = num2/total
EEMperc = num3/total
VXXperc = num4/total

print("ETF      PERCENTAGE")
print("-------------------")
print("SPY     {0:10,.2%}".format(SPYperc))
print("QQQ     {0:10,.2%}".format(QQQperc))
print("EEM     {0:10,.2%}".format(EEMperc))
print("VXX     {0:10,.2%}".format(VXXperc))
print("TOTAL AMOUNT INVESTED : $",total)