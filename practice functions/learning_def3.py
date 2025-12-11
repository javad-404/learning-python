def character_numbers (s, c):
    '''
this function take the name and give u the number of each character you desire.
    '''
    counter = 0
    for this_character in s:
        if this_character == c:
            counter+=1
    return (counter)
name = "javad jijanij"
show = character_numbers(name, "j")
print(f"{name} has {show} character of J")
        
        
    