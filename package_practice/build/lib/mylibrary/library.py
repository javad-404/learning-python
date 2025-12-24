


class Library:
    def __init__(self):
        self.books = []
    
    
    def add_book(self, title, author):
        new_book = f"title:{title}, author:{author}"
        self.books.append(new_book)
        
        
    def remove_book(self, title):
         for book in self.books:
             if book["title"] == title:
                 self.books.remove(book)
             print(f" book {title} deleted")
             return
         print("Book not found.")
         
         
    def search_book(self,title):
        for book in self.books:
            if book["title"] == title:
                print(f"book {title} found")
                return
        print(f"'{title}' is not in the library.")
        
    def show_books(self):
        if len(self.books) == 0:
            print("There is not any book")
            return
        print("--- List of Books ---")
        for book in self.books:
            print(f"Book:{book["title"]} | Author:{book["author"]}")
        
                
             
                 
        