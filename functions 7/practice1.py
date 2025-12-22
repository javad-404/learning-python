def add_expense(name, amount):
    with open ("expenses.txt", "a") as f:
       line = f"{name},{amount}\n"
       f.write(line)


def calculate_total():
        total_price = 0
        try:
            with open ("expenses.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        price = int(parts[1])
                        total_price += price 
                return total_price
        except FileNotFoundError:
            return 0
        
def main():
    while True:
        print("*"*30)
        print("       Menu")
        print("1:add expense")
        print("2:show total expenses")
        print("3:Exit")
        print()
        try:
            user_choice = int(input("selece one: "))
        except ValueError:
            print("you need to enter  number")
            continue
        
        if user_choice == 1:
            name = input("what did you buy? ")
            try:
                amount = int(input("how much it took?"))
                add_expense(name, amount)
                print("Saved.")
            except ValueError:
                print("price must be a number")
        elif user_choice == 2:
            x = calculate_total()
            print(f"your total price is {x:,}")
        elif user_choice == 3:
            break
        else:
            print("you need to enter between (1-3)")
main()

            
            
            
       
        
