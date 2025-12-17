def save_score(name, score):
    with open ("scores.txt", "a") as f:
        f.write(f"{name} : {score}\n")
    print("Record Saved")
    
def show_leaderboard():
    with open ("scores.txt", "r") as f:
        try:
            content = f.read()
            print("\n--- SCORES ---")
            print(content)
            print("--------------")
        except FileNotFoundError:
            print("file not created yet!")

while True:
    name = input("name: (list / exit) ")
    
    if name.upper() == "EXIT":
         break
    elif name.upper() == "LIST":
        show_leaderboard()
    
    else:
        try:
            score = int(input("score: "))
            save_score(name, score)
        except ValueError:
            print(" Score bayad adad bashe!")
        


