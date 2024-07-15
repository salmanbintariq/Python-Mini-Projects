import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")

def time():
    string = strftime("%H:%M:%S %p\n %m/%d/%Y")
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='red')
label.pack(anchor='center')

time()
root.mainloop()
