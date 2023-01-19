# Hangman implementation 

Allows users to enter a word which will then be hidden allowing another player to guess. Reaching a certain number of incorrect letter guesses will end the game as will guessing an incorrect word. Players will be prompted if they correctly guess the word or phrase.

Use / Example output : 

Hangman is a simple game where the goal is to guess the hidden word. You are allowed you to guess letters
or attempt to finish the whole word. Guessing the wrong word will result in a loss.
Pick a word or phrase :test
----
Guess a letter or the wordf
f  is not in the phrase/word.
You are now at  1 guesses of an allowed : 5
You have guessed these letters already! :  f
----
Guess a letter or the wordt
t--t
Guess a letter or the wordg
g  is not in the phrase/word.
You are now at  2 guesses of an allowed : 5
You have guessed these letters already! :  ftg
t--t
Guess a letter or the worde
te-t
Guess a letter or the words
Congratulations you win! The correct word/phrase was ' test '

example 2 : 
Pick a word or phrase :phrase
------
Guess a letter or the wordf
f  is not in the phrase/word.
You are now at  1 guesses of an allowed : 5
You have guessed these letters already! :  f
------
Guess a letter or the wordg
g  is not in the phrase/word.
You are now at  2 guesses of an allowed : 5
You have guessed these letters already! :  fg
------
Guess a letter or the wordj
j  is not in the phrase/word.
You are now at  3 guesses of an allowed : 5
You have guessed these letters already! :  fgj
------
Guess a letter or the wordq
q  is not in the phrase/word.
You are now at  4 guesses of an allowed : 5
You have guessed these letters already! :  fgjq
------
Guess a letter or the wordx
x  is not in the phrase/word.
You are now at  5 guesses of an allowed : 5
You have guessed these letters already! :  fgjqx
You are out of guesses, you lose.
The correct word was ' phrase  '
