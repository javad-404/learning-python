import tkinter

window = tkinter.Tk()
print("My first Gui program")
window.minsize(width=500, height=600)
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()