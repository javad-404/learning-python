import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5
    
    
def help_game(user_guess, computer_number):
    if user_guess == computer_number:
        return "You got it!"
    elif user_guess > computer_number:
        return "Too high"
    elif user_guess < computer_number:
        return "Too low" 
  
  
computer_number = random.randint(1, 100)   
turns = set_difficulty()
user_guess = 0

while user_guess != computer_number:
    print(f"You have {turns} attempts remaining to guess the number.")
    user_guess = int(input("Guess it: "))
    
    print(help_game(user_guess, computer_number))
   
    if user_guess != computer_number:
        turns -= 1
        if turns == 0:
            print("You've run out of guesses, you lose")
            print(f"The answer was {computer_number}.")
            break
    
        
    
    







    
