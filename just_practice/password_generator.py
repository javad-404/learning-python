import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []

print("Welcome to the PyPassword Generator!")
try:
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for i in range(nr_letters):
        x = random.choice(letters)
        password_list.append(x)
    for i in range(nr_symbols):
        x = random.choice(symbols)
        password_list.append(x)
    for i in range(nr_numbers):
        x = random.choice(numbers)
        password_list.append(x)
    random.shuffle(password_list)
    password =''.join(password_list)
    print(f"your password is:{password}")
    
except ValueError:
    print("you need to enter numbers!")