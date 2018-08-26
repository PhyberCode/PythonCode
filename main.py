import os
import sys
import random
from random import randint
import webbrowser
import datetime
#variables

#mobs

#player
playerhealth = 200

#Functions
def options():
    print("Options:")
    print("1) Information")
    print("2) Random number generator (Command is: Random)")
    print("3) URL")
    print("4) ")
    print("All \'options\' are case sensitive by the way.")

def urlsearch():
    #webbrowser.open()
    print("Welcome to the url search engine.")
    print("The URL must be properly formatted such as: https://website.com/")
    urlchoice = input("Enter a URL:")
    webbrowser.open(urlchoice)
#multiscript

print("Welcome to my python multiscript, I don\'t have a huge use for it right now... \n Except to just show off.")
print("\n")

while True:
    options()

    choice = input(":")

    if choice == "Random":
        print("Welcome to my random number generator.")
        randomchoice = input("Default/Custom:")
        if randomchoice == "Default":
            print("Generating a number between 1 and 12.")
            randomnumber = (randint(1,12))
            print("Your number is ",randomnumber,".")

        if randomchoice == "Custom":
            randomfirst = input("First number boundary: ")
            randomsecond = input("Second number boundary: ")
            print("Generating number between ",randomfirst," and ",randomsecond,".")
            randombumber1 = (randint(randomfirst,randomsecond))
            print("Your number is ",randombumber1,".")

    if choice == "Information":
        print("So I coded this in an IDE called Atom, it doessn\'t help the user apart from automatic indentation.")
        print("I like that a lot since it helped me actually learn Python rather than use osmehting such as Pycharm, \n which does almost everything for you.")
        print("My name\'s Cameron, I\'m 16 for now.")
        print("I don\'t have a definitive reason why I made this, but I can use it for future reference.")

    if choice == "URL":
        urlsearch()

    if choice == "a":
        print("A!")
