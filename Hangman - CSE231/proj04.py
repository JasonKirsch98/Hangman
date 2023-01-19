#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jasonkirschsmacbookpro
"""
# Project to play hangman
print("Hangman is a simple game where the goal is to guess the hidden word. You are allowed you to guess letters")
print("or attempt to finish the whole word. Guessing the wrong word will result in a loss.")
word_choice = input('Pick a word or phrase :')  # assigns value
while not (word_choice.isalpha() or word_choice.isspace()):  # check if only letters
    word_choice = input("Error please enter only letters")
word_choice = word_choice.lower()  # makes all lower case
word = ''  # empty string
guesses = ''  # empty string
for i in word_choice:  # Build hidden word into '------' format ie 'test' = '----'
    if i == " ":
        word = word + " "
    else:
        word = word + "-"
c = True
incremental = 0
max_guesses = 5
while c:  # Retrieve a prompt and compare to word
    print(word)  # show current score
    guess = input("Guess a letter or the word")  # prompts user
    check = 0
    if guess == word_choice:
        print(guess, "was the word! You win!")
        break
    else:
        if len(guess) == 1:  # Finds length

            guesses = guesses + guess  # guessed letter, add to list of guesses
            for i, ch in enumerate(word_choice):  # iterate thru chars, if correct replace '-' for letter
                if ch == guess:
                    word = word[0:i] + guess + word[i + 1:]
                    check = 1
        else:  # If length of guess doesn't equal length of word it's incorrect
            if len(guess) != len(word):
                print("Incorrect Answer, wrong length of word! you lose!")
                break
            else:
                if guess != word_choice:
                    print("Incorrect Answer, you lose!")
                    break
    if word.find("-") < 0:  # If no more - all chars guessed correctly, user wins
        print("Congratulations you win! The correct word/phrase was" , "'" , word_choice , "'" )

        c = False
    if check == 0:
        incremental = incremental + 1  # Wrong letter,
        print(guess, " is not in the phrase/word.")
        print("You are now at ", incremental, 'guesses of an allowed :', max_guesses)
        print("You have guessed these letters already! : ", guesses)
    if incremental >= max_guesses:  # how many incorrect guesses you get
        print("You are out of guesses, you lose.")
        print("The correct word was '", word_choice , " '")
        c = False


  
