#fermat's theorem
def check_fermat():
        x1 = a**n + b**n
        x2 = c**n
        if n > 2 and x1 == x2:
                print("Holy smokes, Fermat was wrong!!")
        elif n<2 and x1==x2:
                print("It works!")
        else:
                print("No, that doesn't work")



a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
n = int(input("Enter the exponent:"))

check_fermat()
