menu = {'Espresso': 25, 'Latte': 30, 'Cake': 15, 'Tea': 10}

def show_menu():
    print("\n" + 30* "=")
    print("      Resturant Menu")
    for i, j in menu.items():
        print(f"{i} : {j}")
    print("\n" + 30* "=")
def get_order():
    order = []
    while True:
        user_order = input("what would you like ?(say end to close) ").title()
        if user_order == "end":
            break
        if user_order in menu:
            order.append(user_order)
            print(f"{user_order} ezafe shod.")
        else:
            print("we dont have this")
        
    return order
def calculate_bill(order):
    total = 0
    for i in order:
        price = menu[i]
        total += price
    return total


def main():
    show_menu()
    my_order = get_order()
    if len (my_order) > 0:
        final_price = calculate_bill(my_order)
        print(f"Sefarash shoma: {my_order}")
        print(f"Gheymat kol: {final_price} Toman")
    else:
        print("Hichi sefaresh nadadi ke!")
        
    
main()
    
    
    




        
        