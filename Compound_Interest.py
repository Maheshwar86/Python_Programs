from sympy.physics.units import amount


def wr():
    res = input("Run Again Or Not (Y/N)")
    if res == "Y" or res == "y":
        Compound_Interest()
    else:
        print("Bye Sir Tata❤❤❤❤")

def Compound_Interest():
    amount = float(input("Please Enter Amount : "))
    years = int(input("Please Enter Years : "))
    rate = float(input("Please Enter Rate : "))
    if amount <=0 or years <=0 or rate <=0:
        print("Please Enter Valid Input (Greater Than 0 )")
        Compound_Interest()
    total = amount * pow((1+rate/100),years)
    print(f"The Balance Is After {years} Years Of Rs: {total:.2f}")
    wr()

Compound_Interest()