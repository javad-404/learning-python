class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_info(self):
        print(f"my name is {self.name} and im {self.age} old")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,  age)
        self.grade = grade
    
    def show_status(self):
        if self.grade > 17 :
            return "Excellent"
        elif self.grade < 12:
            return 'Needs help'
        else:
            return "Good"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        print(f"im teaching {self.subject}")
        
        
def main():
    s1 = Student("ali", 20, 15)
    t1 = Teacher("reza", 45, "math")
    
    print("--- info ---")
    s1.show_info()
    t1.show_info()
    
    print("\n--- actions ---")
    
    status = s1.show_status()
    print(f"Student status is {status}")
    
    t1.teach()
    
main()
    
        
        
    