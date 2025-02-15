from string import capwords


def Temp_Convert():
    unit = input("Please Enter A Temperature Unit Celsius or Fahrenheit (C/F) : ")
    Co_Unit = capwords(unit)
    if Co_Unit == "C" or Co_Unit == "F":
        temp = float(input("Please Enter A Temperature : "))
        if Co_Unit == "C":
            result = round((9*temp)/5+32,2)
            print(f"The Temperature Is {result}F")
        elif Co_Unit == "F":
            print(f"The Temperature Is {round((temp-32)*5/9 ,2)}C")
    else:
        print(f"{Co_Unit} Is A Not A Valid Unit !")
        Temp_Convert()
Temp_Convert()

