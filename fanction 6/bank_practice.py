def deposit(current_balance, amount):
    current_balance +=  int(amount)
    return current_balance


def withdraw(current_balance, amount):
    if current_balance >= int(amount):
        current_balance -= int(amount)
        return current_balance
    else:
        print ("you dont have enough money")
        return current_balance
   

def main():
    balance = 0
    while True:
        try:
            print("\n" + "="*30)
            print("     Bank App")
            print("1:deposit")
            print("2:withdraw")
            print("3:balance")
            print("4:Exit")
            user_choice = int(input("pls selece one? "))
        except ValueError:
            print("you have to enter a number")
            continue
        if user_choice == 1:
            try:
                deposit_amount = int(input("how much? "))
                balance = deposit(balance, deposit_amount)
            except ValueError:
                print("you should enter numbers") 
            
        elif user_choice == 2:
            try:
                withdraw_amount = int(input("how much? "))
                balance = withdraw(balance, withdraw_amount)
            except ValueError:
                print("you should enter numbers")

        elif user_choice == 3:
            print(f"your balance is {balance}")
        
        elif user_choice == 4:
            break
        else:
            print("you should enter between(1-4)")
             
main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    