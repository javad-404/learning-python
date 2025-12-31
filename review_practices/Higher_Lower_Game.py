data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    }
]
import random

def format_data(account):
    name = account["name"]
    description = account['description']
    country = account ["country"]
    return f"{name} a {description} from {country}"


def check_answer(guess, a_followers, b_followers):
    if guess == "A" and a_followers >= b_followers:
        return True
    elif guess == "B" and b_followers >= a_followers:
        return True
    else:
        return False       
    
account_a = random.choice(data)
account_b = random.choice(data)

while account_a == account_b:
    account_b = random.choice(data)

game_should_continue = True
score = 0
print("Welcome to Higher Lower Game!")

while game_should_continue:
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")
    
    user_guess = input("who has more follwer A or B? ").upper()
    a_followers = account_a ["follower_count"]
    b_followers = account_b ["follower_count"]

    is_correct = check_answer(user_guess, a_followers, b_followers)
    
    print("\n" * 20)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_b
        account_b = random.choice(data)
        
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
        




    
    