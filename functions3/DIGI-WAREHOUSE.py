def add_product(name, price, count):
    if name in inventory:
        inventory[name]["count"]+= count
    else:
        inventory [name] = {"price":price, "count": count}
    print("Updated")
    
    
def sell_product(name, count):
    if name not in inventory:
        print("Not found")
        return
    if count > inventory[name]["count"] :
        print("Not enough stock")
    else: 
        inventory[name]["count"] -= count
        print("sold")
        
        
def get_total_value():
    total_sum= 0
    
    
    for name, data in inventory.items():
        p = data["price"]
        c = data ["count"]
        total_sum += p * c
    return total_sum


def check_low_stock(threshold):
    low_items= []
    for name, data in inventory.items():
        count = data['count']
        if count < threshold:
            low_items.append(name)
    return low_items


inventory = {
    "laptop": {"price": 50000, "count": 10},
    "mouse": {"price": 500, "count": 100},
}


while True:
    print("--- WELLCOME! ---")
    print("this is our store products")
    print(inventory)
    print("1: add_product")
    print("2: sell_product")
    print("3: get_total_value")
    print("4: check_low_stock")
    print("5: Exit")
    print()
    user_choice = int(input('pls select one(1-5): '))
    if user_choice < 1 or user_choice > 5:
        print("wrong number! try again")
        continue
        
    if user_choice == 1:
        print("new product!")
        name = input("what is the product name? ")
        price = int(input("what is the product price? "))
        count = int(input("what is the product count? "))
        add_product(name, price, count)
    elif user_choice == 2:
        name = input("what product do you want to buy? ")
        count = int(input("how much do you want? "))
        sell_product(name, count)
    elif user_choice == 3:
        total = get_total_value()
        print(f"our total value is {total}")
    elif user_choice == 4:
        limit = int(input("Enter limit number: "))
        items = check_low_stock(limit)
        print(f"Low stock items: {items}")
    elif user_choice == 5:
        print("Bye!")
        break
    
        
        
        
            
            
    
        
        
        
        
    
        
        
        
    
    
    
    
    
    
   
        
   
            
        
    
    

        
        
        
        
        
        
        
        
    
        
        
        
     
        


















