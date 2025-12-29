alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, cipher_direction):
    shift_amount = shift_amount % 26
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount = -1 * shift_amount
        
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = shift_amount + position
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
            
    return cipher_text
    
    
    
direction = input("Do you want Encode or Decode? \n").lower()
text = input("what is your masseage? \n").lower()
shift = int(input("How many to shift? \n"))

print(caesar(text, shift, direction))


