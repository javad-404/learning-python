class Book:
    def __init__(self,name,page):
        self.name = name
        self.page = page
        
    def opening(self):
        print(f"our {self.name} book has {self.page} pages")

class Darsi(Book):
    def __init__(self, name, page, reshte, paye):
        Book.__init__(self, name, page)
        self.reshte = reshte
        self.paye = paye
    def opening(self):
        print(f"the {self.name} of {self.reshte} in {self.paye}")
        
d= Darsi("fizik", 200, "dovom", 6)
d.opening()
    