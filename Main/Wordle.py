import RPi.GPIO as GPIO
import time
import random

##Opening and handling file
file1 = open["words.txt"]
word = []
def wordle_answer():
    for line in file1:
        word = [line]
        print(word)
##Function to get users input and then check if its a valid word
def user_input():
    while True:
        s = input("Guess: ")
wordle_answer()
print("Hello")
