import tkinter as tk
import json
import time
import random


from threading import Thread

class timer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        startTime = time.perf_counter()
        while True:
            currentTime = time.perf_counter()-startTime
            print(currentTime)
            time.sleep(0.1)

# reading the json file that the questions are kept in
Q_and_A = json.load(open("famousPersonv2.json", "r", encoding="utf-8"))

root = tk.Tk()


def checkAnswer():
    global Q_and_A, answer

    # this tells the computer to read from the answerbox starting from the first charcter and ending on the secound to last charcter. this is so that it dosen't
    # include the last charcter
    rawInupt = answerBox.get()
    processedInput = rawInupt.replace(' ', '').lower()

    if processedInput == answer.replace(' ', '').lower():
        print("correct")

    answerBox.delete(0, tk.END)

    del Q_and_A[answer]

    newQuestion()


def newQuestion():
    global Q_and_A, answer

    answer = random.choice(list(Q_and_A.keys()))
    question = Q_and_A[answer]

    text.config(text=question)

    # this pice of code will make the font smaller if the question is too big to fit on the screen
    fontsize = 24
    text.config(font=("Courier", fontsize))
    root.update()

    while text.winfo_width() == root.winfo_width():
        fontsize -= 1
        text.config(font=("Courier", fontsize))
        root.update()


def startFunc():
    start.destroy()
    # this variable will give me a refrense time of when the user started

    answerBox.pack()
    submitButton.pack(pady=30)
    timer()
    newQuestion()


submitButton = tk.Button(text="Submit", font=(
    "Courier", 24), command=lambda: checkAnswer())
answerBox = tk.Entry(root, text="Placeholder text", font=("Courier", 24))
text = tk.Label(root, text="Welcome to \"Famous Person quiz 2021\"",
                anchor='center', font=("Courier", 24))
text.pack(pady=30)
answer = ""
start = tk.Button(root, text="Click here to begin", anchor='center', font=(
    "Courier", 12), command=lambda: startFunc())
start.pack(pady=30)

root.geometry("1000x700")
root.mainloop()
