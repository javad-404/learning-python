def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 

operations = {"+": add, "-":subtract, "*":multiply, "/":divide}

def calculator():
    n1 = float(input("num1: "))  
    
    should_continue = True
    while should_continue:  
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("num2: "))

        calculation_function = operations [operation_symbol]
        
        answer = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        user_answer = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if user_answer == "y":
            n1 = answer 
        else:
            should_continue = False
            calculator()
            
calculator()
        
        
    
