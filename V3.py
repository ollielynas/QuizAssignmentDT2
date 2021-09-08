import tkinter as tk
import json
import time
root = tk.Tk()
c=tk.Canvas(root)

state = "start" # this vairable will let me see what stage of the game is being played

def configure(event): # this event will be trigered when you resize the window so that i can move the item in it to fit the new size
    root.update()
    if state == "start":
        start.place(x = (root.winfo_width()//2)-(start.winfo_width()//2), y = (root.winfo_height()//2)-(start.winfo_height()//2))
    elif state == "countdown":
        countdown.place(x = (root.winfo_width()//2)-(countdown.winfo_width()//2), y = (root.winfo_height()//2)-(countdown.winfo_height()//2))


root.bind("<Configure>", configure) 



def gameloop():
    global state
    start.place_forget()
    state = ""
    welcome.pack_forget()
    root.update()
    countdown.place(x = -100, y = -100) # see explanation [1]
    print("state =",state)
    state = "countdown"
    countdown.place(x = (root.winfo_width()//2)-(countdown.winfo_width()//2), y = (root.winfo_height()//2)-(countdown.winfo_height()//2))
    for i in range(5):
        countdown.config(text=str(5-i))
        root.update()
        time.sleep(1)
    state = "playing"
    countdown.place_forget()
    min = 0
    sec = 0
    mls = 0
    timer = tk.Label(root, text="00:00.00", font=("Courier", 17))
    timer.place(x = 10, y = 0)
    starttime = time.perf_counter()
    while True:
        mls = time.perf_counter() - starttime
        sec = mls//100
        mls = mls - (mls//100)*100
        min = sec//60
        sec = sec-(sec//60)
        root.update()

        if mls < 10:
            strmls = "0"+str(round(mls, 2))
        else: strmls = str(round(mls, 2))
        if sec < 10:
            strsec = "0"+str(sec)
        else: strsec = str(sec)
        if min < 10:
            strmin = "0"+str(min)
        else: strmin = str(min)
        timer.config(text=strmin+":"+strsec+"."+strmls)
        mls += 1
        time.sleep(0.01)
Q_and_A = json.load(open("famousPersonv2.json", "r", encoding="utf-8"))

welcome = tk.Label(root, text="Welcome to my quizz game!", font=("Courier", 27))
countdown = tk.Label(root, text="", font=("Courier", 40))
start = tk.Button(root, text="Start", font=("Courier", 27), command=gameloop)

welcome.pack(padx=20, pady=20)



root.minsize(1000, 700)
start.place(x = -100, y = -100)
# [1]
#this is here because i need to know thw the width of the button but you can't know what that is before it is drawn. 
#to get arround this i fraw it off screan first and then get the size befor moveing it to where i want it.
root.update()
start.place(x = (root.winfo_width()//2)-(start.winfo_width()//2), y = (root.winfo_height()//2)-(start.winfo_height()//2))
print("width =",start.winfo_width())
c.pack(expand=True, fill=tk.BOTH)
root.mainloop()
