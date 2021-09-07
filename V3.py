import tkinter as tk
import json
import time

root = tk.Tk()
c=tk.Canvas(root)


def gameloop():
    start.place_forget()
    welcome.pack_forget()
    root.update()
    countdown = tk.Label(root, text="5", font=("Courier", 27)).place(x = -100, y = -100) # see explanation [1]
    countdown.place(x = (root.winfo_width()//2)-(countdown.winfo_width()//2), y = (root.winfo_height()//2)-(countdown.winfo_height()//2))
    for i in range(5):
        root.update()
        countdown.config(text=i)
        time.sleep()
    timer = tk.Label(root, text="00.00", font=("Courier", 27)).place(x = 10, y = 0)
    while True:
        root.update()


Q_and_A = json.load(open("famousPersonv2.json", "r", encoding="utf-8"))

welcome = tk.Label(root, text="Welcome to my quizz game!", font=("Courier", 27)).pack(padx=20, pady=20)
start = tk.Button(root, text="Start", font=("Courier", 27), command=gameloop)


root.minsize(1000, 700)
start.place(x = -100, y = -100)
#[1]
#this is here because i need to know thw the width of the button but you can't know what that is before it is drawn. 
#to get arround this i fraw it off screan first and then get the size befor moveing it to where i want it.
root.update()
start.place(x = (root.winfo_width()//2)-(start.winfo_width()//2), y = (root.winfo_height()//2)-(start.winfo_height()//2))
print("width =",start.winfo_width())
c.pack(expand=True, fill=tk.BOTH)
root.mainloop()
