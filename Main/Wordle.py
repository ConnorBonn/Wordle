import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT) #sets up port 4 to be able to turn on green
GPIO.setup(6,GPIO.OUT) #sets up port 6 to be able to turn on red

##Main function to call checking functions
def main():
    wordle_answer()
    if user_input():
        print("YOU WIN")
    else:
        print("Try again!  The answer was:", answer[0].capitalize())

##Opening and handling file
file1 = open("words.txt")

##Used to hold the answerand the list of words
words = []
answer = []

##Functions used to pick the answer and put it into its own seperate list
def wordle_answer():
    #appends words in the file to the list
    words = file1.readlines()
    #appends a random word in the "words list" to answer
    answer.append(words[random.randrange(len(words))])
    #reappends each letter of the answer to a seperate index
    for letter in answer[0]:
        answer.append(letter)
    #deletes all excess in the lists
    words.clear()
    if len(answer) > 6:
        answer.pop
##Function to get users input and then check if its a valid word
def user_input():
    attempts = 0
    while attempts < 6:
        s = input("Guess: ")
        s = s.lower()
        if len(s) != 5:
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
            green()
            if correct == 5:
                return True
        elif guess[x] in answer:
            print(guess[x], "is in the word!")
            yellow()
        else:
            print(guess[x], "is incorrect :c")
            red()
main()

## Raspberry Pi functions
def red():
    GPIO.output(4,GPIO.HIGH) #turns green light on 
    time.sleep(1) #leaves light on for 1 second
    GPIO.output(4,GPIO.LOW) #turns green light off
    
def green():
    GPIO.output(6,GPIO.HIGH) #red on
    time.sleep(1) #leaves light on for 1 second
    GPIO.output(6,GPIO.LOW) #red off
    
def yellow():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)#red + green = yellow on
    time.sleep(1) 
    GPIO.output(4,GPIO.LOW)#
    GPIO.output(6,GPIO.LOW)# yellow off
    