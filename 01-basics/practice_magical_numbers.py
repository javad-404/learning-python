n = input ("pls enter an integer: ")
n = int (n)

if (n % 3 == 0) and (n % 5 ==0) :
    print(f"oh {n} is legend!")
elif n % 3 == 0 :
    print (f"oh {n} is magical!")
elif n % 5 ==0:
    print (f"oh {n} is cursed!")
else:
    print(f"oh {n} is normal!")