def divide(a, b):
    try:
        return  a / b
    except ZeroDivisionError:
        print("you cant divide on zero")
        return None
    except Exception as e:
        print(f"anothr error:{e}")
        return None
    
while True:
    try:    
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        Result = divide(num1, num2)
        if Result is not None:
            print(f"result:{Result}")
            break
        else:
            print("try again")
    except ValueError:
        print("you need to enter numbers")
    finally:
        print("the progragram is run seccesfully")
        
    
        
