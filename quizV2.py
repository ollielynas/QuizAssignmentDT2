import json
from random import choice
import random
import os
import time

#reading the json file that the questions are kept in
Q_and_A = json.load(open("famousPerson.json", "r", encoding="utf-8"))

os.system("CLS")

# this allow people who allready know how to play a chance skip the tutorial while letting people who don't know how to play learn how to
start_input = input(
    "hello and welcome to my quiz\npress enter to begin or type \"?\" to read a tutorial\n")
if start_input == "?":
    input("you will be given the description of a famous person, you must type their full name and press enter. if they have a title eg. \"sir\", you do not need to include it. you do not have to capatalise either. at the end of the game you will be given how long it took you to finish the quiz as your score. \n good luck! \n\n")

question_counter = 0
mistakes = 0
tic = time.perf_counter()
while True:
    if question_counter == 10:
        break
    question_counter += 1
    
    os.system("CLS")
    display_list = []
    if len(list(Q_and_A.keys())) == 0:#this part checks if there are any more question left and if not it ends the loop which ends the quiz
        break
    answer = choice(list(Q_and_A.keys()))
    question = (Q_and_A[answer])
    answer_list = list(answer)
    for i in answer_list:
        if i == " ":
            display_list.append(" ")
        else:
            display_list.append("_")

    print("(",*display_list,")")
    user_input = input(question+"\n>")

    #this part mean that if the user adds an extra space before they answer or they capitalize their answer it will still be seen as correct
    processed_input = user_input.replace(" ", "").lower()
    processed_answer = answer.replace(" ", "").lower()
    
    while True:
        if processed_answer == processed_input:
            print("correct")#this will run if they are right
            del Q_and_A[answer]#it will also remove the question from the list of questions
            break
        else:
            
            while True:
                if display_list.count("_") == 0:
                    break
                letter = random.randint(0, len(display_list)-1)
                if display_list[letter] == "_":
                    display_list[letter] = answer_list[letter]
                    break
            os.system("CLS")
            print("incorrect\n+2 sec time penalty")
            time.sleep(2)
            os.system("CLS")
            print("(",*display_list,")")
            print(question)
            user_input = input("incorrect\n>")
            processed_input = user_input.replace(" ", "").lower()
            mistakes += 1 
    input("press enter for next question\n")
toc = time.perf_counter()
os.system("CLS")
input(("good job you finished the quiz. you made "+str(mistakes)+f" mistakes and it took you", int(toc - tic), "seconds\n"))