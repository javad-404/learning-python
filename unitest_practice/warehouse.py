def update_inventory(inventory, item_name, quantity):
    if not isinstance(item_name, str):
        raise TypeError("Item name must be a string")
    
    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer")
    
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    
    if item_name in inventory:
        inventory[item_name] += quantity
        
    else:
        inventory [item_name] = quantity
        
    return inventory

