#!/usr/bin/env python3.8

print('Welcome to quiz game')
print('You will be asked 5 questions')
print('You will be given 4 choices for each question')
print('Choose the correct answer')
print('You will be given 1 point for each correct answer')
print('You will be deducted 0.5 points for each wrong answer')
print('You will be given 0 points for each unattempted question')
print('You will be given 5 seconds to answer each question')


playing = input('Do you want to play? (yes/no): ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

# Q1
answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# Q2
answer = input('What does GPU stand for? ')
if answer.lower() == 'Graphics Processing Unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# Q3
answer = input('What does RAM stand for? ')
if answer.lower() == 'Random Access Memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# Q4
answer = input('What does PSU stand for? ')
if answer.lower() == 'Power Supply Unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'You got {score} questions correct')
print(f'You got {score/4*100}%')