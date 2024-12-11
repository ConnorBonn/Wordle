#import RPi.GPIO as GPIO
import time
import random

def main():
    wordle_answer()
    if user_input():
        print("YOU WIN")
    else:
        print("Try again!  The answer was:", answer[0].capitalize())
##Opening and handling file
file1 = open("words.txt")
words = []
answer = []
def wordle_answer():
    for line in file1:
        words.append(line)
    answer.append(words[random.randrange(297)])
    for letter in answer[0]:
        answer.append(letter)
    
    if len(answer) > 6:
        answer.pop
##Function to get users input and then check if its a valid word
def user_input():
    attempts = 0
    while attempts < 6:
        s = input("Guess: ")
        s = s.lower()
        if len(s) < 5:
            continue
        else:
            attempts += 1
            if check_answer(s):
                return True
                break
    return False
##Checks users answer
def check_answer(e):
    guess = []
    correct = 0
    for letter in e:
        guess.append(letter)
    for x in range(5):
        if guess[x] == answer[x + 1]:
            print(guess[x], "is correct!")
            correct += 1
            if correct == 5:
                return True
        elif guess[x] in answer:
            print(guess[x], "is in the word!")
        else:
            print(guess[x], "is incorrect :c")
main()