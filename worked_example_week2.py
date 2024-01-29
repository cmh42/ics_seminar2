#!/usr/bin/env python




##.*
import sys
import random

lower = 0
upper = 100
target = random.randint(lower, upper)

not_finished = True

while not_finished:
    guess = int(input("Enter a number between {} and {}: ".format(lower, upper)))
    if guess == target:
        print("Correct guess: {} is the target.".format(guess))
        not_finished = False
    elif guess > target:
        upper = guess
        print("Your guess {} was too high.".format(guess))
    else:
        lower = guess
        print("Your guess was too low.".format(guess))
    ##.*
