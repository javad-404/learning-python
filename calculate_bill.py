
prices = {
    'apple': 50,
    'banana': 30,
    'milk': 100,
    'bread': 40
}
cart = ['apple', 'milk', 'apple', 'cheese', 'bread', 'chips']
def calculate_bill (system_prices, customer_cart):
    unlisted = []
    total = 0
    for item in customer_cart:
        if item in system_prices:
            total+= system_prices[item]
        else:
            unlisted.append(item)
    
    return total , unlisted
total_price, unknown_price = calculate_bill(prices, cart)
print(f"Total Bill: {total_price}")
print(f"Unknown Items: {unknown_price}")
            
        

