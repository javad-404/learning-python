import mylibrary



if __name__ == "__main__":
    
    my_lib = mylibrary.Library()
    
    while True:
        print("="*30)
        print("      Menu")
        print("1:add book")
        print("2:remove book")
        print("3:search book")
        print("4:show book")
        print("5:Exit book")
        
        try:
            user_choice = int(input("select one: "))
        except ValueError:
            print("you need to enter numbers")
            continue
         
        if user_choice == 1:
                title = input("what is the title? ")
                author = input("what is the author name? ")
               
                my_lib.add_book(title, author)
        elif user_choice == 2:
            title = input("enter title to remove ")
            my_lib.remove_book(title)
        elif user_choice == 3:
            title = input("enter title to search ")
            my_lib.search_book(title)
        elif user_choice == 4:
            my_lib.show_books() 
        elif user_choice == 5:
            print("bye")
            break
        else:
            print("you must enter between 1-5 ")




    
            
                
            
    


