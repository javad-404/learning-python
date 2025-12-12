rates = {
    "dollar": 50000,
    "euro": 54000,
    "derham": 14000
}

def add_currency():
    new_curre = input("pls enter new currency name: ")
    new_price = int(input("pls enter new currency price: "))
    rates[new_curre] = new_price
    print(f"Done! new {new_curre} is added and its price is {new_price}")
    return new_curre, new_price
def calculate_cost(name, amount):
    if name in rates:
        price = rates[name]
        total = amount * price
        return total
    else:
        return 0
    
def show_menu():
    print("*** MENU ***\n")
    print("1: add_currency \n")
    print("2: calculate_cost\n")
    print("3: Exit")
    choice = int(input("pls choose one(1-3): "))
    return choice

while True:
    user_choice = show_menu()
    if user_choice == 1:
        add_currency()
    elif user_choice == 2:
        what = input("which currency? ")
        money = int(input("how much: "))
        result = calculate_cost(what, money)
        if result == 0:
            print ("currency not found")
        else:
            print (f"price is {result} toman")
    elif user_choice == 3:
        print ("good_bye")
        break
        
         
        
                            