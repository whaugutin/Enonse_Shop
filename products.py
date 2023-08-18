products = [{"name":"Laptop", "price":"$ 400", "quantity":10},
            {"name":"Router", "price":"$ 58", "quantity":8},
            {"name":"USB", "price":"$ 25", "quantity":20},
            {"name":"Keyboard", "price":"$ 20", "quantity":22},
            {"name":"Souris", "price":"$ 15", "quantity":15}]

#To display all the products in stock
def display_products():
    print()
    i = 1
    for product in products:
        print(f"Pwodui {i}")
        for ind, val in product.items():
            print(f"{ind}: {val}")
        print()
        i+=1
    print()
