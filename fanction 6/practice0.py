def average(score_1, score_2, score_3):
    return (score_1 + score_2 + score_3) // 3


def grade(average):
    if average > 17:
        return("A")
    if  15 <= average <= 17:
        return("B")
    if average < 15:
        return("C") 

def status(average):
    if average >= 10:
        return("Pass!")
    if average < 10:
        return("Faile")
        
        
def print_sheet(score_1, score_2, score_3):
    average_1 = average(score_1, score_2, score_3)
    print(f"moadel shoma hast {average_1}")
    grade_1 = grade(average_1)
    print(f"Grade shoma hast {grade_1}")
    status_1 = status(average_1)
    print(f"status shoma hast {status_1}")
    

try:
    score_1 =int(input("what is your math score? "))
    score_2 =int(input("what is your science score? "))
    score_3 =int(input("what is your history score? "))
    if not (0 <= score_1 <=20) or not (0 <= score_2 <=20) or not (0 <= score_3 <=20):
        print("you need to enter between (0-20)")
    else:
        print_sheet(score_1, score_2, score_3)
    
except ValueError:
    print("you should enter a number")


    
    




    
    
    