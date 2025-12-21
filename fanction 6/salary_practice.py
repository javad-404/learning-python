def calculate_base_pay(hours, rate):
    if hours <= 160:
        base = hours * rate
        return base
    else:
        base1 = (hours- 160) * rate * 1.5
        base2 = 160 * rate
        base = base1 + base2
        return base  
    
    
def calculate_tax(gross_pay):
    if gross_pay < 10000000:
        tax = 0
        return tax
    elif 10000000 <= gross_pay <= 20000000:
        tax = gross_pay * 0.1
        return tax
    else:
        tax = gross_pay * 0.2
        return tax
    
    
def calculate_insurance(gross_pay):
    return gross_pay * 0.07


def calculate_net_salary(gross, tax, insurance):
    salary = gross - (tax + insurance)
    return salary


def main():
    try:
        hours = int(input("how many do you worked? "))
        rate = int(input("what is your payment per hour? "))
    except:
        print("pls enter numbers")
        return
    base = calculate_base_pay(hours, rate)
    tax = calculate_tax(base)
    insurance = calculate_insurance(base)
    salary = calculate_net_salary(base, tax, insurance)
    print("\n" + "*" * 30)
    print("     Salary Slip")
    print(f"Gros :{int(base):,}")
    print(f"Tax :{int(tax):,}")
    print(f"Insurance :{int(insurance):,}")
    print("-" * 30)
    print(f"Salary :{int(salary):,}")
    print("*" * 30)
    
main()   
    

        
        
        
        
        
        