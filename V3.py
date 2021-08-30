import tkinter as tk
import json

root = tk.Tk()
c=tk.Canvas(root)

def begin():
    welcome.place(relx = 0.5,  
                   rely = 0.5, 
                   anchor = 'center') 


Q_and_A = json.load(open("famousPersonv2.json", "r", encoding="utf-8"))

welcome = tk.Label(root, text="Welcome to my quizz game!", font=("Courier", 27)).pack(padx=20, pady=20)
start = tk.Button(root, text="Start", font=("Courier", 27), command=begin())

start.pack()

c.pack(expand=True, fill=tk.BOTH)
root.minsize(1000, 700)


root.mainloop()