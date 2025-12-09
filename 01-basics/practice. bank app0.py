password = 1234
cash = 500000
history = []
tries = 0

print("**** Bank App *****\n")

while tries < 3:
    user_pass = int(input("ENTER PASS: "))
    
    if user_pass == password:
        print("\n--- WELCOME ---")
        
        while True:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Balance & History")
            print("4. Exit")
            
            choice = int(input("Select (1-4): "))

            if choice == 1:
                amount = int(input("Amount to withdraw: "))
                
                if amount > cash:
                    print("Error: Not enough money!")
                elif amount % 10000 != 0:
                    print("Error: Amount must be multiple of 10,000")
                else:
                    cash -= amount
                    history.append(f"Withdraw: {amount}")
                    print(f"Success! New Balance: {cash}")

            elif choice == 2:
                amount = int(input("Amount to deposit: "))
                cash += amount
                history.append(f"Deposit: {amount}")
                print(f"Success! New Balance: {cash}")

            elif choice == 3:
                print(f"\nCurrent Cash: {cash}")
                print(f"History: {history}")

            elif choice == 4:
                print("Good Bye!")
                break
            
            else:
                print("Invalid input! Try again.")

        break 

    else:
        print("Incorrect Password!")
        tries += 1

if tries == 3:
    print("\nCARD BLOCKED!")