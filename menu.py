while True:

    breads = {"Normal chapati":10,"Karak chapati":20,"Garlic naan":50}
    sabji = {"Computer sabji":100,"Tereee sabji":120,"Sabki sabji":200}

    print()
    print("Welcome!! to bilu ka thaba ")
    print()
    print("Bread's")
    print()
    for i,j in breads.items():

        print(i,": ",j)

    print()
    print("Sabji's")
    print()
    for i,j in sabji.items():

        print(i,": ",j)

    print("Please put the number of the dish first and with a space put the quantity")

    print("Type (Yes) to continue to order or (NO) to check out")
    maininput = input("Order here: ")

    if maininput.lower() == "no":
        break
    
    elif maininput.lower() == "yes":
        continue

    order , quantity = map(int,maininput.split())
    print(order, quantity)


    

