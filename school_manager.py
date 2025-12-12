classroom= {}

def add_student():
    print ("\n--- ADD NEW STUDENT ---")
    name = input("enter name: ")
    score = int(input("enter score (0-20): "))
    if 0<= score <=20 :
        classroom[name]= score
        print (f"Done! Added {name} with score {score}")
    else :
        print ("Error, score must be between 0 and 20")

def check_status(name):
    if name in classroom:
        student_score = classroom[name]
        
        if student_score >= 10:
            return "pass"
        else:
            return "faile"
    else:
        return "student not find"
def find_top_student():
    if len(classroom)==0:
        return "classroom is empty", 0
    
    top_name = max(classroom, key=classroom.get)
    top_score = classroom[top_name]
    return top_name, top_score
def show_menu():
    print("\n======== SCHOOL MENU ========")
    print("1. Add Student")
    print("2. Check Status")
    print("3. Find Top Student")
    print("4. Exit")
    choice = int(input("Please choose (1-4): "))
    return choice
while True:
    user_choice = show_menu()
    
    if user_choice == 1:
        add_student()
    elif user_choice == 2:
        who = input("Enter student name to check: ")
        result = check_status(who)
        print(f"status of {who} is {result}")
    elif user_choice == 3 :
        name, score = find_top_student()
        print (f"top student is {name} with score {score}")
    elif user_choice == 4:
        print("goodbye manager!")
        break
    else:
        print("Invalid option!")
        
    
    
