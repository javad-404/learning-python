def save_contact(name, phone):
    with open ("contacts.txt", "a") as f:
        contact = f"{name}:{phone}\n"
        f.write(contact)
        print("Contact Saved.")


def find_number(target_name):
    try:
        with open ("contacts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    if parts[0] == target_name:
                        return parts[1]
                
            return "Not found"
    except FileNotFoundError:
        return "file not created yet"
    
    
def delete_contact(target_name):
    lines = []
    try:
        with open ("contacts.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return "File not found."
    new_lines = []
    found = False
    for line in lines:
        parts = line.strip().split(":")
        if parts[0] == target_name:
            found = True
        else:
            new_lines.append(line)
    if found:
        with open("contacts.txt", "w") as f:
            for line in new_lines:
                f.write(line)
            return "Deleted successfully."
    else:
        return "Contact not found."
    

def edit_contact(target_name, new_phone):
    lines =[]
    try:
        with open ("contacts.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return "File not found"
    new_lines = []
    found = False
    for line in lines :
        parts = line.strip().split(":")
        if parts[0] == target_name:
            found = True
            updated_name = f"{target_name}:{new_phone}\n"
            new_lines.append(updated_name)
        else:
            new_lines.append(line)
        if found:
            with open("contacts.txt", "w") as f:
                for line in new_lines:
                    f.write(line)
            return "Updated successfully"
        else:
            return "Contact not found."
        
              
def main():
    while True:
        print("="*30)
        print("        menu")
        print("1: Save contant")
        print("2: Search contant")
        print("3: Delete contact")
        print("4: Edit contant")
        print("5: Exit")
        
        try:
            user_choice = int(input("select one: "))
        except ValueError:
            print("you need to enter a number(1-5)")
            continue
        
        if user_choice == 1:
            while True:
                name = input("Enter name: ")
                if name.replace(" ", "").isalpha():
                    break
                else:
                    print("Error: Numbers not allowed! Please enter text only.")
        
            while True:
                phone = input("Enter number: ")
                if phone.isdigit():
                    break
                else:
                    print("Error: Please enter digits only (0-9).")
    
            save_contact(name, phone)
            
            
            
        elif user_choice == 2:
            while True:
                target_name = input("Enter name to search: ")
                if target_name.replace(" ", "").isalpha():
                    break
                else:
                    print("Text only.")
                    
            result = find_number(target_name)
            print(f"Result: {result}")
            
            
        elif user_choice == 3:
            while True:
                target_name = input("Enter name to delete: ")
                if target_name.replace(" ", "").isalpha():
                    break
                else:
                    print("Text only.")
            print(delete_contact(target_name))
        
        
        elif user_choice == 4:
            while True:
                target_name = input("Enter name to edit: ")
                if target_name.replace(" ", "").isalpha():
                    break
                else:
                    print("Text only.")
            while True:
               new_phone = input("Enter number: ")
               if new_phone.isdigit():
                   break
               else:
                   print("Error: Please enter digits only (0-9).")
    
            print(edit_contact(target_name, new_phone))
            
        elif user_choice == 5:
            print("Bye!")
            break
        else:
            print("You need to select between (1-5)")
            
main()
          
            
        
        