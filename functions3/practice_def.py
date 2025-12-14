account = {"name": "Haji", "balance": 0}


def deposit(amount):
    account["balance"]+= amount
    print("Deposit successful")
    
    
def withdraw(amount):
    
    if amount > account["balance"] :
        print("Money not enough")
    else:
        account["balance"] -= amount
        print("Here is your money")


while True:
    print("--- main menu ---")
    print("1: deposit")
    print("2: withdraw")
    print("3: balance")
    print("4: Exit")
    
    user_choice = int(input("please selece one(1-4): "))
    if user_choice < 1 or user_choice > 4:
        print("wrong value! try again")
        continue
    if user_choice == 1:
        amount = int(input("pls enter your depisote value: "))
        deposit(amount)
    elif user_choice == 2:
        amount = int(input("pls enter your withdraw value: "))
        withdraw(amount)
    elif user_choice == 3:
        x = account["balance"]
        print(f"your balance is {x}")
    else:
        print("good bye!")
        break
        
        
        
        


