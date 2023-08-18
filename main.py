import cart, products

print("Bonjou. Byenvini sou platfòm nan\n")
while True:
    print("  ==============Meni===============")
    print("|| 1. Chache pwodui                ||") 
    print("|| 2. Wè panye ak tout pri total   ||")
    print("|| 3. Fèmen                        ||") 
    print("  =================================")

    menu_choice = input("Ki opsyon ou chwazi? ")
    while menu_choice not in ["1", "2", "3"]:
        menu_choice = input("Chwazi soti nan 1 pou rive nan 3. Ki opsyon ou chwazi? ")
    if menu_choice == "1":
        products.display_products()
        put_in_cart = input("Tape 'O' si w ap mete pwodui nan Panye w, tape 'N' si w p ap mete ==> ").upper()
        while put_in_cart not in ["O", "N"]:
            put_in_cart = input("Tape 'O' si w ap mete pwodui nan Panye w, tape 'N' si w p ap mete ==> ").upper()
        if put_in_cart == "O":
            cart.add_products()
            again = True
            while again:
                put_in_cart_again = input("Tape 'O' si w ap mete ankò sinon 'N' ==> ").upper()
                while put_in_cart_again not in ["O", "N"]:
                    put_in_cart_again = input("Tape 'O' si w ap mete ankò sinon 'N' ==> ").upper()
                if put_in_cart_again == "O":
                    cart.add_products()
                else:
                    again = False
        else:
            print()
    elif menu_choice == "2":
        cart.to_pay()
    else:
        print("Mèsi paske ou te vizite nou. Babay \U0001f44b")
        break