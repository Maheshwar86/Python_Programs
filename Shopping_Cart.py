Product = []
Price = []

def total():
    print("==========  Bill Section  =========")
    res =0
    for i in Price:
        res+=i
    print("This Is All Your Products And Price Sir !")
    for j in Product:
        print(j)
    print("Sir Total Price Is : Rs:",res)
    yo = input("Sir Press (Y) Goto Shopping Or Any Key Enter to Exit The Shop ! : ")
    if yo.lower() =="y":
        Shop()
    else:
        print("Thank You For Shopping Dtao Official Shopping Mall Sir ! ")
        print("Come Again Sir Bye Tata ❤😊🤞🤞✌💖")
        exit(1)

def rem():
    go = input("If You Want Shop More Items (Y/N)")
    if go.lower() =="y":
        Shop()
    else:
        total()
def Shop():

    print("==========  Wellcome To Dtao Official Shopping Mall ==========")
    print("\n 1 : Sumsung s30 Ultra  Rs:175000 \n 2: Mongo Fruit(1kg) Rs:70 \n 3: Washing Machine  Rs:25000 \n 4: Banana(1kg)  Rs:40")
    option = int(input("Which Product You Want Please Select Sir/Madam :"))
    if option == 1:
        Product.append("Sumsung s30 Ultra")
        Price.append(175000)
        rem()
    elif option == 2:
        Product.append("Mongo Fruit(1kg)")
        Price.append(70)
        rem()
    elif option == 3:
        Product.append("Washing Machine")
        Price.append(25000)
        rem()
    elif option == 4:
        Product.append("Banana(1kg)")
        Price.append(40)
        rem()
Shop()

