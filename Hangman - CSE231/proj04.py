#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jasonkirschsmacbookpro
"""
#Project to play hangman
print("Hangman is a simple game that allows you to guess letters or words")#Prompts user
word_choice = input('Pick a word or phrase') # assigns value
while not word_choice.isalpha(): #check if only letters
    print("Error please enter only letters")
word_choice = word_choice.lower() #makes all lower case
word = '' #empty string
guesses = '' #empty string
for i in word_choice: #Build hidden word into '---- -----' format ie 'bank stand'
    if i == " ":
        word = word + " "
    else:
        word = word + "-"
c = True    
incremental = 0

        
while c: # Retrieve a prompt and compare to word
    print(word) #show current score
    guess = input("Guess a letter or word") #prompts user
    if len(guess) == 1: #Finds length
         
        guesses = guesses + guess #guessed letter, add to list of guesses
        for i,ch in enumerate(word_choice): #iterate thru chars, if correct replace '-' for letter
            if ch == guess:
                word = word[0:i] + guess + word[i+1:]
    else: # If length of guess doesn't equal length of word it's incorrect
        if len(guess) == len(word):
            print("Incorrect Answer")
        else:
            if guess != word_choice:
                print("Incorrect Answer")
                c = False 
    if word.find("-")<0:#If no more - all chars guessed correctly, user wins
        c = True
        print("Congratulations you win!") 
    incremental = incremental + 1 #Takes count of guesses
    print("Guesses " + str(incremental) +  " " + guesses)
    if incremental > 5: #how many guesses you get
        c = False           
    
            
