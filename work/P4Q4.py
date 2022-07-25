hour = int(input("Enter hours worked : "))
pay = int(input("Enter hourly pay rate : "))
if hour > 40:
    extra = pay * 1.5
    extrapay = extra * (hour - 40)
gross = 40 * pay + extrapay
print("Gross pay = ",format(gross, ".2f"))
