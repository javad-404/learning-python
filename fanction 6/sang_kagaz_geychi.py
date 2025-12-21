import random


def get_computer_choice():
    x = ['s', 'k', 'g']
    computer_guess = random.choice(x)
    return computer_guess


def get_user_choice():
    while True:
            user_choice = input("(s)ang, (k)aghaz, (g)heychi? ").lower()
            if user_choice in ["s", "k", "g"]:
                return user_choice
            else:
                print("wrong value faghat s, k, ya g benevis")
                
                
def determine_winner(user, computer):
    if user == computer:
        return "draw"
    if (user == "s" and computer == "g") or (user =="g" and computer== "k") or (user == "k" and computer == "s"):
        return "user"
    else:
        return "computer"
   
        
def play_game():
    user_score = 0
    computer_score = 0
   
    while user_score < 3 and computer_score < 3:
        gcc = get_computer_choice()
        guc = get_user_choice()
        print(f"Computer chose: {gcc}")
        winner = determine_winner(guc, gcc)
        if winner == "user":
            user_score += 1
            print("You won this round!")
        elif winner == "computer":
            computer_score += 1
            print(" Computer won this round!")
        else:
            print("No win this time")
        print(f"Score -> You: {user_score} | PC: {computer_score}")
        print("-" * 30)
    if user_score == 3 :
        print("\nCONGRATS! You won the match!")
    else:
        print("\nGAME OVER! Computer won the match")
        
         
          
play_game()
            
            
        
        
            
        
        
    

    
    
  