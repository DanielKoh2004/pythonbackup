import math
def area(a,b):
    return (a*b)/2

def perimeter(a,b):
    return a + b + (math.sqrt(a**2 + b **2))

def menu():
    print("         /|                  |\ ")
    print('        / | TRIANGLE EXPERT b| \ ')
    print("       /__|                  |__\ \n")

    print("What do you want to calculate? ")
    print("[1] Area of Triangle")
    print("[2] Perimeter of Triangle")
    print("[other number] EXIT")

def main():
    cont = "Y"
    while cont.upper() == "Y":
        menu()
        choice = input("Your selection (Choose a number):")
        if choice not in '1' and '2':
            print("bye bye!")
            break
        else:
            a = eval(input("Enter the width of the triangle : "))
            b = eval(input("Enter the height of the triangle : "))
            if choice in '1':
                print("Area of triangle is",area(a,b))
            elif choice in '2':
                print("Perimeter of the triangle is",perimeter(a,b))
        cont = input("Do you wish to try again? ")
    
main()
    
    
    
    
    
