# منوی ثابت
menu = {
    "peperoni": 120,
    "makhloot": 150,
    "sabzijat": 100
}

# سبد خرید مشتری 
cart = []


def show_menu():
    print("--- MENU ---")
    for name, price in menu.items():
        print(f"{name} : {price} ")


def add_to_cart(name, count):
    if name in menu.keys():
        for i in range(count):
            cart.append(name)
            print(f" {count} ta {name} added to cart.")
    else:
        print("We don't have this pizza")
        
        
def calculate_bill():
    bill = 0
    for item in cart:
        price = menu[item]
        bill += price
    return bill

def save_bill(total_price):
    with open("factor.txt", "w") as f:
        f.write("--- haji javad pizza factor ---\n")
        for item in cart:
            p= menu[item]
            f.write(f"{item}\t : {p}\n")
            
        f.write("-------------------------\n")
        f.write(f"TOTAL PAY : {total_price} Toman\n")
        f.write("-------------------------\n")
        f.write("Thanks for buying!\n")
    
    print(" Factor saved in 'factor.txt'")
        


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
        try:
            count = int(input("How many? "))
            if count > 0:
                add_to_cart(name, count)
            else:
                print("Count must be positive!")
        except ValueError:
            print("Number for count!")
         
    elif user_choice ==3:
       x = calculate_bill()
       print(f"you should pay {x} toman")
       save_bill(x)
       
    elif user_choice == 4:
        print("enjoy your pizza!")
        break
    else:
        print("wrong number")
        
        
