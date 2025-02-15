from string import capwords


def WeightConverter():
    weight = int(input("Please Enter A  Weight : "))
    unit = input("Kilograms Or Pounds ? (K/P) : ")
    Co_Unit = capwords(unit)
    if Co_Unit == "K" or Co_Unit == "P":
        if Co_Unit == "K":
            print("Your Weight IS ",round(weight*2.205,2),"Lbs ")
        elif Co_Unit == "P":
            print("Your Weight Is ",round(weight/2.205,2),"Kgs")
    else:
        print("Please Enter A Valid Unit !")
        WeightConverter()

WeightConverter()