from random import randint


def generate_secret_number():
    computer_guess = randint(1, 100)
    return computer_guess


def get_user_guess():
    while True:
        try:
            user_guess = int(input("guess my secret number friend? "))
            return user_guess
        except ValueError:
            print("you have to enter a number")
            
    
    
def check_guess(secret, guess):
    if secret == guess:
        print("wooow you won")
        return True
    if secret > guess:
        print("boro balatar...")
        return False
    else:
        print("bia payintar...")
        return False
    
    
def play_game():
    max_tries = 7
    tries = 0
    cg = generate_secret_number()
    print(f"--- Game Shoro Shod! {max_tries} ta joon dari ---")
    
    while tries < max_tries:
        user_guess = get_user_guess()
        check = check_guess(cg, user_guess)
        if check :
            print(f"Barandeh shodi tooye {tries + 1} harakat!")
            break
        else: 
            tries += 1
            print(f"Joon baghi mande: {max_tries - tries}")
    if tries == max_tries:
        print("\nGame Over! You Lost.")
        print(f"Number was: {cg}")
        
            
play_game()
            
            
    
    
        
        
        
        
    
    
    
        
        
    
    
   
 

