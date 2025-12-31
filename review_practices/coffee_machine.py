MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def check_resources(order_ingredients):
    for item in order_ingredients:
        amount_needed = order_ingredients [item]
        amount_available = resources [item]
        
        if amount_available < amount_needed :
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
        
        
def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    
    else:
        change = money_received - drink_cost
        change = round(change, 2)
        profit += drink_cost
        if change > 0:
            print(f"here is change {change}")
        return True
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")
             
   
while True : 
    user_choice = input ("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        break
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        drink_ingredients = drink["ingredients"]
        
        if check_resources(drink_ingredients):
            print("Resources are sufficient! (Next step: Payment)")
            payment = process_coins()
            print(f"All of your money is {payment} ")
            price = drink["cost"]
            if is_transaction_successful(payment, price ):
                make_coffee(user_choice, drink_ingredients)
            
        
        
        
        
