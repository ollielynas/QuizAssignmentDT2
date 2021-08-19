import json
from random import choice
import os

Q_and_A = json.load(open("famousPerson.json", "r", encoding="utf-8"))

input("hello and welcome to my quiz\npress enter to begin")

while True:
    question = (Q_and_A[choice(list(Q_and_A.keys()))])
    answer = Q_and_A[question]
    os.system("CLS")
    user_input = input(question,"\n>")
    processed_input = user_input.replace(" ", "").lower()
    processed_answer = answer.replace(" ", "").lower()
    if processed_answer == processed_input:
        print("correct")
    else:
        print("incorrect")