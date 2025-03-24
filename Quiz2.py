# This program uses dictionaries inside the list.

from easygui import*
import sys

score = 0

name = enterbox('Enter your name : ')
if name is None or name.strip() == "":
    sys.exit('No name entered. Quiz exited.')
# Dictionary
quiz = [ {'question':'10x2','options':['10','20','60'],'answer':'20'},
         {'question':'50+9','options':['10','59','60'],'answer':'59'},
         {'question':'60/3','options':['10','20','60'],'answer':'20'} ]

# Routine
for item in quiz:
    question = item['question']
    options = item['options']
    answer = item['answer']

    user_choice = buttonbox(f'what is the answer for {question}? ',choices = options)
    if user_choice is None:
        sys.exit('quiz exited by user')
    elif user_choice == answer:
        msgbox('Correct')
        score = score+1
    else:
        msgbox(f'Incorrect. The correct answer is {answer}')

# Score Calculations
total_questions = len(quiz)
percent = (100*score)/ total_questions
msgbox(f'{name}: {score }/{total_questions}, {percent :.2f}%\n')

# Writing details to external file
with open ('quiz_results.txt', 'a')as file:
    file.write(f'{name}:{score}/{total_questions}, {percent :.2f}%\n')
msgbox('Your score has been saved. Thank you for playing')



    
