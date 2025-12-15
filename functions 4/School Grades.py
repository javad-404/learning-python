grades = {} 


def add_grade(lesson_name, score):
    if 0 <= score <= 20:
        grades[lesson_name]= score
        print("new grade added!")
    else:
        print("Invalid score")
        
        
def calculate_average():
    if len(grades) == 0:
        return 0
    total_sum = 0
    for name,score in grades.items():
        total_sum += score 
    final_avg = total_sum / len(grades)
       
    return final_avg


while True:
    print("--- wellcome ---")
    print("1: add_grade ")
    print("2: calculate_average")
    print("3: show_all")
    print("4: exit")
    try:
        user_choice = int(input("pls selece one(1-4): "))
    except ValueError:
        print("pls enter a number")
        continue
    
    if user_choice == 1:
        user_lesson = input("what is the lesson name?")
        user_score = int(input("what is the score? "))
        add_grade(user_lesson, user_score)
    elif user_choice == 2:
       avg = calculate_average()
       if avg >= 10:
           print(f"Pass! Average:{avg}")
       else:
           print(f"Fail! Average:{avg}")
           
    elif user_choice == 3:
        print(f"karname to hast:\n{grades}")
              
              
    elif user_choice == 4:
         print("Bye!")
         break
    else:
        print("wrong number")
    
    
        
        
        