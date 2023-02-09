""" Calculator Project """
import pyperclip

# --------------------------------------------------------------------------------------------
def add(number1, number2) -> float:
    "Addition of two numbers"
    return float(number1 + number2)
# --------------------------------------------------------------------------------------------
def subtract(number1, number2) -> float:
    "Subtraction of two numbers"
    return float(number1 - number2)
# --------------------------------------------------------------------------------------------
def multiply(number1, number2) -> float:
    "Multiplication of two numbers"
    return float(number1 * number2)
# --------------------------------------------------------------------------------------------
def divide(number1, number2) -> float:
    "Division of two numbers"
    try:
        return float(number1 / number2)
    except ZeroDivisionError:
        print("\nCan't Divide !!")
        return None
# --------------------------------------------------------------------------------------------
def exponent(number1,number2) -> float:
    "Exponent of two numbers"
    return float(number1 ** number2)
# --------------------------------------------------------------------------------------------
def clipboard(operation):
    "Coping result to Clipboard"
    print("Please Inter From [y/n]:\n")
    clip = input("Do You Want To Copy Result to Clipboard ?: ").strip()
    if clip not in ("y", "Y", "yes"):
        pass
    else:
        pyperclip.copy(operation)
        print("\nResult Successfully Copied To Your Clipboard !!\n")
# --------------------------------------------------------------------------------------------
while True:
    print("Operation Menu :-\n" ,
            "1. Addition of two numbers.\n",
            "2. Subtraction of two numbers.\n",
            "3. Multiplication of two numbers.\n",
            "4. Division of two numbers.\n",
            "5. Exponent of two numbers.\n")
    select_1 = input("Select operations form 1, 2, 3, 4, 5 : ").strip()
# --------------------------------------------------------------------------------------------
    if select_1 == "1":
        while True:
            try:
                num1 = float(input("Enter first number: " ))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("\nInvalid input!\n")
                continue
        Add_s = f"\n{num1} + {num2} = {add(num1, num2)}\n"
        print(Add_s)
        clipboard(add(num1, num2))
#---------------------------------------------------------------------------------------------
    elif select_1 == "2":
        while True:
            try:
                num1 = float(input("Enter first number: " ))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("\nInvalid input!\n")
                continue
        Sub_s = f"\n{num1} - {num2} = {subtract(num1, num2)}\n"
        print(Sub_s)
        clipboard(subtract(num1, num2))
#---------------------------------------------------------------------------------------------
    elif select_1 == "3":
        while True:
            try:
                num1 = float(input("Enter first number: " ))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("\nInvalid input!\n")
                continue
        Multiply_s = f"\n{num1} x {num2} = {multiply(num1, num2)}\n"
        print(Multiply_s)
        clipboard(multiply(num1, num2))
#---------------------------------------------------------------------------------------------
    elif select_1 == "4":
        while True:
            try:
                num1 = float(input("Enter first number: " ))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("\nInvalid input!\n")
                continue
        Divide_s = f"\n{num1} ÷ {num2} = {divide(num1, num2)}\n"
        print(Divide_s)
        clipboard(divide(num1, num2))
#---------------------------------------------------------------------------------------------
    elif select_1 == "5":
        while True:
            try:
                num1 = float(input("Enter first number: " ))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("\nInvalid input!\n")
                continue
        Exponent_s = f"\n{num1} ^ {num2} = {exponent(num1, num2)}\n"
        print(Exponent_s)
        clipboard(exponent(num1, num2))
#---------------------------------------------------------------------------------------------
    elif select_1 not in ("1", "2", "3", "4", "5"):
        print("\nInvalid input!\n")
        continue
#---------------------------------------------------------------------------------------------
    select_2 = input("Do You want to try again ?: ").strip()
    if select_2 not in ("y", "Y", "yes"):
        break
# --------------------------------------------------------------------------------------------
# END OF THE PROJECT 
