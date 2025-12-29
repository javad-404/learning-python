import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
=========
''']
word_list = ["Lion", "Wolf", "camel", "Cristiano"]
chosen_word = random.choice(word_list).lower()
word_len = len(chosen_word)

display = []
for i in range(word_len):
        display.append("_")
print("Let's play Hangman!")
print(display) 
     
        
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Pls just guess a letter: ").lower()
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            
   
    for position in range(word_len):
        letter = chosen_word[position]
        if guess == letter:                      
            display[position] = letter
    print(f"Current word: {display}")
    print(stages[lives])
    
    if "_" not in display:
        end_of_game = True
        print("You won")
        
   

        
