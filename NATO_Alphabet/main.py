import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter : row.code  for (index, row) in data.iterrows()}
while True:
    try:
        user_word = input("Enter a world i will give phonetic pass: ").upper()
        user_phonetic = [phonetic_dict[letter] for letter in user_word]
        print(user_phonetic)
        break
    except KeyError:
        print("you have an error try again")
       

    

