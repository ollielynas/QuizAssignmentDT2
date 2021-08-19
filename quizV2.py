import json
from random import choice
import os

#reading the json file that the questions are kept in
Q_and_A = json.load(open("famousPerson.json", "r", encoding="utf-8"))

# this allow people who allready know how to play a chance skip the tutorial while letting people who don't know how to play learn how to
start_input = input(
    "hello and welcome to my quiz\npress enter to begin or type \"?\" to read a tutorial\n")
if start_input == "?":
    input("you will be given the description of a famous person, you must type their full name and press enter. you do not need to include any titles they may hold\n")

mistakes = 0

while True:
    if len(list(Q_and_A.keys())) == 0:#this part checks if there are any more question left and if not it ends the loop which ends the quiz
        break
    answer = choice(list(Q_and_A.keys()))
    question = (Q_and_A[answer])

    os.system("CLS")
    user_input = input(question+"\n>")

    #this part mean that if the user adds an extra space before they answer or they capitalize their answer it will still be seen as correct
    processed_input = user_input.replace(" ", "").lower()
    processed_answer = answer.replace(" ", "").lower()

    if processed_answer == processed_input:
        print("correct")#this will run if they are right
        del Q_and_A[answer]#it will also remove the question from the list of questions
    else:
        print("incorrect") # if they are incorrect, it will add a point to the counter and will ask them again later
        mistakes += 1 
    input("press enter for next question\n")

os.system("CLS")
input("good job you finished the quiz. you made "+str(mistakes)+" mistakes\n")