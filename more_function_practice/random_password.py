import random 
string = "123456789/*0.-+!@#$%^&*()_+qwertyuiop[]\|}{P';lkjhgfdsazxcvbnm,./?><MNBVCXZASDFGHJKL:|}{POIUYTREWQ"

def generate_password(length):
    password = ""
    for i in range(length):
        my_char = random.choice(string)
        password+= my_char
    return password
user_pass= int(input("pls tell me the password length: "))
result = generate_password(user_pass)
print (f"your new password is {result}")
        
        

