import products as pr

client_cart = []

#To add products in clients' cart
def add_products():
    print()
    name = []
    for product in pr.products:
        name.append(product["name"])

    choice = input("Ki pwodui w ap mete nan panye w: ")
    while choice not in name:
        print("Silvouplè ekri non an jan li ye nan lis la")
        choice = input("Ki pwodui nan lis la w ap mete nan w ap mete nan panye w: ")
    i = name.index(choice)

    while True:
        quantity_ = input("Konbyen ou vle ladan: ")
        while not quantity_.isdigit():
            quantity_ = input("Konbyen ou vle ladan: ")
        quantity_ = int(quantity_)
        if quantity_ > (pr.products[i]["quantity"]):
            print("Kantite ou vle a plis ke sa nou genyen an, pran mwens silvouplè")
        else:
            break
    global price
    price = []
    for product in pr.products:
        price.append(product["price"].split())
    
    client_cart.append({"name": choice,"price": "$ "+ price[i][1], "quantity":quantity_})
    print()

#To compute clients' payment
def to_pay():
    print()
    if client_cart == []:
        pass
    else:
        print("Nan Panye ou genyen: ")
    i = 1
    for all in client_cart:
        print(f"Pwodui {i}")
        for ind, val in all.items():
            print(f"{ind}: {val}")
        print()
        i+=1
    money_sign = []
    money = []
    money_tot = []
    for p in client_cart:
        money_sign.append(p["price"].split())

    for m in money_sign:
        money.append(int(m[1]))
    
    for pro in range(len(client_cart)):
        money_tot.append(money[pro]*client_cart[pro]["quantity"])
    if sum(money_tot) == 0:
        print("Panye ou an vid. Ou pa gen pou w peye.")
    else:
        print(f"W ap peye $ {sum(money_tot)} pou pwodui ou yo")
    print()