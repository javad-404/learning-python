accounts = {'ali': 1000, 'sara': 2000}
transaction_history = []
current_user = None

#---Decorators---
def login_required(func):
    def wrapper(*args, **kwargs):
        if current_user is None:
            return "Error: Please login first"
        return func(*args, **kwargs)
    return wrapper

def log_transaction(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        user_name = current_user
        if user_name:
            transaction_history.append(f"User {user_name} run {func_name}")
        else:
            transaction_history.append(f"Unknown User ran {func_name}")
        result = func(*args, **kwargs)
        return result
    return wrapper

# --- Core Functions ---
def login(username):
    global current_user 
    if username in accounts:
        current_user = username
        print(f"Welcome back, {username}")
    else:
        print("Username not found.")
        
        
def logout():
    global current_user 
    print(f"Goodbye {current_user}")
    current_user = None
    
    
@login_required    
@log_transaction
def deposit(amount):
    accounts [current_user] += amount
    return f"Deposit successful! New balance: {accounts[current_user]}"


@login_required
@log_transaction
def withdraw(amount):
    if accounts [current_user] >= amount:
        accounts[current_user] -= amount
        return f"Withdraw successful! new balance: {accounts[current_user]}"
    else:
        return f"You dont have enough money"

# --- Main Interface ---
if __name__ == "__main__":
    while True:
        print("\n" + "="*30)
        status = f"Logged in as: {current_user}" if current_user else "Not Logged in"
        print(f"SMART BANK ({status})")
        print("1:Login")
        print("2:Deposit")
        print("3:Withdraw")
        print("4:Transaction history")
        print("5:Logout")
        print("6:Exit App")
        
        try:
            user_choice = int(input("select one: "))
        except ValueError:
            print("You need to enter numbers")
            continue
        
        
        if user_choice == 1:
            name = input("Enter username: ")
            login(name)
            
                
        elif user_choice == 2:
            try:
                amount = int(input("How much deposit? "))
                print(deposit(amount))
            except ValueError:
                print("Deposit must be number!")
                
                
        elif user_choice == 3:
            try:
                amount = int(input("How much withdraw? "))
                print(withdraw(amount))
            except ValueError:
                print("Withdraw must be number!")
                
                
        elif user_choice == 4:
            print("\nTransaction History:")
            for log in transaction_history:
                print(log)
           
        
        elif user_choice == 5:
            logout()
            
        
        elif user_choice == 6:
            print("Shutt down")
            break
            
        else:
            print("you need to enter between 1-6")
            
        
        
            
        
            
                
    


    
    
    
    
    
    
        
