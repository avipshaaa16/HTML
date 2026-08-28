#Define the 4 arithemetic functions
def add(a ,b):
    return a + b
def subtract(a ,b):
    return a - b
def multiply(a ,b):
    return a * b
def divide(a ,b):
    return a / b

#main program
try:
    #Reads number from the user
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))

    print("\nSelect operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("enter choice (1/2/3/4):")

    if choice == "1":
        print(f"result:{add (num1, num2)}")
    elif choice == "2":
        print(f"result:{subtract (num1, num2)}")
    elif choice == "3":
        print(f"result:{multiply(num1, num2)}")
    elif choice == "4":
        print(f"result:{divide (num1, num2)}")
    else:
        print("Invalid choice")

#Catch ValueError for non-number input
except ValueError:
    print("INVALID INPUT! PLS ENTER VALID NUMBERS")
#Catch ZeroDivisionError for division by zero
except ZeroDivisionError:
    print("ERROR:CAN'T DIVIDE BY ZERO")