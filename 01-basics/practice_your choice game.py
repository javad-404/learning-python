hp = 100
gems = 0
inventory = []

while hp > 0 :
    if gems == 5:
        print("you won!!!!!!")
        break
    print (f"your helath is {hp} and  your diamonds is {gems}")
    print ("if you choose 1 you will lose 15 hp")
    print ("if you choose 2 you will get 1 diamond")
    print ("if you choose 3 you will find an apple")
    print ("if you choose 4 you will get in store")
    choice = int(input("pls choose your roll between (1 , 4)\n"))
   
    if choice == 1 :
        hp-=15
        print("you lost 15 hp")
    elif choice == 2:
        gems+= 1
        print("you found a diamond!")
    elif choice == 3:
        inventory.append("apple")
        print ("you got an apple!! nice")
    elif choice == 4 :
        if gems >= 2:
            gems-=2
            hp+=20
            inventory.append("potion")
        else:
            print ("you dont have enough gems")
    else:
        print("you didnt choose correct number! pls try again")
if hp <=0:
    print("!!!!GAME OVER!!!!")
apples = [x for x in inventory if x =="apple"]
print("\n--- Final Inventory ---")
print(f"Total Apples collected:{len(apples)}")
print(f"Full Inventory: {inventory}")
   
    