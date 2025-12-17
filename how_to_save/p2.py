def add_task(text, priority):
    with open ("todo.txt", "a") as f:
        f.write(f"[{priority}] : {text} \n")
    print ("Saved!")
    
    
def show_tasks():
    try:
        with open ("todo.txt", "r") as f:
            content = f.read()
            print("\nMy ToDo list")
            print(content)
            print("______________________________________")
    except FileNotFoundError:
        print("file not found")
        
        
def search(word):
    try:
        with open ("todo.txt", "r") as f:
            lines = f.readlines()
            count = 0
            
            for line in lines:
                if word in line:
                    print(f"{line.strip()}")
                    count +=1
            if count == 0:
                print("Hichi peyda nashod!")
    except FileNotFoundError:
        print(" File nist ke begardam!")
       

while True:
    text = input("task name(view/Exit/search): ")
    
    if text.upper() == "EXIT":
        break
    elif text.upper() == "VIEW":
        show_tasks()
    elif text.upper() == "SEARCH":
        word = input("what do you want to search? ")
        search(word)
    else:
        priority = input("priority(high/low): ")
        add_task(text, priority)
        print("unavaible value")
            
    
    