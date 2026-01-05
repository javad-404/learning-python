from tkinter import *


class ContractManager():
    def __init__(self, window):
        self.window = window
        self.window.title("Contract Management system")
        self.window.minsize(width=300, height=300)
        self.window.config(padx=20, pady=20)

        self.label = Label(self.window, text="Contractor Name: ", font=("Arial", 10, "bold"))
        self.label.pack()

        self.button = Button(self.window,text="sign contract", command= self.button_clicked)
        self.button.pack()

        self.reset = Button(self.window, text="Reset", command = self.reset_clicked)
        self.reset.pack()

        self.user_input = Entry(width=20)
        self.user_input.pack()
        self.submit_button = Button(self.window, text="Submit", command=self.submit_name )
        self.submit_button.pack()

    def button_clicked(self):
            self.label.config(text="Contract Signed!")
            
    def reset_clicked(self):
            self.label.config(text="Contractor Name: ")

    def submit_name(self):
            typed_text= self.user_input.get()
            self.label.config(text=f"Contractor: {typed_text}")
root = Tk()
app = ContractManager(root)
root.mainloop()
