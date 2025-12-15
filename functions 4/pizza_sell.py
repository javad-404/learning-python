# منوی ثابت
menu = {
    "peperoni": 120,
    "makhloot": 150,
    "sabzijat": 100
}

# سبد خرید مشتری 
cart = []


def show_menu():
    print(menu)


def add_to_cart(name):
    if name in menu.keys():
        cart.append(name)
        print("Added to cart")
    else:
        print("We don't have this pizza")
        
        
def calculate_bill():
    bill = 0
    for item in cart:
        price = menu[item]
        bill += price
    return bill


while True:
    print("--- welcome ---")
    print("1:show_menu")
    print("2:add_to_cart")
    print("3:calculate_bill")
    print("4:Exit")
    
    try:
        user_choice = int(input("pls selece one(1-4): "))
    except ValueError:
        print("you should enter a number")
        continue
        
    if user_choice == 1:
        show_menu()
        
    elif user_choice ==2:
        
        name = input("what kind of pizza do you want to buy? ") 
        add_to_cart(name)
         
    elif user_choice ==3:
       x = calculate_bill()
       print(f"you should pay {x} toman")
    elif user_choice == 4:
        print("enjoy your pizza!")
        break
    else:
        print("wrong number")
        
        
