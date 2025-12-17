def add_note(text):
    with open ("notes.txt", "a") as f:
        f.write(f"{text}\n")
        
    print("Done!")
    
    
def show_note():
    try:
       with open ("notes.txt", "r") as f:
           content = f.read()
           print(content)
    except FileNotFoundError:
        print("File not found")
            
    
while True:
    text = input("type any thing your ass want(type exit to exit): ")
    if text.upper() == "EXIT":
        break

    elif text == "view":
        show_note()
    
    else:
        add_note(text)
    
