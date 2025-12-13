
def calculate_fare(km, is_night):
    entrance = 10000
    per_km = 2000
    first_km = 3
    total = 0
   
    if km <= 3 and is_night == False:
        total = entrance
    elif km <= 3 and is_night == True:
        total = entrance + (entrance*(0.2))
    elif km > 3 and is_night == False:
        total = entrance + ((km-first_km) * per_km)
    elif km > 3 and is_night == True:
        total1 = entrance + ((km - first_km) * per_km)
        total = total1 + (total1*(0.2))
    return int(total)

        
x = int(input("what is your distance? "))
y = input("is it night? (Y/N)")
if y.upper() in ["Y", "YES"]:
    check_night = True
else:
    check_night = False
final = calculate_fare(x, check_night)
print(f"final price is {final} toman")

