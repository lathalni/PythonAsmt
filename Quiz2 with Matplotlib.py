# This program uses dictionaries inside the list.

from easygui import*
import sys
import matplotlib.pyplot as plt

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

# --- Matplotlib Visualization ---

students = []
scores = []

try:
    with open('quiz_results.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            student_name = parts[0]
            score_part = parts[1].split('/')[0]
            students.append(student_name)
            scores.append(int(score_part))
except FileNotFoundError:
    msgbox('No previous results found for plotting.')

# --- Plotting Leaderboard ---
plt.figure(figsize=(10, 6))
bars = plt.bar(students, scores, color='skyblue', edgecolor='black')

# Highlight the latest student's bar in a different color
bars[-1].set_color('green')

# Add text labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, yval, ha='center', va='bottom')

plt.title(f'Quiz Leaderboard (Latest: {name})')
plt.xlabel('Student Name')
plt.ylabel('Score')
plt.ylim(0, total_questions + 1)  # Ensures bar space at the top
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
    
