donations = {'javad' : 500,
             'sara' : 250,
             'reza' : 269,
             'mahi' : 100
    }
def donation_analisys (don):
    total = 0
    count = 0
    max_donation = -1
    person = ''
    for name, value in don.items():
        total += value
        count += 1
        if max_donation < value :
            person = name
            max_donation = value
    avrage = int (total / count)
    return avrage , total , person
    
    
avg , total , max_don = donation_analisys (donations)
print (f"total donation is {total}")
print (f"avrage of donation is {avg}")
print (f'thanks to {max_don} to the most donation')