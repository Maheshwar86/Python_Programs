def calling():
    option = input("If You Want To Run Again ! (Y/N)")
    if option == "Y" or option == "y":
        calculator()
    else:
        print("Thank You Bye Bro Good Night Sweet Dreams !")
def calculator():
    operator = input("Please Enter A Operator (+,-,*,/) : ")
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        num1 = float(input("Please Enter A Number : "))
        num2 = float(input("Please Enter A Number : "))
        if operator == "+":
            print(round(num1 + num2,3))
            calling()
        elif operator == "-":
            print(round(num1 - num2,3))
            calling()
        elif operator == "*":
            print(round(num1 * num2,3))
            calling()
        elif operator == "/":
            print(round(num1 / num2,3))
            calling()
    else:
        print("Invalid Operator")
        calculator()
calculator()