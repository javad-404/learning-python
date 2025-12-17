def Add_book(book, nevisande):
    with open ("books.txt", "a") as f:
        f.write(f"{book} : {nevisande}\n")
    print("Added")
    
    
def search(book):
    try:
        with open("books.txt", "r") as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                if book in line:
                    print(f"{line.strip()}")
                    count += 1
            if count == 0 :
                print("Hichi peyda nashod!")
    except FileNotFoundError:
        print("File nist ke begardam")
        
        
def Count_Books():
    try:
        with open ("books.txt", "r") as f:
            lines = f.readlines()
            count = len(lines)
            print(f"we have {count} books")
            
    except FileNotFoundError:
        print("File nist ke beshmaram")
        

def Clear_Library():
        with open ("books.txt", "w") as f:
            pass
        print("pak shod!")
            

while True:
    print("___ Library App ___")
    print("1:Add book")
    print("2:Search")
    print("3:Count books")
    print("4:Clear library")
    print("5: Exit")
    try:
        user_choice = int(input("please select (1-5): "))
    except ValueError:
        print(" Lotfan adad vared konid!")
        continue
    
    if user_choice == 1:
        book = input ("book name? ")
        nevisande = input("nevisande name? ")
        Add_book(book, nevisande)
    elif user_choice == 2:
        name = input("what do you want to search? ")
        search(name)
    elif user_choice == 3:
        Count_Books()
    elif user_choice == 4:
        Clear_Library()
    elif user_choice == 5:
        print("Good bye!")
        break
    else:
        print("Adad bayad beine 1 ta 5 bashe.")
        
        
        
        
        
    
    




        
                
                
        
    

