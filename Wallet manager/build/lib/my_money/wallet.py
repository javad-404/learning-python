class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.transactions = []
        
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
        print(f"{amount} deposited. New Balance: {self.balance}")
        
        
    def withdraw(self, amount):
        amount = int(amount)
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
            print(f"{amount} Withdrawed. New balance:{self.balance}")
        else:
            print("you dont have enough money")
    
    def show_history(self):
            if len(self.transactions) == 0:
                print("No transactions yet")
                return
            for trans in self.transactions:
                print(trans)
                
my_wallet = Wallet("Javad")


my_wallet.deposit(5000)
my_wallet.deposit(2000)


my_wallet.withdraw(3000)
my_wallet.withdraw(10000) 


print("\n")
my_wallet.show_history()
        
                                 
        