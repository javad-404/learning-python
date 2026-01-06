from tkinter import *

class Contractcalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Contract Calculator")
        self.window.minsize(width=500, height= 500)
        self.window.config(padx= 20, pady=20, bg="#F1E9E9")
        
        self.label_name = Label(self.window, text="Name:", font=("Arial", 10, "bold"))
        self.label_name.grid(row=0 , column=0, sticky="w")
        self.entry_name = Entry(width=30)
        self.entry_name.grid(row=0, column=1, ipady=3)
        
        
        self.label_money = Label(self.window, text="Amount:", font=("Arial", 10, "bold"))
        self.label_money.grid(row=1, column=0, sticky="w")
        self.entry_money = Entry(width=30)
        self.entry_money.grid(row=1, column=1, ipady=3)
        
        self.label_installments = Label(self.window, text="Number of Installments:", font=("Arial", 10, "bold"))
        self.label_installments.grid(row=2, column=0, sticky="w")
        self.entry_installments = Entry(width=30)
        self.entry_installments.grid(row=2, column=1, ipady=3)
        
        self.calc_button = Button(
            self.window,
            text="Calculate & Register",
            command=self.calculate_all,
            padx=10,
            pady=5,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10, "bold")
            )
        self.calc_button.grid(row=3, column=1, pady=10, sticky="ew")
        
        self.reset_button = Button(self.window,
            text="Rset All",
            command=self.reset_all,
            padx=10,
            pady=5,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10, "bold")
                                   )
        self.reset_button.grid(row=4, column=1, pady=10, sticky="ew")
        
        
        self.result_label = Label(self.window, 
            text="", 
            font=("Arial", 11), 
            fg="blue", 
            justify="left", 
            anchor="w")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=20, sticky="w")
    
    def reset_all(self):
        self.entry_name.delete(0, END)
        self.entry_money.delete(0, END)
        self.entry_installments.delete(0, END)
        self.result_label.config(text="")
        
    def get_tax_calculation(self):
        raw_money = float(self.entry_money.get())
        installments = int(self.entry_installments.get())
        
        if raw_money < 0 or installments <= 0:
            raise ValueError("Numbers must be positive and installments > 0")
            
        total = raw_money * 1.09
        each = total / installments
        
        return total, each, installments

    def calculate_all(self):
        try:
            name = self.entry_name.get()
            total, each, inst = self.get_tax_calculation()
            result_text = (f"Project: {name}\n"
                           f"Total (with tax): {total:,.0f} Rials\n"
                           f"Each Installment ({inst}): {each:,.0f} Rials") 
            self.result_label.config(text=result_text, fg="blue")

        except ValueError as err:
            self.result_label.config(text=f"Error: {err}", fg="red")
        except ZeroDivisionError:
            self.result_label.config(text="Error: Cannot divide by zero!", fg="red")
        except Exception as e:
            self.result_label.config(text=f"Unexpected Error: {e}", fg="red")
        finally:
            print(f"Process finished for project: {self.entry_name.get()}")         
            
root = Tk()
app = Contractcalculator(root)
root.mainloop()
