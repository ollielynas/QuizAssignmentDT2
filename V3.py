import tkinter as tk
import json
import time
import random
from threading import Thread

# ANCHOR when editing this script i used the anchor  extention which alows
# me to jump to parts of the code so the it why some of my comments
# start with the #ANCH0R tag


class timer(Thread):  # the  timer is run on a different thread
    # so that it works at a constant rate no matter what
    # the rest of the code is doing
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        global currentTime, startTime
        startTime = time.perf_counter()
        while True:
            currentTime = time.perf_counter()-startTime
            time.sleep(0.1)
            timerLabel.config(text=round(currentTime, 2))

# reading the json file that the questions are kept in
file = open("famousPersonv2.json", "r", encoding="utf-8")
Q_and_A = json.load(file)
file.close()

root = tk.Tk()

# cheaks if the answer is correct
def checkAnswer():  # ANCHOR cheack answer
    global Q_and_A, answer, numberOfQuestions

    # this tells the computer to read from the answerbox starting
    # from the first charcter and ending on the secound to last charcter.
    # this is so that it dosen't include the last charcter
    rawInupt = answerBox.get()

    # added so that i could skip to the end of quiz when testing
    if rawInupt == ">>END()":
        numberOfQuestions = 10
        newQuestion()
        return()
    processedInput = rawInupt.replace(' ', '').lower()
    processedInput = ''.join([i for i in processedInput if i.isalpha()])
    answerBox.delete(0, tk.END)  # clears the answer box
    if processedInput == answer.replace(' ', '').lower():
        print("correct")
        del Q_and_A[answer]  # removes that question from list of options
        newQuestion()
    else:
        del Q_and_A[answer]
        # prevents the user from clicking enter during the time penalty
        submitButton["state"] = tk.DISABLED

        # this pice of code will make the font smaller if
        # the question is too big to fit on the screen
        text.config(text="Incorrect - 5 second penalty")
        fontsize = 24
        text.config(font=("Courier", fontsize))
        root.update()
        while text.winfo_width() == root.winfo_width():
            fontsize -= 1
            text.config(font=("Courier", fontsize))
            root.update()

        print("incorrect")
        startTimeTimer = time.perf_counter()

        # here i use time.perf to allow the windo to continue to update
        while time.perf_counter()-startTimeTimer < 5:
            root.update()
        # allows the user to click the enter button again
        submitButton["state"] = tk.NORMAL
        newQuestion()

# genorates a new question
def newQuestion():
    global Q_and_A, answer, numberOfQuestions, currentTime
    numberOfQuestions += 1
    if numberOfQuestions > 10:
        answerBox.delete(0, tk.END)  # clears the answer box
        print("score:", currentTime)
        for widget in root.winfo_children():
            widget.forget()

        packStartMenu()
        endScore.config(text="your score is: "+str(round(currentTime, 2))+"s")
        endScore.pack(pady=20)
        text.config(text="Congratulations on completing the quiz")
        start.config(text="CLick here to restart")
        file = open("famousPersonv2.json", "r", encoding="utf-8")
        Q_and_A = json.load(file)
        file.close()
        return
    answer = random.choice(list(Q_and_A.keys()))
    question = Q_and_A[answer]

    text.config(text=question)

    # this pice of code will make the font smaller if the
    # question is too big to fit on the screen
    fontsize = 24
    text.config(font=("Courier", fontsize))
    root.update()
    while text.winfo_width() == root.winfo_width():
        fontsize -= 1
        text.config(font=("Courier", fontsize))
        root.update()


# this function is used to switch to the begin page to the playing page,
# it is trigered by the start button
def startFunc():
    global numberOfQuestions, startTime
    numberOfQuestions = 0
    startTime = time.perf_counter()
    try:
        endScore.forget()
    except Exception as e:
        print(e)

    start.forget()  # removes the start button when clicked
    # this variable will give me a refrense time of when the user started
    timerLabel.pack(side=tk.LEFT, anchor=tk.NW)
    answerBox.pack()
    submitButton.pack(pady=30)

    newQuestion()

answer = ""
numberOfQuestions = 0

# defineing elemnets
timerLabel = tk.Label(root, text="0.00", font=("Courier", 12), padx=10)
submitButton = tk.Button(text="Submit", font=(
    "Courier", 24), command=lambda: checkAnswer())
root.bind('<Return>',lambda event:checkAnswer())

answerBox = tk.Entry(root, text="Placeholder text", font=("Courier", 24))
text = tk.Label(root, text="Welcome to \"Famous Person quiz 2021\"",
                anchor='center', font=("Courier", 24))

start = tk.Button(root, text="Click here to begin", anchor='center', font=(
    "Courier", 12), command=lambda: startFunc())


endScore = tk.Label(root, text="your final score is:",
                    anchor='center', font=("Courier", 16))

# packs the elemts of the start menu
def packStartMenu():
    text.pack(pady=50)
    start.pack(pady=40)


packStartMenu()
timer()

root.geometry("1000x700")
root.mainloop()
