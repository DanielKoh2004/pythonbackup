#input
name = input("Enter your name : ")
salary = float(input("Enter you salary : "))

#process
salary = salary * 1.1

#output
print("Name =" ,name)
print("Salary = {0:.2f}".format(salary))

print("Name =" ,name)
print("Salary = %.2f"%(salary))
