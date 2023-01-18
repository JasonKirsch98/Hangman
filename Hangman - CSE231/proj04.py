#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:45:56 2017

@author: jasonkirschsmacbookpro
"""
#Project to play hangman
print("Hangman is a simple game that allows you to guess letters or words")#Prompts user
word_choice = input('Pick a word or phrase') # assigns value
while not word_choice.isalpha():
    print("Error please enter only letters")
word_choice = word_choice.lower() #makes all lower case
word = '' #empty string
guesses = '' #empty string
for i in word_choice: #Building to string
    if i == " ":
        word = word + " "
    else:
        word = word + "-"
c = True    
incremental = 0

        
while c: # Retrieve a prompt and compare to word
    print(word)
    guess = input("Guess a letter or word") #prompts user
    if len(guess) == 1: #Finds length
         
        guesses = guesses + guess
        for i,ch in enumerate(word_choice):
            if ch == guess:
                word = word[0:i] + guess + word[i+1:]
    else: # If length of guess doesn't equal length of word it's incorrect
        if len(guess) == len(word):
            print("Incorrect Answer")
        else:
            if guess != word_choice:
                print("Incorrect Answer")
                c = False 
    if word.find("-")<0:#If no more - then user wins
        c = True
        print("Congratulations you win!") 
    incremental = incremental + 1 #Takes count of guesses
    print("Guesses " + str(incremental) +  " " + guesses)
    if incremental > 5:
        c = False           
    
            
#6
#5
#6
#5
#1