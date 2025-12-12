import random


def welcome():
    print("wellcome to this funny game")
    print("I will guess a number between 1 and 20")
    print("you have to guess it!")
    print("lets try it...")
    print()
    
    
def finish(number, count):
    print("good game!")
    print(f"my number was {number} and you found it in {count} guesses")
    wanamore= input("Do you want play again?(Y/N)")
    if wanamore.upper() in ["Y" , "YES", "ARE"]:
        return True
    else:
        return False
    
    
def win(computer_number, geuss):
    return computer_number == geuss
       

def get_a_geuss():
    user_geuss = int(input("what is your guess? "))
    return user_geuss


def answer (computer, user):
    if computer > user :
        return "my number is larger"
    elif computer < user :
        return  "my number is smaller"
    else:
        return "WooooW you won! good guess!"

welcome()
continue_playing = True
while continue_playing:
    computer_number = random.randint(1, 20)
    geuss = 0
    count = 0
    while (not win(computer_number, geuss)):
        count += 1
        geuss = get_a_geuss()
        print (answer(computer_number, geuss))
        
    continue_playing= finish(computer_number, count)
        

