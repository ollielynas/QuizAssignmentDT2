<style>
#header {
  display: flex;
  align-items: baseline;
  margin: 15px;
}


 /* blinking cursor */
#cursor {
  background: lime;
  line-height: 17px;
  margin-left: 3px;
  -webkit-animation: blink 0.8s infinite;
  width: 7px;
  height: 15px;
}

#example {
    background-colour: black;
}

@-webkit-keyframes blink {
  0% {background: #222}
  50% {background: white}
  100% {background: #222}



}

</style>

# QuizAssignmentDT2
 My plan is to create a word answer quiz app that can use a JSON files to produce a the questions and answers. inside the json file there will be a dictionary of questions and answers. the program will read the file and will be able to use it to produce a quiz. The quiz will be about the names of famous people. the user will answer by writing the name of the person. The user will be giveen a description of the person. They will have have to input the person's name into the command line. I also hope to at some point advance it from a command line app to a UI based app. 





 <br>
<a href="https://docs.google.com/document/d/1YEYmNcoKA3OZtZaOfMmidjnEeX_0ip5HQU4zY-r9T6M/edit?usp=sharing">evidence document link</a>


 ## Features that I need to add
 these are all the features I want in V1.
 I will add these in the order they appear
 - [x] JSON reading
 - [x] Command line text based questions
 - [x] tutorial 
 - [x] ignore spaces and caps


## Features I could add
these are things I want to add in later versions
- [x] timer
- [ ] tkinter UI        
- [ ] ony ask 10 questions but have much more in the json

## V1
version one begins with an intoduction and then asks the user 10 questions. if the user gets a question wrong then they will be asked it again later on. their score is calculated based on how many times they answered incorrectly.  the data for the questions and answers are stored in a dictonairy inside a JSON file. is that it means you will alwase be asked the same questions and the game will not have much replayability

## V2
in this version i have added a new wat to handle when the user inputs an incorrect answer insted of asking the user again later the name is displayed but all of the lettters are replaced with "_". every time the user inputs an incorrect answer one of the letters is filled in untill the answer is just given to them
here is an example of how it looks:

<div id="example">
(b_l_ g____)<br/>
who was the founder of microsoft?
<div id="header"><p>><br></p><div id="cursor"></div></div>
</div>

in this example the user has entered the wrong answer three times so three of the letters are already filled in for them


## V3