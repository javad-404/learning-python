from tkinter import *

class Contractcalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Contract Calculator")
        self.window.minsize(width=500, height= 500)
        self.window.config(padx= 20, pady=20)
        
        Label(self.window,text="Contractor Name:",font=("Arial",10 ,"bold")).pack()
        self.input_name = Entry(width=30)
        self.input_name.pack()
        
        
        Label(self.window, text="Amount (Rials):", font=("Arial", 10, "bold")).pack()
        self.input_money = Entry(width=30)
        self.input_money.pack()
        
        Label(self.window, text="Number of Installments:", font=("Arial", 10, "bold")).pack()
        self.input_installments = Entry(width=30)
        self.input_installments.pack()
        
        self.calc_button = Button(self.window, text="Calculate & Register", command=self.calculate_all)
        self.calc_button.pack(pady=10)
        
        self.result_label = Label(self.window, text="", font=("Arial", 11), fg="blue")
        self.result_label.pack(pady=20)
        
    def calculate_all(self):
        try:
            name = self.input_name.get() 
            raw_money = float(self.input_money.get())
            num_installments = int(self.input_installments.get())
            
            total_with_tax = raw_money * 1.09
            each_installment = total_with_tax / num_installments
            
            result_text = (f"Project: {name}\n"
                           f"Total (with tax): {total_with_tax:,.0f} Rials\n"
                           f"Each Installment ({num_installments}): {each_installment:,.0f} Rials")   
    
            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Error: Please enter valid numbers!", fg="red")
            
root = Tk()
app = Contractcalculator(root)
root.mainloop()
